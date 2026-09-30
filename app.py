import streamlit as st
from urllib.parse import quote

# Actualiza estos nombres aquí si cambian los productos.
PRODUCTOS = ["Jaboncillo", "Payo", "Burro"]
TELEFONO_VISIBLE = "0980065058"
TELEFONO_WHATSAPP = "593980065058"
CORREO = "bisravilesm97@gmail.com"
UBICACION = (
    "Parroquia Pascuales, Guayaquil. Referencia: entrando por la arenera, "
    "antes de llegar al sector San Nicolás, Av. Francisco de Orellana–Pascuales."
)

st.set_page_config(
    page_title="Ladrillos El Solfos | Pascuales",
    page_icon="🧱",
    layout="wide",
)

st.markdown("""
<style>
    .block-container {max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem;}
    .hero {padding: 1.7rem; border-radius: 18px; background: linear-gradient(120deg,#8b3f21,#c76a32); color: white;}
    .hero h1, .hero p {color: white;}
    div[data-testid="stForm"] {border: 1px solid #ead9cd; border-radius: 14px; padding: 1rem;}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="hero"><h1>🧱 Ladrillos El Solfos</h1>'
    '<p>Ladrillos fabricados de arcilla en Pascuales, Guayaquil.</p></div>',
    unsafe_allow_html=True,
)
st.write("")
st.write("Pide información de nuestros ladrillos y solicita una cotización directamente.")

st.subheader("Nuestros productos")
cols = st.columns(3)
for col, producto in zip(cols, PRODUCTOS):
    with col:
        st.markdown(f"### 🧱 {producto}")
        st.write("Venta por unidad. Consulta precio y disponibilidad.")

st.subheader("Solicita tu cotización")
with st.form("pedido_form"):
    cliente = st.text_input("Tu nombre")
    contacto = st.text_input("Tu teléfono de contacto")
    entrega = st.radio("¿Cómo necesitas el pedido?", ["Retiro en fábrica", "Consultar entrega"], horizontal=True)
    st.caption("Indica cuántos ladrillos necesitas de cada tipo.")
    qty_cols = st.columns(3)
    cantidades = {}
    for col, producto in zip(qty_cols, PRODUCTOS):
        with col:
            cantidades[producto] = st.number_input(
                producto, min_value=0, step=1, value=0, key=f"qty_{producto}"
            )
    notas = st.text_area("Notas (opcional)", placeholder="Medidas, fecha, sector u otra consulta")
    enviado = st.form_submit_button("Preparar pedido", type="primary", use_container_width=True)

if enviado:
    seleccion = {nombre: int(cantidad) for nombre, cantidad in cantidades.items() if cantidad > 0}
    if not cliente.strip():
        st.error("Escribe tu nombre para preparar el pedido.")
    elif not seleccion:
        st.error("Indica al menos una cantidad de ladrillos.")
    else:
        lineas = [f"• {nombre}: {cantidad} unidades" for nombre, cantidad in seleccion.items()]
        mensaje = (
            "Hola, quiero cotizar un pedido de Ladrillos El Solfos.\n\n"
            f"Nombre: {cliente.strip()}\n"
            f"Teléfono: {contacto.strip() or 'No indicado'}\n"
            f"Pedido:\n" + "\n".join(lineas) + "\n"
            f"Modalidad: {entrega}\n"
            f"Notas: {notas.strip() or 'Sin notas'}"
        )
        st.success("Pedido listo. Elige cómo enviarlo para confirmar precio y disponibilidad.")
        wa_url = f"https://wa.me/{TELEFONO_WHATSAPP}?text={quote(mensaje)}"
        email_subject = quote("Cotización de ladrillos - El Solfos")
        email_url = f"mailto:{CORREO}?subject={email_subject}&body={quote(mensaje)}"
        send_cols = st.columns(2)
        with send_cols[0]:
            st.link_button("Enviar por WhatsApp", wa_url, use_container_width=True)
        with send_cols[1]:
            st.link_button("Enviar por correo", email_url, use_container_width=True)
        with st.expander("Ver mensaje del pedido"):
            st.code(mensaje, language=None)

st.divider()
left, right = st.columns(2)
with left:
    st.markdown("### 📍 Ubicación")
    st.write(UBICACION)
with right:
    st.markdown("### ☎️ Contacto")
    st.write(f"Teléfono: {TELEFONO_VISIBLE}")
    st.write(f"Correo: {CORREO}")
    st.caption("Los pedidos se confirman directamente; esta versión no guarda datos ni procesa pagos en línea.")

st.markdown("---")
st.caption("Ladrillos El Solfos · Fabricados de arcilla · Pascuales, Guayaquil")
