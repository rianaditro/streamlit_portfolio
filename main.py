import streamlit as st
import time

st.set_page_config(page_title="Rianaditro",
                   layout="centered",
                   menu_items={
                       "Get Help": "https://wa.me/6289669249279?text=Can%20we%20talk%20about%20working%20together?"
                   })


st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        width: 220px !important; # Set the width to your desired value
    }
    button[title="View fullscreen"]{
        visibility: hidden;
    }
                        
    .title {
        text-align: center;
        color: black;
    }
            
    a {
        text-decoration: none;
        color: white;
    }
            
    .timeline {
        list-style: none;
        position: relative;
        padding-left: 40px;
    }

    .timeline:before {
        content: '';
        position: absolute;
        top: 0;
        bottom: 0;
        left: 20px;
        width: 4px;
        background: #ddd;
    }

    .timeline li {
        position: relative;
        margin-bottom: 20px;
    }

    .timeline li:before {
        content: '●';
        position: absolute;
        left: -12px;
        top: 0;
        font-size: 20px;
        color: black;
    }

    .timeline li strong {
        font-weight: bold;
        color: green;
    }
    </style>
            """,
            unsafe_allow_html=True)


with st.sidebar:
    st.image("assets/profile.jpeg", width=200)
    st.html("<h3 class='title'>Rian | Python Developer</h3>")

    st.divider()

    st.write("Feel free to ask me anything!")
    
    st.success("rianaditro@gmail.com")
    st.link_button(label="Contact Me", 
                   url="https://wa.me/6289669249279?text=Can%20we%20talk%20about%20working%20together?",
                   help="Send me a Whatsapp message",
                   type="primary")

    


st.html("<h1>Hi,<br>I'm Rian Adi Saputro</h1>")
st.write("Python Developer specialize in data extraction, processing, analysis, and data mining, transforming raw data into actionable insights. I also work with web-based machine learning, integrating models into apps for smarter, scalable solutions. Always exploring new ways to solve problems with data!")

st.divider()

st.html("<h1 class='title'>My Skills</h1>")

skill1, skill2, skill3, skill4, skill5 = st.columns(5)

with skill1:
    st.image("https://cdn-icons-png.flaticon.com/64/5968/5968350.png")

with skill2:
    st.image("https://cdn-icons-png.flaticon.com/64/5968/5968267.png")

with skill3:
    st.image("assets/streamlit.png", use_column_width=True)

with skill4:
    st.image("assets/scikit.png", use_column_width=True)

with skill5:
    st.image("https://cdn-icons-png.flaticon.com/64/5968/5968292.png")

st.divider()

st.html("<h1 class='title'>My Projects</h1>")

project1, project2, project3 = st.columns(3)

with project1:
    st.image("assets/myprojects/project1.png", use_column_width=True)
    st.html("""
                <h6 class='title'>
                    <a style='color: black;' href='https://www.linkedin.com/posts/rianaditro_datascraping-python-requests-activity-7164387257091575808-RWpc?utm_source=share&utm_medium=member_desktop' target='_blank'>
                        Data Scraping
                        <p>Bypass human verification</p>
                    </a>
                </h6>
                """)

with project2:
    st.image("assets/myprojects/project2.jpg", use_column_width=True)
    st.html("""
                <h6 class='title'>
                    <a style='color: black;' href='https://rianaditro.pythonanywhere.com/catalog' target='_blank'>
                        Flask Web App
                        <p>Clone web app from scraping</p>
                    </a>
                </h6>
                """)


with project3:
    st.image("assets/myprojects/project3.jpg", use_column_width=True)
    st.html("""
                <h6 class='title'>
                    <a style='color: black;' href='https://dashboardreport.streamlit.app/' target='_blank'>
                        Streamlit Web App
                        <p>Server monitoring using automated scraper</p>
                    </a>
                </h6>
                """)

project4, project5, project6 = st.columns(3)

with project4:
    st.image("assets/myprojects/project4.jpg", use_column_width=True)
    st.html("""
                <h6 class='title'>
                    <a style='color: black;' href='https://prediksibabi.streamlit.app/' target='_blank'>
                        Machine Learning Web App
                        <p>Classification using Decision Tree and KNN and web-based model training</p>
                    </a>
                </h6>
                """)

with project5:
    st.image("assets/myprojects/project5.jpg", use_column_width=True)
    st.html("""
                <h6 class='title'>
                    <a style='color: black;' href='https://github.com/rianaditro/invoice_automation/tree/main' target='_blank'>
                        Google Apps Script
                        <p>Automated invoice generation</p>
                    </a>
                </h6>
                """)


with project6:
    st.image("assets/myprojects/project6.png", use_column_width=True)
    st.html("""
                <h6 class='title'>
                    <a style='color: black;' href='https://www.linkedin.com/posts/rianaditro_project-peramalan-kasus-covid-19-di-indonesia-activity-7064940704359186432-nmPB?utm_source=share&utm_medium=member_desktop' target='_blank'>
                        Google Cloud Platform
                        <p>Forecasting Covid-19 using BigQueryML and Looker Studio</p>
                    </a>
                </h6>
                """)


st.divider()

st.html("<h1 class='title'>My Experience</h1>")

st.markdown("""
<ul class='timeline'>
    <li><strong>2024 - Present:</strong> Freelance Python Developer</li>
    <li><strong>2023 - Present:</strong> Member of <a href='https://www.linkedin.com/company/remote-worker-indonesia/' target='_blank'>Remote Worker Indonesia</a></li>
    <li><strong>2022 - 2023:</strong> Data Entry at Ninja Xpress Jepara</li>
    <li><strong>2021 - 2021:</strong> Student at <a href='https://grow.google/intl/id_id/bangkit/?tab=cloud-computing' target='_blank'>Bangkit Academy 2021</a> - Cloud Computing Learning Path</li>
    <li><strong>2020 - 2021:</strong> Student at <a href='https://www.dicoding.com/users/rianadisaputro/academies' target='_blank'>Dicoding Academy</a></li>
    <li><strong>2017 - 2022:</strong> Undergraduate student at Universitas Islam Nahdlatul Ulama Jepara</li>
