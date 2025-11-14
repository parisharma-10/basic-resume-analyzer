from flask import Flask, render_template, request
import docx2txt
import spacy

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Simple list of common skills
SKILLS = ["python", "java", "c++", "sql", "html", "css", "javascript", "flask", "django", "react"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    if "resume" not in request.files:
        return "No file uploaded!"

    file = request.files["resume"]
    text = docx2txt.process(file)

    doc = nlp(text)

    # Extract entities 
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Extract skills from the resume
    found_skills = []
    lower_text = text.lower()
    for skill in SKILLS:
        if skill in lower_text:
            found_skills.append(skill.capitalize())

    return render_template(
        "result.html",
        text=text,
        entities=entities,
        skills=found_skills
    )

if __name__ == "__main__":
    app.run(debug=True)
    
#pre trained model spacy from the NPL
#Named Entity Recognition (NER)