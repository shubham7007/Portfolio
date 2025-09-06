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
    page='views/sales_dashboard.py',
    title='Sales Dashboard',
    icon=":material/smart_toy:",
)

project_2_page = st.Page(
    page = 'views/chatbot.py', 
    title = 'Chat',
    icon = ':material/chat:',
)

project_3_page = st.Page(
    page ='views/jscheck.py',
    title = 'jsCheck',
    icon = ':material/smart_toy:'
)
#navigation setup 
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
    }
)

#run navigation 
pg.run()
