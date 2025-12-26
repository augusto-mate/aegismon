import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="AegisMon Demo", page_icon="🛡️")

st.title("🛡️ AegisMon — Security Monitor")
st.write("Demo interativa: escaneamento de políticas e geração de relatórios.")

uploaded = st.file_uploader("Upload JSON de políticas/telemetria", type=["json"])

def fake_anomaly_score(record):
    base = 0.3
    if "error" in record.get("level", "").lower():
        base += 0.4
    if record.get("latency_ms", 0) > 500:
        base += 0.2
    if record.get("source", "") in {"external", "unknown"}:
        base += 0.1
    return min(1.0, base)

def analyze_telemetry(data, th):
    findings = []
    for i, rec in enumerate(data):
        score = fake_anomaly_score(rec)
        if score >= th:
            findings.append({
                "index": i,
                "score": round(score, 3),
                "timestamp": rec.get("timestamp", "n/a"),
                "summary": f"Anomaly detected (level={rec.get('level','n/a')}, latency={rec.get('latency_ms','n/a')}ms)"
            })
    return findings

if uploaded:
    try:
        payload = json.load(uploaded)
        records = payload["records"] if isinstance(payload, dict) else payload
        st.success(f"Carregado {len(records)} registros.")
        findings = analyze_telemetry(records, 0.7)
        st.subheader("Resultados do escaneamento")
        st.dataframe(findings)

        report = {
            "report_id": f"aegismon-{datetime.utcnow().isoformat()}Z",
            "threshold": 0.7,
            "findings": findings,
            "status": "demo"
        }
        st.subheader("Relatório")
        st.code(json.dumps(report, indent=2), language="json")

        st.download_button(
            "Baixar relatório",
            data=json.dumps(report, indent=2),
            file_name="aegismon_report.json",
            mime="application/json"
        )
    except Exception as e:
        st.error(f"Erro ao processar arquivo: {e}")
else:
    st.info("Faça upload de um arquivo JSON para análise.")
