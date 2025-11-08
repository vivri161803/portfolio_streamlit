import streamlit as st


def main():
    """
    Funzione principale per costruire l'app Streamlit.
    Utilizza una barra laterale per la navigazione tra le sezioni.
    """

    # --- CONFIGURAZIONE DELLA PAGINA ---
    st.set_page_config(
        page_title="Carlo Bianchi | Portfolio",
        page_icon="🐜",
        layout="wide",
        initial_sidebar_state="expanded",

        # --- (MODIFICA) TEMA COLORI INTERFACCIA ---
        # Qui puoi definire i colori principali dell'app.
        # RIMOSSO il dizionario 'theme' che causava l'errore.
    )

    # --- (MODIFICA) CSS GLOBALE PER "ZOOM" E COLORE TEMA ---
    # Iniettiamo CSS per
    # 1. Applicare il colore tema ai titoli
    # 2. Rimosso lo zoom globale per gestirlo in modo specifico
    st.markdown("""
        <style>
        /* (GOAL 4) Applica il colore tema ai titoli */
        h1, h2, h3, h4, h5, h6 {
            color: #c41e3a;
        }

        /* Rimosso: html { font-size: 105%; } */

        </style>
        """, unsafe_allow_html=True)

    # --- NAVIGAZIONE SIDEBAR ---
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", [
        "Home",
        "About Me",
        "Skills & Projects",
        "Other Experience",
        "Contact"
    ])

    # --- ROUTING DELLE PAGINE ---
    if selection == "Home":
        show_home()
    elif selection == "About Me":
        show_about_me()
    elif selection == "Skills & Projects":
        show_skills_projects()
    elif selection == "Other Experience":
        show_experience()
    elif selection == "Contact":
        show_contact()


# --- DEFINIZIONI DELLE PAGINE ---

def show_home():
    """Renderizza la pagina 'Home' con layout professionale,
       contenuto centrato e stili personalizzati.
    """

    # --- CSS PERSONALIZZATO PER LA HOME ---
    st.markdown("""
        <style>
        /* (GOAL 2) Contenitore principale per centrare tutto */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center; /* Centra tutto orizzontalmente */
            text-align: center; /* Centra il testo di default */
        }

        /* (GOAL 3) Testo del paragrafo più grande e leggibile */
        .main-text {
            font-size: 1.15rem; /* Più grande del default (1rem) */
            line-height: 1.6;
            max-width: 720px; /* Mantiene il testo leggibile */
            text-align: left; /* Allinea a sinistra per leggibilità */
            margin-top: 1rem;
            margin-bottom: 1rem;
        }

        /* Contenitore per i pulsanti (per tenerli affiancati) */
        .button-container {
            display: flex;
            flex-direction: row;
            justify-content: center;
            gap: 1rem; /* Spazio tra i pulsanti */
            margin-top: 1rem;
        }

        /* Modifica del colore della st.info box (rimosso centraggio) */
        [data-testid="stInfo"] {
            background-color: #F0F4F8; /* Un grigio-blu molto chiaro */
            color: #262730; /* Testo scuro */
            border-left: 5px solid #90A4AE; /* Bordo grigio-blu */
            max-width: 300px; /* Larghezza massima UGUALE all'immagine */
            text-align: center;
            margin-top: 1rem; /* Aggiunto spazio sopra */
        }

        /* Cambia anche il colore dell'icona (che è un SVG) */
        [data-testid="stInfo"] svg {
            fill: #262730; /* Colore dell'icona */
        }
        </style>
        """, unsafe_allow_html=True)

    # (GOAL 1) LAYOUT A COLONNA SINGOLA
    # Rimosse st.columns([1, 2])

    # Applichiamo il nostro stile CSS "main-container"
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # --- IMMAGINE DEL PROFILO ---
    placeholder_url = "img.png"

    col1, col2 = st.columns([0.5,0.5],
                            # border=True,
                            vertical_alignment="center"
                            )
    with col1:
        st.image(
            placeholder_url,
            # width=600,  # Larghezza fissa per permettere il centraggio
            # caption="Carlo Bianchi"
        )
    with col2:
        st.title("Carlo Bianchi 🐜")
        st.subheader("Data Science & AI Master's Student 💾")
        st.subheader("Aspiring NLP & LLM Researcher 🧠")

        st.markdown("""
                <div class="main-text">
                Hi and welcome. I'm Carlo, a Data Science & AI Master's student at the University of Florence. 
                My mission is to turn my strong curiosity and research skills into a career in academic 
                and applied research. 
                <br><br>
                I explore the intersections between human communication and artificial intelligence, 
                with a specific focus on Natural Language Processing (NLP), Large Language Models (LLM), 
                and Explainable AI (XAI).
                </div>
            """, unsafe_allow_html=True)
    st.markdown("---")

    # --- LINK AI SOCIAL ---
    # (GOAL 1 & 2) Contenitore per pulsanti centrati
    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    # Colonne per allineare i pulsanti dei link
    link_col1, link_col2 = st.columns(2)

    with link_col1:
        st.link_button(
            "🔗 LinkedIn",
            "https://www.linkedin.com/in/carlo-bianchi-b6016b390/",
            use_container_width=True
        )

    with link_col2:
        st.link_button(
            "🐙 GitHub",
            "https://github.com/vivri161803",
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)  # Chiusura button-container
    st.markdown('</div>', unsafe_allow_html=True)  # Chiusura main-container


