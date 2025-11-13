## 🚀 AI Banking Assistant

### 📝 Overview

This Python script is a command-line chat assistant built on the **Azure OpenAI Service**. It acts as a comprehensive **Retrieval Augmented Generation (RAG)** system by merging and utilizing content from multiple local knowledge files: **FAQs, general bank policies, and loan policies.**

The assistant's primary goal is to provide accurate, banking-related answers strictly based on the provided local data.

-----

### ✨ Key Features

  * **Multi-Source Knowledge Base:** Consolidates information from `faq.txt`, `bank_policy.txt`, and `loan_policy.txt`.
  * **Persistent Merged File:** Creates and uses a `merged_bank_files.txt` to avoid reprocessing input files on every run.
  * **Enhanced System Prompt:** Explicitly instructs the LLM to use the entire context for comprehensive answers and to reject non-banking-related queries.
  * **Customer Care Fallback:** Directs users to customer care if the specific banking-related answer is not found in the combined context.

-----

### ⚙️ Prerequisites

  * **Python:** Python 3.x must be installed.
  * **Dependencies:** The required Python libraries are `openai` and `python-dotenv`.
  * **Azure OpenAI Service:** You need an active Azure OpenAI Service instance, including an **API Key**, **Endpoint**, and a deployed chat model (like `gpt-4o-mini`).

-----

Here is the brief rewrite of the "How to Run" section, focusing on clear steps:

-----

### ▶️ How to Run

1.  Start the assistant from your terminal.
2.  Ask your questions at the prompt.
4.  Type **`q`** (or `quit`/`exit`) to end the session.

----- |
| **System Prompt** | Directs the model to be a specialized banking assistant, restrict answers to the provided `<context>`, and handle off-topic or unanswerable banking questions gracefully. |
| **RAG Prompt** | Sends the user's question along with the **entire merged content** to the Azure OpenAI model for context-aware generation. |
