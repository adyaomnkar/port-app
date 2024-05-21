import streamlit as st

st.set_page_config(
    page_title="Resume",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="auto",
)
st.title("Adya Omnkar Here👋🏻")
st.subheader("AI|ML Freshman")
st.write("Emerging AI & Machine Learning Enthusiast | Pursuing Bachelors inAI & Data Science | Python Learner")
st.sidebar.success("select an option")

paragraph="""
Welcome to my  profile! 😊 As a dedicated individual immersed in the realm of Artificial Intelligence (AI), I am actively pursuing a Bachelor's degree in Artificial Intelligence and Data Science, with a primary focus on machine learning 🧠."""
st.write(paragraph)
st.markdown("---")
para="""
Here are some key aspects that
define my professional journey:

📚 Educational Pursuit: Currently enrolled in a rigorous program for Artificial Intelligence and Data Science, fostering a comprehensive understanding of the field.

💻 Technical Proficiency: Possess strong command over programming languages, particularly C and Python, enabling effective development and implementation of AI solutions.

🚀 Passion for Innovation: Driven by a fervent interest in AI, my goal is to contribute meaningfully to the ever-evolving landscape of technology by leveraging cutting-edge solutions.

🌟 Career Aspiration: Eager to transition into a dynamic career within the AI and Data Science domain, where I can apply my skills and knowledge to address complex challenges and drive innovation. Let's connect and explore the vast opportunities within the exciting world of AI together!

"""
st.write(para)
st.subheader("🏫 Education")
edu="""

->University:CV Raman Global University (CGU), Bhubaneswar
Bachelor of Technology - BTech,Artificial intelligence and data science , Computer and Information Sciences and
Support Services · (April 2023 - April 2027)


->High School:Saraswati Shishu Vidya Mandir,Keonjhargarh"""

st.write(edu)
st.markdown("---")