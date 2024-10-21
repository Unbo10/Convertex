import streamlit as st
from main import markdown

def run(styles: str):
    st.set_page_config(
        page_title="Enviado",
        page_icon="assets/icon.png",
        layout="wide"
    )
    markdown(styles)
    markdown("""<h1 class="header-h1">CONVERTEX</h1>""")
    markdown("""<h2 class="header-h2">Enviado exitosamente</h2>""")
    st.write("¡En menos de 12 horas tendrás la transcripción de tu imagen a un archivo .tex en tu bandeja de entrada!")
    load_main_button = st.button("Volver a CONVERTEX")
    if load_main_button:
        st.switch_page("main.py")

if __name__ == "__main__":
    styles: str = """
    <style>
    :root{
        --primary-background-color: #2f3ccf;
        --primary-text-color: #eeeeee;
    }
    .header-h1{
        padding: 2rem 0 0 0 !important;
        font-size: 3.5rem;
        font-weight: bold;
    }
    .header-h1 span {
        width: 0;
        height: 0;
        margin: 0;
        padding: 0;
    }
    .header-h2 {
        padding: 1rem 0 1rem 0 !important;
        font-family: 'Monospace';
        font-size: 2rem;
        font-weight: bold;
    }
    .header-h2 span {
        width: 0 !important;
        height: 0;
        margin: 0;
        padding: 0;
    }
    p {
        font-weight: bold;
    }
    </style>
    """
    run(styles)