Here’s a clean and well-documented README.md file for your Resume Parser with Job Description Skill Matching application built using React (frontend) and Django (backend), including batch parsing, secure API with secret key, and CORS configuration:

⸻


# 🧠 Resume Parser & Job Description Skill Matcher

A web-based tool that parses resumes (PDFs) and compares them against a job description to compute skill match scores. Built using **React.js** for frontend and **Django Rest Framework** for backend.

---

## 🚀 Features

- ✅ Parse single or multiple resumes (batch mode).
- ✅ Extract skills from resumes using spaCy NLP.
- ✅ Match resume skills with job description keywords.
- ✅ Compute and return similarity scores.
- ✅ Secure API access with secret key.
- ✅ CORS-enabled for frontend-backend integration.

---

## 🛠️ Tech Stack

| Layer       | Technology               |
|-------------|---------------------------|
| Frontend    | React.js                  |
| Backend     | Django Rest Framework     |
| NLP         | spaCy (custom skill matcher) |
| Parsing     | PDFMiner or PyPDF2        |
| Security    | Secret key-based header check |
| Hosting     | Localhost (dev mode)      |

---

## 📦 Installation

### Backend (Django)

1. **Clone the repo & navigate to backend folder**
   ```bash
   git clone <your-repo-url>
   cd backend

	2.	Create virtual environment & activate

python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows


	3.	Install dependencies

pip install -r requirements.txt


	4.	Run migrations

python manage.py migrate


	5.	Run the server

python manage.py runserver



🔐 Default API secret key is defined in .env or settings.py as API_SECRET_KEY = 'your-secret-key'.

⸻

Frontend (React)
	1.	Navigate to frontend folder

cd frontend


	2.	Install dependencies

npm install


	3.	Start the development server

npm start



⸻

🔐 API Security

All requests to /api/parse/ and /api/parse-multiple/ require a secret header:

Header to include:

X-API-SECRET: your-secret-key

Example axios config in ResumeForm.js:

const config = {
  headers: {
    'X-API-SECRET': 'your-secret-key',
    'Content-Type': 'multipart/form-data'
  }
};
await axios.post('http://localhost:8000/api/parse/', formData, config);


⸻

🌐 CORS Configuration (Django)

In settings.py:

INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE

from corsheaders.defaults import default_headers
CORS_ALLOWED_ORIGINS = ["http://localhost:3001"]
CORS_ALLOW_HEADERS = list(default_headers) + ["x-api-secret"]


⸻

📂 Project Structure

/backend
  └── api/
      ├── views.py
      ├── utils.py
      ├── security.py
  └── settings.py

/frontend
  └── src/
      ├── ResumeForm.js
      ├── ResumeForm.css


⸻

📈 Sample Response (Single Resume)

{
  "file_name": "rahul_resume.pdf",
  "resume_skills": ["Python", "Django", "SQL"],
  "jd_skills": ["Django", "React", "SQL"],
  "matched_skills": ["Django", "SQL"],
  "score": 78
}


⸻

🧪 To Test
	•	Upload single or multiple .pdf files
	•	Paste job description in the text box
	•	Click “Parse Resume(s)”
	•	View score & matched skills

⸻

🙌 Credits

Developed by Rahul Chavan
LinkedIn • GitHub

⸻

📜 License

MIT License — free to use, modify, and distribute.

---

Let me know if you'd like this README as a downloadable `.md` file or tailored for deployment (Docker, AWS, etc.).