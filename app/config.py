import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
		GEMINI_API_KEY = os.get_env("GEMINI_API_KEY")
		QDRANT_API_KEY = os.get_env("QDRANT_API_KEY")
		QDRANT_URL = os.get_env("QDRANT_CLUSTER_ENDPOINT")
		QDRANT_COLLECTION = "enterprise_rag"

		GROQ_API_KEY = os.get_env("GROQ_API_KEY")
		GROQ_MODEL="llama-3.3-70b-versatile"
		# GROQ_FALLBACK_API_KEY= os.get_env("GEMINI_API_KEY")

settings = Settings()