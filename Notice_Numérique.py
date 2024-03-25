import streamlit as st
import pandas as pd
from streamlit_pdf_viewer import pdf_viewer


st.set_page_config(
    page_title='Homepage',
    page_icon='📃',
    layout='wide',
    initial_sidebar_state='auto'
)

st.title('📃 Notice Numérique Doliprane 💊')

st.divider()


tab1,tab2,tab3 = st.tabs(['Fiche info','Résumé des caractéristiques du produit','Notice'])

with tab1:
    pdf_viewer("Fiche-info-DOLIPRANE-1000-mg-comprimé-Base-de-données-publique-des-médicaments.pdf")

with tab2:
     pdf_viewer("Résumé-des-caractéristiques-du-produit-DOLIPRANE-1000-mg-comprimé-Base-de-données-publique-des-médicaments.pdf")

with tab3:
     pdf_viewer("Notice-patient-DOLIPRANE-1000-mg-comprimé-Base-de-données-publique-des-médicaments.pdf")
