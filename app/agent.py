from google.cloud import aiplatform

# Initialize Vertex AI
aiplatform.init(project="genai-agent-apac", location="us-central1")

class SummarizerAgent:
    def __init__(self):
        # Load Gemini model
        self.model = aiplatform.GenerativeModel("gemini-1.0-pro")

    def run(self, text: str) -> str:
        response = self.model.generate_content(f"Summarize this: {text}")
        return response.text