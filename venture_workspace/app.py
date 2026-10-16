"""Venture OS Workspace v0.1 — internal, server-hosted Streamlit interface.

Start (private loopback): streamlit run venture_workspace/app.py --server.address 127.0.0.1
All Core credentials remain server-side. No multi-client access is supported.
"""
from __future__ import annotations

import hmac
import os
from html import escape
from pathlib import Path
import sys

import streamlit as st

# Support streamlit run venture_workspace/app.py from repository root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from venture_workspace.core_store import CoreStateStore, WorkspaceError, summary

st.set_page_config(page_title="Venture OS · Designeo", page_icon="◈", layout="wide",
                   initial_sidebar_state="expanded")

st.markdown("""
<style>
.stApp {background: #f8f8f6; color: #1c1c1c;}
[data-testid="stSidebar"] {background: #171717;}
[data-testid="stSidebar"] * {color: #f4f4f2;}
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] * {color: #bababa;}
.block-container {max-width: 1320px; padding-top: 2.1rem;}
.v-eyebrow {font-size: .76rem; font-weight: 700; letter-spacing: .14em; color: #c63d23; text-transform: uppercase;}
.v-title {font-size: 2.3rem; font-weight: 750; letter-spacing: -.05em; line-height: 1.08; margin: .32rem 0;}
.v-desc {color: #6b6b69; font-size: .96rem; margin: .4rem 0 1.5rem;}
.v-card {border: 1px solid #e1dfdb; background: #fff; border-radius: 12px; padding: 20px 22px; min-height: 156px; margin: 5px 0 9px;}
.v-card strong {display: block; font-size: 1.1rem; color: #222; margin: 9px 0 8px;}
.v-card small {color: #737373;}
.v-card p {color: #595957; line-height: 1.45; font-size: .87rem;}
.v-pill {display: inline-block; padding: 4px 9px; border-radius: 20px; background: #f3e6e1; color: #ae351c; font-size: .71rem; font-weight: 700;}
.v-meta {font-size: .74rem; color: #777; letter-spacing: .04em;}
.v-rule {border-top: 1px solid #e6e4df; margin: 12px 0 20px;}
.v-section {font-size: 1.05rem; font-weight: 750; margin: 24px 0 12px;}
div[data-testid="stMetric"] {background: white; border: 1px solid #e1dfdb; padding: 16px 18px; border-radius: 10px;}
[data-testid="stButton"] button[kind="primary"] {background: #d3341a; border-color: #d3341a;}
</style>
""", unsafe_allow_html=True)


def access_gate():
    expected = os.getenv("VENTURE_WORKSPACE_ADMIN_PASSWORD", "")
    if not expected:
        st.error("Configuração incompleta: definir VENTURE_WORKSPACE_ADMIN_PASSWORD no servidor. Acesso bloqueado.")
        st.stop()
    if st.session_state.get("venture_admin") is True:
        return
    st.markdown('<div class="v-eyebrow">Designeo · área privada</div>', unsafe_allow_html=True)
    st.title("Venture OS")
    st.write("Acesso interno ao Workspace. Não está preparado para utilizadores externos.")
    supplied = st.text_input("Palavra-passe", type="password")
    if st.button("Entrar", type="primary"):
        if hmac.compare_digest(supplied.encode(), expected.encode()):
            st.session_state["venture_admin"] = True
            st.rerun()
        else:
            st.error("Credenciais inválidas.")
    st.stop()


def intro(kicker, title, subtitle):
    st.markdown(
        f'<div class="v-eyebrow">{escape(kicker)}</div>'
        f'<div class="v-title">{escape(title)}</div>'
        f'<div class="v-desc">{escape(subtitle)}</div>',
        unsafe_allow_html=True,
    )


def display_name(item):
    return f"{item.get('name', 'Sem nome')} · {item['id']}"


def card(item):
    title = escape(str(item.get("name", "Sem nome")))
    cid = escape(str(item["id"]))
    stage = escape(str(item.get("stage", "Por classificar")).replace("_", " "))
    problem = escape(str(item.get("problem", "Problema por definir")))
    st.markdown(
        f'<div class="v-card"><div class="v-meta">{cid}</div>'
        f'<strong>{title}</strong><span class="v-pill">{stage}</span>'
        f'<p>{problem[:210]}</p><small>Sem validação comercial confirmada</small></div>',
        unsafe_allow_html=True,
    )
    if st.button("Abrir no Workspace →", key="open_" + item["id"], use_container_width=True):
        st.session_state["selected"] = item["id"]
        st.session_state["section"] = "Workspace"
        st.rerun()


def render_list(values, empty="Ainda sem informação registada."):
    if not values:
        st.caption(empty)
    else:
        for value in values:
            st.markdown("• " + str(value))


def labeled_value(title, value, empty="Por definir"):
    st.markdown(f"**{title}**")
    st.write(value if value not in (None, "", [], {}) else empty)


