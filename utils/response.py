import json
import streamlit as st
import time
import re
# Load profile data
with open("utils/profile.json", "r") as f:
    profile = json.load(f)





# === Intents ===
INTENTS = {
    "about": ["about", "yourself", "who are you", "introduce"],
    "education": ["education", "study", "degree", "college", "university"],
    "skills": ["skills", "technologies", "stack", "tools", "tech stack"],
    "projects": ["projects", "work", "portfolio", "apps", "applications"],
    "experience": ["experience", "career", "job", "internship", "role"]
}

def detect_intent(prompt: str):
    for intent, keywords in INTENTS.items():
        for kw in keywords:
            if re.search(rf"\b{kw}\b", prompt):
                return intent
    return None

# === Response Generator (keeps your preferred 0.1s delay) ===
def response_generator(prompt):
    prompt = prompt.lower()

    # ensure context exists
    if "context" not in st.session_state:
        st.session_state.context = {"awaiting_project_detail": False}

    intent = detect_intent(prompt)

    if intent == "about":
        response = profile.get("about", "No about info.")
        st.session_state.context["awaiting_project_detail"] = False

    elif intent == "education":
        response = profile.get("education", "No education info.")
        st.session_state.context["awaiting_project_detail"] = False

    elif intent == "skills":
        response = ", ".join(profile.get("skills", []))
        st.session_state.context["awaiting_project_detail"] = False

    elif intent == "projects":
        found_project = None
        for name in profile.get("projects", {}).keys():
            if name.lower() in prompt:
                found_project = name
                break

        if found_project:
            response = f"{found_project}: {profile['projects'][found_project]}"
            st.session_state.context["awaiting_project_detail"] = False
        else:
            project_names = "\n".join([f"• {name}" for name in profile.get("projects", {}).keys()])
            response = (
                "🚀 Here are some of my projects:\n"
                f"{project_names}\n\n"
                "👉 Type the **project name** to know more about it!"
            )
            st.session_state.context["awaiting_project_detail"] = True

    elif intent == "experience":
        response = "\n".join([
            f"{e['role']} at {e['company']} ({e['duration']}): {e['description']}"
            for e in profile.get("experience", [])
        ])
        st.session_state.context["awaiting_project_detail"] = False

    # follow-up after project listing
    elif st.session_state.context.get("awaiting_project_detail"):
        found_project = None
        for name in profile.get("projects", {}).keys():
            if name.lower() in prompt:
                found_project = name
                break
        if found_project:
            response = f"{found_project}: {profile['projects'][found_project]}"
            st.session_state.context["awaiting_project_detail"] = False
        else:
            response = "I couldn’t find that project. Please type the exact project name from the list above."

    else:
        response = "🤖 I'm still learning! Try asking about my skills, education, or projects."
        st.session_state.context["awaiting_project_detail"] = False

    # stream with preferred delay
    for word in response.split():
        yield word + " "
        time.sleep(0.1)
