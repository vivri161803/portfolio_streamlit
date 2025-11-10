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
    )

    # --- CSS GLOBALE PER COLORE TEMA ---
    st.markdown("""
        <style>
        /* Applica il colore tema ai titoli */
        h1, h2, h3, h4, h5, h6 {
            color: #c41e3a;
        }
        </style>
        """, unsafe_allow_html=True)

    # --- NAVIGAZIONE SIDEBAR ---
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", [
        "Home",
        "About Me",
        "Skills & Projects",
        "Other Experience",
        "Books & Resources",  # <-- NUOVA PAGINA AGGIUNTA QUI
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
    elif selection == "Books & Resources":  # <-- ROUTING PER LA NUOVA PAGINA
        show_books_resources()
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
        /* Contenitore principale per centrare tutto */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center; /* Centra tutto orizzontalmente */
            text-align: center; /* Centra il testo di default */
        }

        /* Testo del paragrafo più grande e leggibile */
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

        /* Modifica del colore della st.info box */
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

    # Applichiamo il nostro stile CSS "main-container"
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # --- IMMAGINE DEL PROFILO E TITOLI ---
    placeholder_url = "img.png"  # Assicurati che questo file sia nella cartella

    col1, col2 = st.columns([0.5, 0.5], vertical_alignment="center")

    with col1:
        try:
            st.image(
                placeholder_url,
                # width=600, # Rimosso per lasciare che Streamlit gestisca la larghezza
            )
        except Exception as e:
            st.error(
                f"Errore nel caricamento dell'immagine 'img.png'. Assicurati che il file sia nella cartella corretta. Dettagli: {e}")

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
    st.markdown('<div class="button-container">', unsafe_allow_html=True)

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
    st.markdown(
        "I believe in 'hands-on' learning. Here are some of the repositories I'm working on. Check out my GitHub account for the latest repos.")

    projects = [
        {
            "name": "LLM from Scratch",
            "url": "https://github.com/vivri161803/LLM_From_Scratch",
            "desc": "Practical implementation of the 'Build a Large Language Model (From Scratch)' book, by Sebastian Raschka"
        },
        {
            "name": "Hands-on Machine Learning",
            "url": "https.github.com/vivri161803/Generative-AI-Studies",
            "desc": "A collection of studies, notebooks, and experiments in Machine Learning/Deep Learning."
        },
        {
            "name": "UNet Architecture - Hands-On",
            "url": "https://github.com/vivri161803/UNet",
            "desc": "Hands-on experience on a widely used architecture for medical image analysis"
        }
    ]

    for project in projects:
        st.markdown(f"**[{project['name']}]({project['url']})**")
        st.write(project['desc'])


def show_experience():
    """Renderizza la pagina 'Other Experience'."""
    st.title("Other Experience 🌊")
    st.header("Beyond Academics: Experience & Volunteering ")
    st.markdown("---")

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


# --- NUOVA FUNZIONE PER LA PAGINA LIBRI E RISORSE ---
def show_books_resources():
    """Renderizza la pagina 'Books & Resources'."""
    st.title("Books & Resources 📚")
    st.header("What I'm Reading and Watching")
    st.markdown("---")
    st.markdown(
        "Here's a curated list of the content that is shaping my learning and research. Feel free to reach out if you have recommendations!")

    # Usiamo st.tabs per organizzare i contenuti
    tab_books, tab_blogs, tab_videos = st.tabs(["📚 Books", "📰 Blogs & Articles", "📺 Videos & Courses"])

    with tab_books:
        st.subheader("Books")
        st.markdown("""
            * **Build a Large Language Model (From Scratch)** by Sebastian Raschka
                * *Description:* A hands-on guide that I'm actively using for my 'LLM from Scratch' project. In-depth and practical.
            * **Deep Learning** by Ian Goodfellow, Yoshua Bengio, and Aaron Courville
                * *Description:* The foundational textbook for Deep Learning. A must-read for understanding the theory.
            * **Speech and Language Processing** by Dan Jurafsky and James H. Martin
                * *Description:* The classic textbook for NLP. I consult it regularly for core concepts.
            * **Storytelling with Data: A Data Visualization Guide for Business Professionals - Knaflic**
                * *Description:* Wonderful introduction to state of the art techniques for data visualization
            * **An Introduction to Statistical Learning: with Applications in Python - James et al.**
                * *Description:* An Introduction to Statistical Learning provides an accessible overview of the field. 
        """)
        # Puoi aggiungere altri libri qui, seguendo lo stesso formato
        # st.markdown("""
        # * **[Another Book Title]**
        #     * *Description:* [Your notes here]
        # """)

    with tab_blogs:
        st.subheader("Blogs & Articles")
        st.markdown("""
            * **[Sebastian Raschka's Blog](https://sebastianraschka.com/)**
                * *Why I read it:* Incredibly clear explanations on AI, ML, and LLMs, often diving deep into code.
            * **[Jay Alammar's Blog (e.g., The Illustrated Transformer)](https://jalammar.github.io/)**
                * *Why I read it:* Famous for visual and intuitive explanations of complex models like the Transformer.
            * **[distill.pub](https://distill.pub/)**
                * *Why I read it:* High-quality, interactive articles on machine learning research. A benchmark for clarity.
        """)
        # Puoi aggiungere altri blog qui
        # st.markdown("""
        # * **[Blog/Article Name](URL)**
        #     * *Why I read it:* [Your notes here]
        # """)

    with tab_videos:
        st.subheader("Videos & Courses")
        st.markdown("""
            * **[Stanford CS224N: NLP with Deep Learning](https://www.youtube.com/playlist?list=PLoROMvodv4rOSHNKYZoflsYbdB5OylAUW)**
                * *Source:* Stanford University (YouTube)
                * *Why I watch it:* A comprehensive university-level course on modern NLP.
            * **[3Blue1Brown (Deep Learning Series)](https://www.3blue1brown.com/topics/neural-networks)**
                * *Source:* YouTube
                * *Why I watch it:* Unbeatable for building a deep, visual intuition for the math behind neural networks.
            * **[DL Projects](https://www.youtube.com/watch?v=5avSMc79V-w&list=PL93LW34iMK8Qlh31UKxoo50r_OMwwj1zG&pp=gAQB)**
                * *Source:* Various
                * *Why I watch it:* Hands-on lectures.
            * **[Neural Networks: Zero to Hero](https://www.youtube.com/@AndrejKarpathy)**
                * *Source:* Andrej Karpathy
                * *Why I watch it:* Hands-on lectures.
            * **[NLP](https://www.youtube.com/watch?v=u1_qMdb0kYU&list=PL1v8zpldgH3pQwRz1FORZdChMaNZaR3pu)**
                * *Source:* Yannic Kilcher
                * *Why I watch it:* Review of hot articles in a clear and concise way.           
        """)
        # Puoi aggiungere altri video qui
        # st.markdown("""
        # * **[Course/Video Name](URL)**
        #     * *Source:* [Platform/Creator]
        #     * *Why I watch it:* [Your notes here]
        # """)


# --- FINE NUOVA FUNZIONE ---

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

    st.markdown(f"""
        ### **Email** 📧
        `bianchicarlo2002@icloud.com`

        ### **LinkedIn** 🔗
        [linkedin.com/in/carlo-bianchi-b6016b390](https.www.linkedin.com/in/carlo-bianchi-b6016b390/)

        ### **GitHub** 🐙 
        [github.com/vivri161803](https.github.com/vivri161803)
    """)


# --- ESECUZIONE DELL'APP ---
if __name__ == "__main__":
    main()