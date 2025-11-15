📄 Basic Resume Analyzer

- A simple web-based Resume Analyzer built using Python, Flask, spaCy, and docx2txt.
This project extracts text from uploaded resumes, identifies entities, and detects common technical skills.

🚀 Features:
Upload a .docx resume
Extract raw text from the file
Perform Named Entity Recognition (NER) using spaCy
Identify common programming skills
Display extracted text, entities, and skills in a clean UI

🧰 Tech Stack:
Python 3
Flask (backend web framework)
spaCy (en_core_web_sm model for NLP)
HTML/CSS (templates)

🧠 how the project comiles:
User uploads a .docx resume
Application extracts text using docx2txt
spaCy processes the extracted text
Entities (names, dates, orgs, etc.) are identified
Predefined skills are matched against resume text
Output is displayed neatly on the results page
