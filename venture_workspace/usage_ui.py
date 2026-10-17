"""Private AI spend visibility using only monthly, operation-level aggregates."""
from __future__ import annotations

import csv
import io
import json

import streamlit as st

from venture_workspace.usage_metering import (
    COLUMNS, UsageError, parse_usage, read_aggregates_csv, totals,
)


def render_usage() -> None:
    st.markdown('<div class="v-eyebrow">Venture Factory · Medição</div>', unsafe_allow_html=True)
    st.markdown('<div class="v-title">Consumo de IA</div>', unsafe_allow_html=True)
    st.markdown('<div class="v-desc">Medir o custo das operações de IA antes de definir um preço comercial.</div>',
                unsafe_allow_html=True)
    st.info(
        "Nesta V0.1 os registos são temporários, na sessão do Workspace, e não são guardados "
        "na base de dados. Só podem ser usados resumos agregados — nunca perguntas, respostas, "
        "gravações, nomes de alunos, IDs de utilizador ou documentos escolares."
    )
    st.markdown("#### Operações identificadas no Learning OS")
    st.table([
        {"Operação": "card_generation", "Utilização": "Criar cartões a partir de matéria", "Origem": "OpenRouter"},
        {"Operação": "tutor_feedback", "Utilização": "Avaliar explicações escritas", "Origem": "OpenRouter"},
        {"Operação": "audio_transcription", "Utilização": "Converter áudio em texto", "Origem": "OpenRouter"},
    ])
    st.caption(
        "O código atual efetua pedidos externos para estas operações, mas não há ainda "
        "uma medição persistente de tokens, duração e faturação por operação. "
        "Não se deve considerar o consumo zero."
    )

    if "venture_usage_entries" not in st.session_state:
        st.session_state["venture_usage_entries"] = []
    with st.expander("Adicionar medição agregada", expanded=True):
        st.caption(
            "Preencher a partir do painel do fornecedor, fatura ou uma estimativa identificada. "
            "Valores em EUR, após qualquer conversão cambial necessária."
        )
        with st.form("usage_entry_form"):
            p1, p2, p3 = st.columns(3)
            with p1:
                month = st.text_input("Mês (AAAA-MM)", value="2026-10", max_chars=7)
                app = st.selectbox("Aplicação", ["learning-os", "other"])
                operation = st.selectbox("Operação", [
                    "card_generation", "tutor_feedback", "audio_transcription", "other"
                ])
            with p2:
                provider = st.text_input("Fornecedor", value="openrouter", max_chars=80)
                model = st.text_input("Modelo (identificador técnico)", value="unknown", max_chars=80)
                source = st.selectbox("Origem da informação", [
                    "provider_dashboard", "provider_invoice", "manual_estimate"
                ])
            with p3:
                requests = st.number_input("Chamadas agregadas", min_value=0, max_value=1000000000, step=1)
                input_tokens = st.number_input("Tokens de entrada (total)", min_value=0, max_value=1000000000000, step=1)
                output_tokens = st.number_input("Tokens de saída (total)", min_value=0, max_value=1000000000000, step=1)
            have_cost = st.checkbox("Conheço o custo faturado/estimado em EUR para este conjunto")
            cost = st.number_input("Custo deste conjunto (€)", min_value=0.0, value=0.0, step=0.01, disabled=not have_cost)
            submit = st.form_submit_button("Adicionar à sessão", type="primary")
            if submit:
                raw = dict(month=month, app=app, operation=operation, provider=provider.strip().lower(),
                           model=model.strip().lower(), source_kind=source, requests=requests,
                           input_tokens=input_tokens, output_tokens=output_tokens,
                           cost_eur=str(cost) if have_cost else None)
                try:
                    entry = parse_usage(raw)
                except UsageError as exc:
                    st.error(str(exc))
                else:
                    st.session_state["venture_usage_entries"].append(entry)
                    st.success("Registo agregado adicionado apenas à sessão atual.")

    template = io.StringIO()
    writer = csv.DictWriter(template, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    st.download_button("Descarregar modelo CSV agregado (vazio)", template.getvalue(),
                       file_name="venture-ai-usage-template.csv", mime="text/csv")
    upload = st.file_uploader("Importar CSV agregado — sem dados pessoais (até 128 KB)", type=["csv"])
    if upload is not None and st.button("Validar e importar CSV para a sessão"):
        try:
            entries = read_aggregates_csv(upload.getvalue())
        except UsageError as exc:
            st.error("CSV recusado: " + str(exc))
        else:
            st.session_state["venture_usage_entries"].extend(entries)
            st.success(f"{len(entries)} linhas agregadas aceites. Não foram guardadas no Core.")

    entries = st.session_state["venture_usage_entries"]
    if entries:
        report = totals(entries)
        st.markdown("### Resumo declarado")
        m1, m2, m3 = st.columns(3)
        m1.metric("Pedidos registados", report["requests"])
        m2.metric("Pedidos com custo conhecido", report["requests_with_cost"])
        m3.metric("Custo introduzido (EUR)", report["declared_cost_eur"] + " €")
        if report["any_missing_cost"]:
            st.warning("Existem pedidos sem custo conhecido. O total não representa a despesa completa.")
        st.dataframe(report["by_month_operation"], use_container_width=True, hide_index=True)
        st.caption(
            "Valores declarados pelo operador, não reconciliados com as faturas do fornecedor. "
            "Repetir importações soma os valores e pode duplicar medições."
        )
        st.download_button(
            "Exportar apenas resumos agregados (JSON)",
            json.dumps([item.as_json() for item in entries], ensure_ascii=False, indent=2),
            file_name="venture-ai-usage-aggregated.json", mime="application/json",
        )
        if st.button("Limpar registos desta sessão"):
            st.session_state["venture_usage_entries"] = []
            st.rerun()
    else:
        st.caption("Ainda não há consumos introduzidos. Não existem valores medidos ou faturados aqui.")
