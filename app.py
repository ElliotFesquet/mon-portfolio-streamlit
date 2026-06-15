import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Portfolio | Mon Nom", page_icon="💼", layout="centered")

# --- BARRE LATÉRALE (Sidebar) ---
with st.sidebar:
    st.image("https://media.licdn.com/dms/image/v2/D4E03AQFIIg1Is6ukEw/profile-displayphoto-crop_800_800/B4EZrbPtOiGoAI-/0/1764614919798?e=1782950400&v=beta&t=q41EXb1QsiBfDb61rrNRw-wcs6eUbwO4me7UEXMuPm8", width=150) # Remplace par ta photo plus tard
    st.markdown("## Elliot Fesquet")
    st.markdown("Analytics engineer")
    st.markdown("Paris, Londres")
    st.markdown("---")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/elliot-fesquet)")
    st.markdown("[GitHub](https://github.com/ElliotFesquet)")

# --- PAGE PRINCIPALE ---
st.title("Mon Portfolio")
st.write("Bienvenue sur mon espace professionnel. Passionné par la donnée, voici les projets sur lesquels j'ai travaillé.")

st.markdown("---")

# Section Projets
st.header("🛠️ Mes Projets")

# Projet 1
with st.expander("Mon CV"):
    st.write("**Description :** Mon CV sur hébergé sur GitHub Pages, présentant mon parcours et mes compétences.")
    st.write("**Technologies :** classique HTML, CSS, GitHub Pages")
    st.markdown("[Voir mon CV](https://elliotfesquet.github.io/cv/index.html)")

# Projet 2
with st.expander("🤖 Projet 2 : Prédiction du prix des logements"):
    st.write("**Description :** Modèle de régression pour estimer les prix de l'immobilier.")
    st.write("**Technologies :** Scikit-Learn, Streamlit")
    st.markdown("[Voir le code source](https://github.com/ElliotFesquet)")

st.markdown("---")

# Section Contact
st.header("✉️ Me contacter")
st.write("Si mon profil vous intéresse, n'hésitez pas à me contacter directement via mes réseaux ou par mail : **test**")