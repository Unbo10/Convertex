import re

import streamlit as st
from streamlit.delta_generator import DeltaGenerator

def markdown(content) -> DeltaGenerator:
    return st.markdown(content, unsafe_allow_html=True)

def retrieve_styles() -> str:
    return styles

@st.dialog("Regístrate")
def open_registration() -> None:
    with st.form(key="body_form"):
        email_input = st.text_input(label="Email", value="", autocomplete="email")
        st.write("No recibirás correos de Convertex más allá de la transcripción de tus documentos a .tex")
        submit_button = st.form_submit_button(label="Enviar")
        # * Apparently buttons return True if they have been pressed.
        if submit_button:
            # * Same with input but this one returns a str instead.
            submit_registration(email_input)

def submit_registration(email: str) -> None:
    valid_email: bool = validate_email(email)
    if valid_email:
        st.switch_page("pages/submitted_succesfully.py")
    else:
        st.error(body="Dirección de correo electrónico inválida")


def validate_email(email: str) -> bool:
    # * This expression means: from start to end of the string, it must contain
    # * any letters or numbers, and a few signs (multiple times if it's the
    # * case), followed by an at symbol, any letters, numbers, dots or dashes
    # * a dot, and a domain at last containing at least two letters.
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def run(styles: str):
    st.set_page_config(
        page_title="Convertex",
        page_icon="assets/icon.png",
        layout="wide",
        initial_sidebar_state="auto",
    )

    # * STYLES
    markdown(styles)

    st.divider()

    # * HEADER title
    markdown("""<h1 class="header-h1">CONVERTEX</h1>""")

    # * HEADER subtitle (motto)
    markdown("""<h2 class="header-h2">Fácil. Exacto. Preciso.</h2>""")

    # * BODY text (description)
    markdown(
        """
        <div class="container">
            <p class="body-p">
                Sube hasta 25 MB en cualquier formato de imagen (preferiblemente <code>.png</code> o <code>.jpg</code>) de tus notas matemáticas y nosotros nos encargaremos de <b>transcribirlas a Latex</b> en menos de 12 horas.
            </p>
        </div>
        """
    )
    st.file_uploader(label=":arrow_down_small: Sube tus imágenes :arrow_down_small:", type=['png', 'jpg', 'tiff'], accept_multiple_files=True)
    columns = st.columns(3)
    center_column = columns[0]
    if center_column.button(label="Convertir a .tex", key="body_submit"):
        open_registration()

styles: str = """
<style>
    :root{
        --primary-background-color: #2f3ccf;
        --primary-text-color: #eeeeee;
    }

    * {
        margin: 0;
        padding: 0;
        gap: 0 !important;
    }

    b{
        font-weight: 700;
    }

    .header-h1{
        padding: 2rem 0 0 0 !important;
        text-align: center;
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
        text-align: -webkit-center;
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

    .body-p{
        padding: 0.75rem 0.75rem 0.75rem 0.75rem;
        margin: 2rem 0 0 0;
        background-color: var(--primary-background-color);
        border-radius: 1rem;
        color: var(--primary-text-color);
        text-align: center;
        font-size: 1rem;
        font-weight: 500;
    }
    .icon {
        width: 1rem;
        height: 1rem;
        margin-right: 0.3rem;
        vertical-align: middle;
    }
    code {
        background-color: var(--primary-text-color);
    }
    .stFileUploader {
        padding: 2rem 0 0 0;
    }
    .stFileUploader * {
        margin: 0;
    }
    .stFileUploader label p {
        border-radius: 0 !important;
        font-size: 1.3rem;
        font-weight: bold;
    }
    .stFileUploader label {
        justify-content: center;
    }
    .stFileUploader section {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row !important;
        align-content: space-around;
        justify-content: space-around;
        margin: 0 0 2rem 0;
    }
    .stFileUploaderFileData {
        justify-content: space-around;
    }
    .stPopover {
        display: flex;
        justify-content: center;
    }
"""

if __name__ == "__main__":
    run(retrieve_styles())