</ul>
""", unsafe_allow_html=True)

st.divider()

st.html("<h1 class='title'>Find more about me!</h1>")
st.html("<p class='title'>A high rehire rate at Fastwork, rising talent at Upwork, a writer and many more...</p>")

url1, url2, url3, url4, url5 = st.columns(5)

url1.link_button("GitHub", "https://github.com/rianaditro", use_container_width=True, type="primary")
url2.link_button("LinkedIn", "https://www.linkedin.com/in/rianaditro/", use_container_width=True, type="primary")
url3.link_button("Medium", "https://medium.com/@rianaditro", use_container_width=True, type="primary")
url4.link_button("Fastwork", "https://fastwork.id/user/rianaditro", use_container_width=True, type="primary")
url5.link_button("Upwork", "https://www.upwork.com/freelancers/~01ffba4c460505aeab?mp_source=share", use_container_width=True, type="primary")


st.divider()

st.html("<h1 class='title'>Feeling lost?</h1>")
st.html("<p class='title'>Chatbot ready to help</p>")

with st.container():

    prompt = st.chat_input("Ask bot anything......")
    response = """
                I'm sorry, this feature is under development. 
                Feel free to ask me anything via email: rianaditro@gmail.com 
                or via WhatsApp: https://wa.me/6289669249279
            """

    def stream_response():
        for word in response.split(" "):
            yield word + " "
            time.sleep(0.02)

    if prompt:
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            st.write_stream(stream_response)



st.markdown("""
    <style>
    .chatbot-button {
        position: fixed;
        bottom: 40px;
        right: 40px;
        background-color: #3498db;
        color: white;
        padding: 10px 20px;
        border-radius: 50px;
        border: none;
        cursor: pointer;
    }
    </style>
            
    <a href="https://wa.me/6289669249279?text=Can%20we%20talk%20about%20working%20together?">
        <button class="chatbot-button">Chat with me!</button>
    </a>
    """, unsafe_allow_html=True)