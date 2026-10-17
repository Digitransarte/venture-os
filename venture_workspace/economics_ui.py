"""Read-only SaaS feasibility workspace; no payment, model or Core calls."""
from __future__ import annotations

import streamlit as st

from venture_workspace.economics import Scenario, simulate


def _money(value: float) -> str:
    return f"{value:,.2f} €".replace(",", " ").replace(".", ",")


def render_economics(candidates: list[dict]) -> None:
    st.markdown('<div class="v-eyebrow">Venture Factory · Avaliação de negócio</div>', unsafe_allow_html=True)
    st.markdown('<div class="v-title">Viabilidade SaaS</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="v-desc">Simular o custo de disponibilizar uma aplicação a terceiros, '
        'sem confundir estimativas com resultados observados.</div>',
        unsafe_allow_html=True,
    )
    name = st.selectbox("Candidato", ["Cenário genérico"] + [
        f"{x.get('name', x['id'])} · {x['id']}" for x in candidates
    ])
    st.caption(f"Análise privada de: {name}. Não modifica a ficha nem comunica com fornecedores de IA.")
    mode = st.radio("Modelo de disponibilização", [
        "Interno — ChatGPT assistido",
        "Piloto — IA por utilização",
        "SaaS — aplicação pública",
    ], horizontal=True)
    explanations = {
        "Interno — ChatGPT assistido":
            "Ferramenta interna assistida por ChatGPT. Um resultado familiar positivo não mede o custo de operar para terceiros.",
        "Piloto — IA por utilização":
            "Automatizar apenas tarefas selecionadas e medir tokens, qualidade e custo real por utilizador, com segurança validada.",
        "SaaS — aplicação pública":
            "Exige identidade, isolamento de dados, operação, suporte, faturação, segurança e sustentabilidade demonstráveis.",
    }
    st.info(explanations[mode])
    st.caption(
        "Os preços da API não estão predefinidos: variam por fornecedor, modelo, contexto, "
        "ferramenta e data. Introduz taxas em EUR, já convertidas, e valores mensais sem IVA. "
        "Uma assinatura ChatGPT não cobre automaticamente chamadas à API."
    )
    with st.expander("1 · Clientes e receitas hipotéticas", expanded=True):
        x, y = st.columns(2)
        with x:
            clients = st.number_input("Famílias/contas pagantes", min_value=0, max_value=1000000, value=0, step=10)
        with y:
            price = st.number_input("Preço mensal por conta, sem IVA (€)", min_value=0.0, value=0.0, step=1.0, format="%.2f")
    with st.expander("2 · Consumo de IA — por conta e por mês", expanded=True):
        a, b, c = st.columns(3)
        with a:
            calls = st.number_input("Chamadas à IA por conta/mês", min_value=0, value=0, step=10)
        with b:
            input_tokens = st.number_input("Tokens entrada/chamada", min_value=0, value=0, step=100)
        with c:
            output_tokens = st.number_input("Tokens saída/chamada", min_value=0, value=0, step=100)
        a, b, c = st.columns(3)
        with a:
            input_rate = st.number_input("€ / milhão tokens entrada", min_value=0.0, value=0.0, format="%.4f")
        with b:
            output_rate = st.number_input("€ / milhão tokens saída", min_value=0.0, value=0.0, format="%.4f")
        with c:
            extras = st.number_input("Voz, OCR, outras ferramentas / conta (€)", min_value=0.0, value=0.0, format="%.2f")
        st.caption("Documentos extensos, transcrição, pesquisa e modelos multimodais podem acrescentar custos que não se resumem aos tokens de texto.")
        st.link_button("Consultar preços atuais de API", "https://developers.openai.com/api/docs/pricing")
    with st.expander("3 · Infraestrutura e serviço", expanded=False):
        a, b, c = st.columns(3)
        with a:
            hosting = st.number_input("Hosting e base de dados / mês (€)", min_value=0.0, value=0.0, format="%.2f")
            storage = st.number_input("Armazenamento por conta / mês (€)", min_value=0.0, value=0.0, format="%.2f")
        with b:
            backups = st.number_input("Backups e monitorização / mês (€)", min_value=0.0, value=0.0, format="%.2f")
            fixed = st.number_input("Outros custos fixos / mês (€)", min_value=0.0, value=0.0, format="%.2f")
        with c:
            support_minutes = st.number_input("Minutos de suporte por conta / mês", min_value=0.0, value=0.0, format="%.1f")
            hourly = st.number_input("Custo de suporte por hora (€)", min_value=0.0, value=0.0, format="%.2f")
    with st.expander("4 · Processamento de pagamentos", expanded=False):
        a, b = st.columns(2)
        with a:
            payment_percent = st.number_input("Comissão percentual de pagamento (%)", min_value=0.0, max_value=100.0, value=0.0, format="%.2f")
        with b:
            payment_fixed = st.number_input("Comissão fixa por cobrança (€)", min_value=0.0, value=0.0, format="%.2f")
        st.caption("Modelo simplificado: uma cobrança por conta pagante e por mês.")
    result = simulate(Scenario(
        paying_accounts=clients, subscription_price_eur_ex_vat=price,
        ai_calls_per_account=calls, input_tokens_per_call=input_tokens,
        output_tokens_per_call=output_tokens,
        input_eur_per_million_tokens=input_rate, output_eur_per_million_tokens=output_rate,
        other_ai_tools_eur_per_account=extras, storage_eur_per_account=storage,
        support_minutes_per_account=support_minutes, support_hourly_eur=hourly,
        payment_percent=payment_percent, payment_fixed_eur_per_account=payment_fixed,
        monthly_hosting_eur=hosting, monthly_backup_monitoring_eur=backups,
        monthly_other_fixed_eur=fixed,
    ))
    st.markdown("### Projeção mensal — valores introduzidos")
    cols = st.columns(4)
    cols[0].metric("Receita sem IVA", _money(result["revenue_eur"]))
    cols[1].metric("Custos totais", _money(result["total_cost_eur"]))
    cols[2].metric("Resultado simplificado", _money(result["operating_result_eur"]))
    cols[3].metric("Custo variável por conta", _money(result["variable_eur_per_account"]))
    with st.expander("Ver decomposição e ponto de equilíbrio"):
        st.write("IA por conta:", _money(result["ai_eur_per_account"]))
        st.write("Suporte por conta:", _money(result["support_eur_per_account"]))
        st.write("Pagamentos por conta:", _money(result["payment_eur_per_account"]))
        st.write("Contribuição por conta:", _money(result["contribution_eur_per_account"]))
        st.write("Custos fixos totais:", _money(result["fixed_eur_total"]))
        threshold = result["break_even_accounts"]
        st.write("Contas necessárias para cobrir os custos incluídos:",
                 str(threshold) if threshold is not None else "Não atingível com esta margem unitária")
    st.warning(
        "SIMULAÇÃO, não rentabilidade comprovada. Campos a zero podem representar custos ainda desconhecidos. "
        "Não inclui automaticamente IVA, impostos sobre resultados, aquisição de clientes, churn, "
        "desenvolvimento inicial nem obrigações jurídicas. Sem segurança e proteção de dados adequadas, "
        "sobretudo para menores, um cenário lucrativo não autoriza lançamento."
    )
