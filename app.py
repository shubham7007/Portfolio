import streamlit as st
from utils.ui import set_animated_background

#page setup 
about_page = st.Page(
    page="views/about_me.py",
    title="about_me",
    icon=":material/account_circle:",
    default=True    #this will be a default page while opening a webapp
)

project_1_page = st.Page(
    page='views/car_price_prediction.py',
    title='Used Car Price Estimation',
    icon=":material/directions_car:",
)

project_2_page = st.Page(
    page = 'views/chatbot.py', 
    title = 'Chat-Bot',
    icon = ':material/chat:',
)

project_3_page = st.Page(
    page = 'views/spam_ham_classification.py',
    title = 'Spam Ham Mail Classifier',
    icon = ':material/shield:',
)

project_4_page = st.Page(
    page='views/CustomerChurnANN.py',
    title='Customer Churn Prediction ANN',
    icon=':material/group:',
)

project_5_page = st.Page(
    page='views/movie_sentiment_analysis_rnn.py',
    title='Movie Sentiment Analysis Simple RNN',
    icon=':material/movie:'
)
#navigation setup 
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page, project_4_page, project_5_page],
    }
)

#run navigation 
pg.run()