access_gate()
demo = os.getenv("VENTURE_WORKSPACE_DEMO", "") == "1"
writes = os.getenv("VENTURE_WORKSPACE_ENABLE_LEGACY_WRITES", "") == "1"

@st.cache_resource
def core_store():
    return CoreStateStore(
        os.getenv("DESIGNEO_CORE_URL", ""),
        os.getenv("DESIGNEO_CORE_API_TOKEN", ""),
        allow_legacy_writes=writes,
    )

store = None
if demo:
    candidates = [{
        "schema": "designeo.venture.candidate.v0.1",
        "id": "VF-DEMO-01", "name": "Projeto demonstrativo",
        "stage": "G0_discovery", "decision": "INVESTIGATE",
        "problem": "Hipótese fictícia de necessidade, apenas para pré-visualizar a interface.",
        "value_proposition": "Exemplo de proposta de valor",
        "customer_segments": ["Segmento demonstrativo"],
        "hypotheses": ["Uma necessidade real será confirmada por entrevistas"],
        "experiments": [{"name": "Entrevistas iniciais", "status": "planned"}],
        "metrics": {"retention": None}, "costs": {"status": "unmeasured"},
        "risks": ["Hipótese não comprovada"], "business_validated": False,
        "_updated_at": "demo",
    }]
else:
    try:
        store = core_store()
        candidates = store.list_candidates()
    except WorkspaceError as exc:
        st.error(f"Não foi possível ler o Designeo OS Core: {exc}")
        st.info("Verifica a ligação interna, as credenciais de serviço e as permissões. Não existe uma base de dados alternativa neste Workspace.")
        st.stop()

st.sidebar.markdown("### ◈ DESIGNEO")
st.sidebar.caption("VENTURE OS · WORKSPACE")
if "section" not in st.session_state:
    st.session_state["section"] = "Board"
section = st.sidebar.radio(
    "Navegação", ["Board", "Workspace", "Experiências", "SaaS Core"],
    key="section", label_visibility="collapsed",
)
st.sidebar.divider()
st.sidebar.caption(f"{len(candidates)} candidatos registados")
st.sidebar.caption("Modo demonstração" if demo else "Ligado ao Core · dados persistentes")
if not demo and not writes:
    st.sidebar.caption("Edição protegida · apenas leitura")
if st.sidebar.button("Terminar sessão"):
    st.session_state.pop("venture_admin", None)
    st.rerun()

if section == "Board":
    intro("Gestão de oportunidades", "Venture Board", "Investigar → testar → validar → decidir. Uma visão comum de todos os candidatos.")
    numbers = summary(candidates)
    metrics = st.columns(4)
    for col, label, value in zip(
        metrics,
        ["Candidatos", "Em descoberta", "Experiências por realizar", "Negócios validados"],
        [numbers["total"], numbers["in_discovery"], numbers["pending_experiments"], numbers["validated_businesses"]],
    ):
        col.metric(label, value)

    st.markdown('<div class="v-section">Portefólio</div>', unsafe_allow_html=True)
    if not candidates:
        st.info("Ainda não existem candidatos no âmbito venture-factory do Designeo OS Core.")
    else:
        for i in range(0, len(candidates), 2):
            for col, item in zip(st.columns(2), candidates[i:i + 2]):
                with col:
                    card(item)
    st.markdown('<div class="v-section">Método de decisão</div>', unsafe_allow_html=True)
    st.caption("G0 Descoberta → G1 Validação → G2 Piloto → G3 Viabilidade → G4 Produto. Avanços exigem revisão humana e evidência; o Board não aprova operações externas.")

