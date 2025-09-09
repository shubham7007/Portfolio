import streamlit as st
from utils.ui import set_animated_background

#calling particle bg function



import streamlit as st
from PIL import Image

# Custom CSS for styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Main container styling */
    .main-container {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        color: white;
    }
    
    /* Animated Hero Section */
    .animated-hero {
        position: relative;
        background: rgba(32, 40, 72, 0.6); /* dark bluish translucent */
        backdrop-filter: blur(10px) saturate(150%); /* frosted glass effect */
        -webkit-backdrop-filter: blur(10px) saturate(150%);
        border: 1px solid rgba(0, 255, 255, 0.6); /* subtle border*/
        min-height: 60vh;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        overflow: hidden;
        margin: 2rem 0;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.1); /* subtle glowing shadow */
    }
    
    .floating-particles {
        position: absolute;
        width: 100%;
        height: 100%;
        overflow: hidden;
    }
    
    .particle {
        position: absolute;
        display: block;
        pointer-events: none;
        width: 6px;
        height: 6px;
        background: rgba(76, 205, 196, 0.6);
        border-radius: 50%;
        animation: float 6s ease-in-out infinite;
    }
    
    .particle:nth-child(1) {
        top: 20%;
        left: 20%;
        animation-delay: 0s;
    }
    
    .particle:nth-child(2) {
        top: 80%;
        left: 80%;
        animation-delay: 2s;
    }
    
    .particle:nth-child(3) {
        top: 40%;
        left: 70%;
        animation-delay: 4s;
    }
    
    .particle:nth-child(4) {
        top: 70%;
        left: 30%;
        animation-delay: 1s;
    }
    
    .particle:nth-child(5) {
        top: 30%;
        left: 50%;
        animation-delay: 3s;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) scale(1); opacity: 0.7; }
        50% { transform: translateY(-20px) scale(1.1); opacity: 1; }
    }
    
    .hero-content {
        text-align: center;
        z-index: 10;
        position: relative;
    }
    
    .profile-container {
        margin-bottom: 2rem;
        position: relative;
    }
        
   
    @keyframes profileFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes glow {
        from { opacity: 0.3; transform: scale(1); }
        to { opacity: 0.6; transform: scale(1.05); }
    }
        
    .title-word {
        display: inline-block;
        animation: titleBounce 1s ease-out;
        animation-fill-mode: both;
    }
    
    .title-word:nth-child(2) {
        animation-delay: 0.3s;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes titleBounce {
        0% { opacity: 0; transform: translateY(50px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .typing-container {
        margin: 1.5rem 0;
    }
    
    .typing-text {
        font-size: 1.3rem;
        color: #b8c6db;
        border-right: 2px solid #4ecdc4;
        padding-right: 5px;
        animation: typing 3s steps(60, end), blink 0.75s step-end infinite;
        white-space: nowrap;
        overflow: hidden;
        display: inline-block;
    }
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink {
        from, to { border-color: transparent; }
        50% { border-color: #4ecdc4; }
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: #95a5a6;
        margin: 1rem 0 2rem;
        animation: fadeInUp 1s ease-out 1s both;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .cta-buttons {
        display: flex;
        gap: 1rem;
        justify-content: center;
        animation: fadeInUp 1s ease-out 1.5s both;
    }
    
    .cta-btn {
        padding: 12px 30px;
        border: none;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .cta-btn.primary {
        background: linear-gradient(45deg, #4ecdc4, #44a08d);
        color: white;
        box-shadow: 0 4px 15px rgba(76, 205, 196, 0.4);
    }
    
    .cta-btn.primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(76, 205, 196, 0.6);
    }
    
    .cta-btn.secondary {
        background: transparent;
        color: #4ecdc4;
        border: 2px solid #4ecdc4;
    }
    
    .cta-btn.secondary:hover {
        background: #4ecdc4;
        color: white;
        transform: translateY(-3px);
    }
    
    /* About Section Styling */
    .about-section {
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        border-radius: 20px;
        margin: 3rem 0;
    }
    
    .section-title {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .gradient-text {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(45deg, #4ecdc4, #ff6b6b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }
    
    .title-underline {
        width: 100px;
        height: 4px;
        background: linear-gradient(45deg, #4ecdc4, #ff6b6b);
        margin: 0 auto;
        border-radius: 2px;
    }
    
    .about-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .about-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        animation-duration: 1s;
        animation-fill-mode: both;
    }
    
    .about-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        background: rgba(255, 255, 255, 0.15);
    }
    
    .card-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
        animation: iconBounce 2s ease-in-out infinite;
    }
    
    @keyframes iconBounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    .about-card h3 {
        color: #4ecdc4;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .about-card p {
        color: #b8c6db;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    .slide-in-left {
        animation-name: slideInLeft;
        animation-delay: 0.2s;
    }
    
    .slide-in-right {
        animation-name: slideInRight;
        animation-delay: 0.4s;
    }
    
    .slide-in-bottom {
        animation-name: slideInBottom;
        animation-delay: 0.6s;
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes slideInBottom {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 2rem 0;
        padding: 1rem;
        border-bottom: 3px solid #4ecdc4;
    }
    
    /* Card styling for sections */
    .info-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Work/Education item styling */
    .timeline-item {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #4ecdc4;
        color: white;
        position: relative;
    }
    
    .timeline-item::before {
        content: "";
        position: absolute;
        left: -8px;
        top: 20px;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background: #4ecdc4;
    }
    
    .item-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #4ecdc4;
        margin-bottom: 0.5rem;
    }
    
    .item-company {
        font-size: 1.1rem;
        color: #b8c6db;
        margin-bottom: 0.5rem;
    }
    
    .item-date {
        font-size: 0.9rem;
        color: #95a5a6;
        margin-bottom: 1rem;
    }
    
    /* Skills styling */
    .skill-tag {
        display: inline-block;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        color: white;
        padding: 0.5rem 1rem;
        margin: 0.25rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
    }
    
    /* Contact info styling */
    .contact-item {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border-left: 3px solid #4ecdc4;
    }
    
    /* Navigation styling */
    .nav-section {
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* Project card styling */
    .project-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .animated-title {
            font-size: 2.5rem;
        }
        
        .cta-buttons {
            flex-direction: column;
            align-items: center;
        }
        
        .about-grid {
            grid-template-columns: 1fr;
        }
        
        .typing-text {
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("""
<div class="nav-section">
    <h2 style="color: white; text-align: center;"> About-me</h2>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.selectbox("Go to:", 
    ["🏠 Home", "🎓 Education", "💼 Work Experience", "🛠️ Skills", "📊 Projects", "📞 Contact"])

if page == "🏠 Home" or page == "👨‍💻 About Me":
    
    # Enhanced Hero Section with animations
    st.markdown("""
    <div class="animated-hero">
        <div class="floating-particles">
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
        </div>
        <div class="hero-content">
                <h1 class="animated-title">
                <span class="title-word">Shubham</span>
                <span class="title-word">Rai</span>
            </h1>
            <div class="typing-container">
                <p class="typing-text">Aspiring Data Scientist/AI/ML Engineer & Ex VFX-TD (Tools Dev Python)</p>
            </div>
            <p class="hero-description">Always ready to take challenges and a good learner</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive About Me Section


    st.markdown("""
    <div style="background-color: #1f2b3a; padding: 1.5rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
         <h2 style="color: #4ecdc4; margin-bottom: 1rem; font-family: 'Segoe UI', sans-serif;"> About Me</h2>
         <p style="font-size: 1.05rem; line-height: 1.7; font-family: 'Segoe UI', sans-serif; color: #ffffff;">
            Passionate about transforming data into actionable insights.Background in VFX and 
            tools development, I am a good learner and always ready to accept challenges
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "🎓 Education":
    st.markdown('<h1 class="section-header">🎓 Education</h1>', unsafe_allow_html=True)
    
    # Education items
    st.markdown("""
    <div class="timeline-item">
        <div class="item-title">Master's in Computer Application</div>
        <div class="item-company">Integral University</div>
        <div class="item-date">2023 - 2025</div>
        <p>Specialized in Machine Learning, Deep Learning, and Statistical Analysis. 
        Completed projects in NLP, Computer Vision, and Predictive Analytics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <div class="item-title">Bachelor's in Computer Application</div>
        <div class="item-company">Integral University</div>
        <div class="item-date">2015 - 2028</div>
        <p>Foundation in programming, software development. 
        Graduated with honors, focusing on Python development.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "💼 Work Experience":
    st.markdown('<h1 class="section-header"> Work Experience</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <div class="item-title">VFX Technical Director - Tools Developer</div>
        <div class="item-company">Technicolor India</div>
        <div class="item-date">2020 - 2023</div>
        <p>• Developed Python tools and scripts for VFX pipeline automation<br>
        • Optimized workflows resulting in 40% time savings<br>
        • Collaborated with artists and supervisors to create technical special effects<br>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <div class="item-title">Data Science </div>
        <p>• Fresher in Datascience, looking for apportunitues in it, always eager to learn about
                new and upcoming techs so i jumped into DataScience And i am a good learner too.<br>

    </div>
    """, unsafe_allow_html=True)

elif page == "🛠️ Skills":
    st.markdown('<h1 class="section-header">🛠️ Technical Skills</h1>', unsafe_allow_html=True)
    
    # Programming Languages
    st.markdown("### 💻 Programming Languages")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <span class="skill-tag">Python</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Data Science & ML
    st.markdown("### 🤖 Data Science & ML")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <span class="skill-tag">Pandas</span>
        <span class="skill-tag">NumPy</span>
        <span class="skill-tag">Scikit-learn</span>        
        <span class="skill-tag">Matplotlib</span>
        <span class="skill-tag">Seaborn</span>
        <span class="skill-tag">Plotly</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Tools & Technologies
    st.markdown("### 🔧 Tools & Technologies")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <span class="skill-tag">Git</span>
        <span class="skill-tag">Docker</span>
        <span class="skill-tag">Jupyter</span>
        <span class="skill-tag">Streamlit</span>
    </div>
    """, unsafe_allow_html=True)

elif page == "📊 Projects":
    st.markdown('<h1 class="section-header">📊 Data Science Projects</h1>', unsafe_allow_html=True)
    
    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #4ecdc4;"> Used Car Price Estimator</h3>
        <p><strong>Tech Stack:</strong> Python, Scikit-learn, Pandas, Streamlit, Github</p>
        <p>Built a machine learning model to predict used car price , 
        Implemented feature engineering, model selection, and hyperparameter tuning. 
        Used Random Forest Regressor for model training,accuracy calculated using r2 score 92% test set.</p>
        <p><strong>Key Results:</strong> Helped to search used cars according to brand,seats, engine and other feautures</p>
    </div>
    """, unsafe_allow_html=True)
    

    

elif page == "📞 Contact":
    st.markdown('<h1 class="section-header"> Get In Touch</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="contact-item">
            <h4>📧 Email</h4>
            <p>raishubham999.sr@outlook.com</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="contact-item">
            <h4>🔗 LinkedIn</h4>
            <p>linkedin.com/in/shubham-rai-a139761a1</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-item">
            <h4>📱 GitHub</h4>
            <p>github.com/shubham7007</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="contact-item">
            <h4>📍 Location</h4>
            <p>Lucknow, INDIA</p>
        </div>
        """, unsafe_allow_html=True)

