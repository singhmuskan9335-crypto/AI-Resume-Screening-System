def extract_skills(resume_text):

    skill_database = [

        "Python",
        "Java",
        "C++",
        "SQL",
        "MySQL",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "TensorFlow",
        "Scikit-learn",
        "Docker",
        "Git",
        "GitHub",
        "HTML",
        "CSS",
        "JavaScript",
        "Streamlit",
        "FastAPI",
        "AWS",
        "Azure",
        "Linux",
        "MongoDB",
        "LangChain",
        "Hugging Face",
        "LLM",
        "RAG"

    ]

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skill_database:

        if skill.lower() in resume_text:

            found_skills.append(skill)

    return found_skills