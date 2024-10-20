import streamlit as st
from streamlit.delta_generator import DeltaGenerator

def markdown(content) -> DeltaGenerator:
    return st.markdown(content, unsafe_allow_html=True)

def run():
    st.set_page_config(
        page_title="Convertex",
        page_icon="assets/icon.png",
        layout="wide",
        initial_sidebar_state="auto",
    )

    # * STYLES
    markdown(
        """
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
                font-size: 4rem;
                font-weight: bold;
            }
            .header-h2 {
                padding: 1rem 0 1rem 0 !important;
                text-align: center;
                font-family: 'Monospace';
                font-size: 2rem;
                font-weight: bold;
            }

            .body-p{
                padding: 0.75rem 0.75rem 0.75rem 0.75rem;
                margin: 2rem 0 0 0;
                background-color: var(--primary-background-color);
                border-radius: 1rem 1rem 0rem 0rem;
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
                border: 1px white;
            }
            .stFileUploader * {
                margin: 0;
                background-color: var(--primary-background-color);
                color: var(--primary-text-color);
                border: 0 !important;
                border-radius: 0 0 1rem 1rem;
            }
            .stFileUploader p  {
                border-radius: 0 !important;
                font-size: 1.3rem;
                font-weight: bold;
            }
            .stFileUploader label {
                padding: 2rem 0 0 0;
                display: flex;
                justify-content: center;
                border-radius: 0 !important;
            }
            .stFileUploader svg {
                margin: 0rem 1rem 0 0;
            }
            .stFileUploader section {
                display: flex;
                flex-wrap: wrap;
                flex-direction: row !important;
                justify-content: space-between;
                align-content: center;
            }
            .stFileUploader section > div {
                display: flex;
                justify-content: center;
                width: 45%;
            }
            // TODO: Center button
            .stFileUploader button {
                width: 45%;
                background-color: var(--primary-text-color);
                border-radius: 0.5rem;
                color: var(--primary-background-color);
            }
            .stFileUploader button::hover {
                background-color: #555555;
            }
        </style>
        """
    )
    st.divider()

    # * HEADER title
    markdown("""<h1 class="header-h1">CONVERTEX</h1>""")

    # * HEADER subtitle (motto)
    markdown("""<h2 class="header-h2">Fácil. Exacto. Preciso</h2>""")

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
    
if __name__ == "__main__":
    run()