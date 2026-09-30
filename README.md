# Ladrillos El Solfos — cotizaciones web

Aplicación en Python y Streamlit para mostrar ladrillos de arcilla y preparar solicitudes de cotización por WhatsApp o correo.

## Ejecutar en tu computadora

1. Instala Python 3.10 o superior.
2. En una terminal, entra a esta carpeta y ejecuta:

   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

## Publicar en Streamlit Community Cloud

1. Sube los archivos de esta carpeta a un repositorio de GitHub.
2. En Streamlit Community Cloud, crea una app nueva y selecciona ese repositorio, la rama principal y `app.py`.
3. Pulsa **Deploy**.

## Editar el catálogo y los contactos

En `app.py`, busca `PRODUCTOS`, `TELEFONO_VISIBLE`, `TELEFONO_WHATSAPP`, `CORREO` y `UBICACION`.

## Alcance actual

- Catálogo de Jaboncillo, Payo y Burro.
- Imagen ilustrativa de ladrillos de arcilla en una obra (`obra_ladrillos.png`); no es una fotografía exacta del producto fabricado.
- Formulario para cantidades, datos de contacto, modalidad y notas.
- Prepara un mensaje para que el comprador lo envíe por WhatsApp o correo.
- No fija precios porque no fueron indicados; tampoco procesa pagos ni almacena pedidos.
