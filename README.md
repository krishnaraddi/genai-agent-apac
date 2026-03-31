# GenAI Agent APAC

A FastAPI service that uses **Google Cloud Vertex AI Gemini models** for text summarization.  
Deployed on **Cloud Run** with CI/CD via **Cloud Build**.

---

## 🚀 Features
- FastAPI endpoint `/summarize` for text summarization
- Vertex AI Gemini (`gemini-1.0-pro`) integration
- Dockerized for Cloud Run deployment
- Requirements pinned for reproducibility
- `.gitignore` and `.dockerignore` included to keep repo clean

---

## 📦 Requirements
`requirements.txt` includes:
fastapi0.110.0 
uvicorn0.29.0 
google-cloud-aiplatform1.143.0 
pytest8.1.1
