import spacy
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util
from io import BytesIO
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_file):
    # Convert InMemoryUploadedFile to BytesIO
    file_data = BytesIO(pdf_file.read())
    return extract_text(file_data)

def extract_skills_spacy(text):
    doc = nlp(text.lower())
    skill_keywords = {
        # Programming Languages
        "java", "python", "javascript", "typescript", "c#", "c++", "go", "ruby", "kotlin", "swift", "php", "scala",

        # Web Development
        "html", "css", "sass", "less", "bootstrap", "tailwind", "react", "angular", "vue", "next.js", "jquery",

        # Backend Frameworks
        "spring", "spring boot", "hibernate", "express", "django", "flask", "fastapi", "laravel", ".net", "node.js",

        # Databases
        "mysql", "postgresql", "oracle", "mongodb", "sqlite", "redis", "cassandra", "mariadb", "firebase",

        # APIs and Protocols
        "rest", "restful", "graphql", "soap", "grpc", "json", "xml", "websockets",

        # DevOps / CI-CD
        "git", "github", "gitlab", "bitbucket", "docker", "kubernetes", "jenkins", "circleci", "travisci", "ansible", "terraform", "prometheus", "grafana",

        # Cloud Platforms
        "aws", "azure", "gcp", "heroku", "digitalocean", "cloudflare", "netlify", "vercel",

        # Testing
        "junit", "mockito", "selenium", "cypress", "jest", "mocha", "chai", "pytest", "unittest", "postman",

        # Tools / Misc
        "linux", "bash", "powershell", "jira", "confluence", "slack", "vs code", "eclipse", "intellij", "pycharm",

        # Concepts & Practices
        "ci/cd", "agile", "scrum", "tdd", "bdd", "oop", "mvc", "microservices", "design patterns", "multithreading", "data structures", "algorithms", "web security", "api security",

        # AI/ML (optional add-on)
        "numpy", "pandas", "scikit-learn", "tensorflow", "keras", "pytorch", "opencv", "spacy"
    }
    found_skills = set()

    for token in doc:
        if token.text.lower() in skill_keywords:
            found_skills.add(token.text.lower())
    return list(found_skills)

def compute_similarity(resume_text, job_desc):
    embeddings = model.encode([resume_text, job_desc])
    score = util.cos_sim(embeddings[0], embeddings[1])
    return round(score.item() * 100, 2)