import streamlit as st

# Datos simulados para mostrar (puedes luego automatizarlo)
ip = "15.204.37.30"
pais = "Estados Unidos"
asn = "AS16509 (Amazon.com)"
riesgo_ibm = "🔴 Alto"
detecciones_vt = 11
imagen_url = "https://0x0.st/XXXX.png"  # <-- Aquí va la URL pública de la captura

# Interfaz
st.set_page_config(page_title="Reporte de IP", layout="centered")
st.title("🔍 Reporte de reputación IP")
st.write(f"**IP analizada:** `{ip}`")
st.write(f"**País:** {pais}")
st.write(f"**ASN:** {asn}")
st.write(f"**Detecciones (VirusTotal):** `{detecciones_vt}` motores")
st.write(f"**Riesgo (IBM X-Force):** {riesgo_ibm}")
st.write("📸 **Captura de IBM X-Force:**")
st.image(imagen_url, use_column_width=True)