def show_about_me():
    """Renderizza la pagina 'About Me'."""
    st.title("About Me: My Journey 🚀")
    st.header("From Florence to Data Science 🕸️")
    st.markdown("---")

    st.subheader("The Foundations")
    st.markdown("""
        I am Carlo Bianchi, born and raised in Florence. My background is deeply rooted in analytical and structured thinking. 

        * **Liceo Classico Galileo:** Graduated with 95/100.
        * **Bachelor's in Management Engineering (University of Florence):** Graduated on time with 100/110.
    """)

    st.subheader("The Pivot: AI and Language 👅")
    st.markdown("""
        This solid managerial and engineering foundation gave me the tools to pursue my true passion: Artificial Intelligence. 
        I am currently a **Master's student in Data Science & AI**, where I am delving into topics like Deep Learning, 
        Generative AI, and NLP.
    """)

    st.subheader("The Goal (The 'Desire')")
    st.markdown("""
        My "desire" is to become a researcher. My "dream" is to actively contribute to a field that is shaping our future. 
        I am particularly fascinated by the challenge of making language models not only powerful but also transparent 
        and reliable, which is reflected in my planned thesis topic:

        **"Explainable AI and Automated Fact Checking for LLMs"**
    """)


def show_skills_projects():
    """Renderizza la pagina 'Skills & Projects'."""
    st.title("Skills & Projects 💻")
    st.header("What I Do (and What I'm Building)")
    st.markdown("---")

    st.subheader("Focus Areas & Research Interests 🔎")
    st.markdown("""
        * Deep Learning and Generative AI
        * Natural Language Processing (NLP)
        * Explainable AI (XAI) & Fact Checking applied to LLMs
    """)

    st.markdown('---')
    st.subheader("Technical & Soft Skills 💪")
    # Usa le colonne per organizzare visivamente le competenze
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            "**Technical Skills**\n"
            "* Python (Data Science, Deep-Learning)\n"
            "* PyTorch, Tensorflow, SQL, Java\n"
            "* Strong foundations in math \n"
            "* Bachelor degree in System Engineering"
        )
    with col2:
        st.markdown(
            "**Soft Skills**\n"
            "* Independent Research & Curiosity\n"
            "* Time Management\n"
            "* Team Working\n"
            "* Academic Writing"
        )
    with col3:
        st.markdown(
            "**Spoken Languages**\n"
            "* Italian (Mother tongue)\n"
            "* English (Proficient)\n"
            "* French (Intermediate)"
        )

    st.markdown("---")

    st.subheader("Projects (From my GitHub) 🚧")
    st.markdown("I believe in 'hands-on' learning. Here are some of the repositories I'm working on. Check out my GitHub account for the latest repos.")

    # Definisci i tuoi progetti qui
    projects = [
        {
            "name": "LLM from Scratch",
            "url": "https://github.com/vivri161803/LLM_From_Scratch",
            "desc": "Practical implementation of the 'Build a Large Language Model (From Scratch)' book, by Sebastian Raschka"
        },
        {
            "name": "Hands-on Machine Learning",
            "url": "https://github.com/vivri161803/Generative-AI-Studies",
            "desc": "A collection of studies, notebooks, and experiments in Machine Learning/Deep Learning."
        }
    ]

    # Itera sui progetti e mostrali
    for project in projects:
        st.markdown(f"**[{project['name']}]({project['url']})**")
        st.write(project['desc'])


def show_experience():
    """Renderizza la pagina 'Other Experience'."""
    st.title("Other Experience 🌊")
    st.header("Beyond Academics: Experience & Volunteering ")
    st.markdown("---")
    # Usa st.expander per rendere la sezione interattiva e pulita
    with st.expander("**Volunteering (Current) - Misericordia di Prato**"):
        st.markdown("""
            * Earned First Aid and AED certification (Proficient in CPR, emergency response, patient assessment).
            * This role continually develops my teamwork, communication, and resilience-under-pressure skills.
        """)

    with st.expander("**Event & Logistics Management - Fiorentina FC & Pitti Uomo**"):
        st.markdown("""
            * **Fiorentina FC:** Managed hospitality services for VIP guests, ensuring exceptional customer satisfaction and coordinating event logistics.
            * **Pitti Uomo:** Managed Customer Experience, event logistics, and human resources working at the event.
        """)

    with st.expander("**Customer Service (Cashier) - CoopFI**"):
        st.markdown("""
            * Managed cash transactions efficiently, ensuring accuracy.
            * Assisted customers with inquiries and processed returns, enhancing service satisfaction.
            * Collaborated with team members to optimize store operations.
        """)


def show_contact():
    """Renderizza la pagina 'Contact'."""
    st.title("Let's Connect ☎️")
    st.markdown("---")

    st.markdown("""
        Do you share my passion for computational linguistics or generative AI? Are you working 
        on projects in the NLP/LLM field or looking for a motivated profile for research opportunities?

        I would love to connect.
    """)

    st.markdown("---")

    # Usa icone emoji per i link
    st.markdown(f"""
        ### **Email** 📧
        `bianchicarlo2002@icloud.com`

        ### **LinkedIn** 🔗
        [linkedin.com/in/carlo-bianchi-b6016b390](https://www.linkedin.com/in/carlo-bianchi-b6016b390/)

        ### **GitHub**  🐙 
        [github.com/vivri161803](https://github.com/vivri161803)
    """)


# --- ESECUZIONE DELL'APP ---
if __name__ == "__main__":
    main()