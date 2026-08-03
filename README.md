# 🤖 AI Resume Screening & Candidate Ranking System

An AI-powered Resume Screening System that helps recruiters automatically analyze resumes, calculate ATS scores, compare resumes with job descriptions, rank candidates, and generate professional reports.

---

## 📌 Features

- 📄 Resume Parsing (PDF)
- 🎯 ATS Score Calculation
- 🤖 AI Semantic Matching
- 🧠 Skill Extraction
- ❌ Missing Skill Detection
- 💡 AI Suggestions
- 🏅 Resume Rating
- 👤 Candidate Summary
- 📊 Candidate Ranking
- 📁 Export Candidate Ranking to Excel
- 📄 Generate PDF Report
- 🗄 SQLite Database Integration
- 🔍 Search Candidate
- ⭐ Filter Candidates by Rating
- 📈 Recruiter Dashboard
- 🗑 Delete Candidate
- 🎨 Professional Streamlit User Interface

---

## 🛠 Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- Scikit-learn
- Sentence Transformers
- PyMuPDF
- ReportLab
- OpenPyXL

---

## 📂 Project Structure

```
AI_Resume_Screening/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── style.css
│
├── components/
│   ├── analysis.py
│   ├── charts.py
│   └── dashboard.py
│
├── database/
│   ├── database.py
│   └── candidates.db
│
├── utils/
│   ├── ats_score.py
│   ├── semantic_match.py
│   ├── pdf_reader.py
│   ├── skill_extractor.py
│   ├── report_generator.py
│   ├── excel_export.py
│   └── ...
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screening.git
```

### Move into the Project Folder

```bash
cd AI-Resume-Screening
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📊 Application Modules

- Home
- Resume Analysis
- Candidate Ranking
- Reports
- About

---

## 📈 Future Improvements

- Authentication System
- Recruiter Login
- Resume Recommendation
- Email Notifications
- Cloud Database Integration
- AI Interview Question Generation

---

## 👨‍💻 Developed By

**Himanshu Singh**

B.Tech CSE (Artificial Intelligence & Machine Learning)

---

## 📜 License

This project is developed for educational and portfolio purposes.