elif section == "Workspace":
    intro("Ficha de trabalho", "Venture Workspace", "O conteúdo vem diretamente do Designeo OS Core; a ficha não substitui os dados operacionais de cada aplicação.")
    if not candidates:
        st.info("Não existem fichas disponíveis.")
        st.stop()
    ids = [item["id"] for item in candidates]
    if st.session_state.get("selected") not in ids:
        st.session_state["selected"] = ids[0]
    selected = st.selectbox(
        "Escolher candidato", ids, index=ids.index(st.session_state["selected"]),
        format_func=lambda cid: display_name(next(item for item in candidates if item["id"] == cid)),
    )
    st.session_state["selected"] = selected
    item = next(c for c in candidates if c["id"] == selected)
    st.subheader(item.get("name", item["id"]))
    st.caption(f"{item['id']}  ·  {item.get('stage', 'Não classificado')}  ·  {item.get('decision', 'Sem decisão')}")
    tabs = st.tabs(["Visão", "Hipóteses", "Experiências", "Métricas e custos", "Riscos", "Edição"])
    with tabs[0]:
        labeled_value("Problema a resolver", item.get("problem"))
        labeled_value("Proposta de valor", item.get("value_proposition"))
        st.markdown("**Públicos propostos**")
        render_list(item.get("customer_segments", []))
        labeled_value("Próxima ação", item.get("next_action") or item.get("next_gate"))
        st.caption("O estado de mercado é uma hipótese até existir evidência externa verificável.")
    with tabs[1]:
        st.markdown("#### Hipóteses a testar")
        render_list(item.get("hypotheses", []))
    with tabs[2]:
        experiments = item.get("experiments", [])
        if not experiments:
            st.info("Ainda não foram definidas experiências.")
        for e in experiments:
            if not isinstance(e, dict):
                continue
            with st.expander(str(e.get("name", "Experiência")), expanded=True):
                st.write("Estado: " + str(e.get("status", "por definir")))
                if e.get("target"):
                    st.write("Alvo: " + str(e["target"]))
        st.caption("Uma experiência planeada não constitui validação nem autorização para contactar terceiros.")
    with tabs[3]:
        left, right = st.columns(2)
        with left:
            st.markdown("**Métricas registadas**")
            for key, value in (item.get("metrics") or {}).items():
                st.write(f"{key}: {value if value is not None else 'Por medir'}")
        with right:
            st.markdown("**Economia**")
            for key, value in (item.get("costs") or {}).items():
                st.write(f"{key}: {value if value is not None else 'Por medir'}")
        st.warning("Sem métricas de procura ou margens verificadas, não classificar como negócio validado.")
    with tabs[4]:
        st.markdown("**Riscos e dependências**")
        render_list(item.get("risks", []))
        if isinstance(item.get("evidence"), dict):
            doc = item["evidence"].get("validation_document")
            if isinstance(doc, str) and doc.startswith("https://github.com/"):
                st.link_button("Consultar fonte documental", doc)
    with tabs[5]:
        st.markdown("#### Atualizar a hipótese de negócio")
        if demo:
            st.info("A demonstração não guarda alterações.")
        elif not writes:
            st.info("Edição bloqueada enquanto a integração com revisões atómicas do Core não estiver pronta. A consulta dos registos existentes já é funcional.")
        else:
            st.warning("Modo interno de escritor único. A verificação de versão ainda não é transacional; não usar com vários editores.")
            with st.form("edit_candidate"):
                problem = st.text_area("Problema", value=item.get("problem", ""), max_chars=3000)
                value_proposition = st.text_area("Proposta de valor", value=item.get("value_proposition", ""), max_chars=3000)
                next_action = st.text_area("Próxima ação", value=item.get("next_action", ""), max_chars=3000)
                notes = st.text_area("Notas de investigação", value=item.get("notes", ""), max_chars=3000)
                submitted = st.form_submit_button("Guardar campos de investigação", type="primary")
                if submitted:
                    try:
                        store.update_candidate(selected, item["_updated_at"], {
                            "problem": problem, "value_proposition": value_proposition,
                            "next_action": next_action, "notes": notes,
                        })
                    except WorkspaceError as exc:
                        st.error(str(exc))
                    else:
                        st.success("Alterações guardadas no Core.")
                        st.rerun()

elif section == "Experiências":
    intro("Validação de hipóteses", "Experiências", "Experiências planeadas e respetivo estado, sem confundir intenção com evidência.")
    total = 0
    for item in candidates:
        experiments = item.get("experiments", [])
        for experiment in experiments:
            if not isinstance(experiment, dict):
                continue
            total += 1
            with st.expander(item.get("name", item["id"]) + " · " + str(experiment.get("name", "Experiência")), expanded=True):
                st.write("**Estado:** " + str(experiment.get("status", "por definir")))
                st.write("**Objetivo:** " + str(experiment.get("target", "Ainda não definido")))
                st.caption("Consultar o Workspace para o contexto completo da hipótese.")
    if not total:
        st.info("Nenhuma experiência registada.")

elif section == "SaaS Core":
    intro("Infraestrutura transversal", "SaaS Core", "Mapa de componentes e dependências — proposta técnica, não declaração de funcionalidades auditadas.")
    st.table([
        {"Componente": "Projetos, memória, tarefas", "Direção": "Reutilizar Designeo OS Core", "Prioridade": "Já disponível"},
        {"Componente": "Candidatos Venture", "Direção": "Registo no Core e vista Workspace", "Prioridade": "V0.1"},
        {"Componente": "Revisões atómicas", "Direção": "Reconciliar Core PR #30", "Prioridade": "Crítica"},
        {"Componente": "Autenticação e isolamento", "Direção": "Auditar identidades e permissões", "Prioridade": "Crítica"},
        {"Componente": "Backups e restauro", "Direção": "Validar recuperação e rollback", "Prioridade": "Crítica"},
        {"Componente": "Gateway IA e custos", "Direção": "Reutilizar provedores existentes", "Prioridade": "Posterior"},
        {"Componente": "Subscrições e pagamentos", "Direção": "Só após validação de mercado", "Prioridade": "Adiada"},
    ])
    st.warning("Workspace apenas para administração interna. Não publicar como plataforma multiutilizador nem colocar tokens do Core no frontend.")
