import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="genai-agent-apac", location="us-central1")

class SummarizerAgent:
    def __init__(self):
        self.model = GenerativeModel("gemini-2.5-flash")

    def run(self, text: str) -> str:
        response = self.model.generate_content(f"Summarize this: {text}")
        return response.text