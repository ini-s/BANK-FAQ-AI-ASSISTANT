This Python script creates a simple Bank FAQ AI Assistant using the Azure OpenAI Service. It loads Frequently Asked Questions (FAQs) from a local text file and uses an LLM (Language Model) to answer user questions based only on the provided FAQ context.

🚀 Bank FAQ AI Assistant README
📝 Overview

This script implements a command-line interface (CLI) chat assistant that uses the Azure OpenAI service to answer banking-related questions. The assistant is designed for Retrieval Augmented Generation (RAG), meaning it only uses the content of the local file, bank_faq.txt, as its knowledge base. If a user asks a question not covered in the FAQ content, the assistant will direct them to customer care.

⚙️ Prerequisites
Python: Python 3.x must be installed.

Dependencies: The required Python libraries are openai and python-dotenv.

Azure OpenAI Service: You need an active Azure OpenAI Service instance, an API Key, and an Endpoint.

🛠️ SetupInstall Dependencies:Bashpip install openai python-dotenv

Create Environment File:Create a file named .env in the same directory as the script to store your Azure credentials:Ini, TOML# .env file
API_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT_HERE"
API_KEY="YOUR_AZURE_OPENAI_API_KEY_HERE"

Replace the placeholders with your actual values.Create FAQ Data File:Create a file named bank_faq.txt in the same directory. This file will contain the knowledge base (the bank's FAQs).Example bank_faq.txt content:Plaintextq: How do I open a new account?
a: You can open a new account online through our website or by visiting any branch location.

q: What are your working hours?
a: Our branches are open Monday to Friday, 9 AM to 4 PM. Online banking is available 24/7.

q: How can I reset my password?
a: You can reset your password using the "Forgot Password" link on the login page of our online portal.

(Ensure your data is structured clearly for the model to understand.)▶️ How to RunSave the provided code as a Python file (e.g., faq_assistant.py).Run the script from your terminal:Bashpython faq_assistant.py
The assistant will start, and you can begin typing your questions.Type q or quit to exit the assistant.🔬 
