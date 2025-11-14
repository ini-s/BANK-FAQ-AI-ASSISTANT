import os

from openai import AzureOpenAI
from dotenv import load_dotenv
from utils import *

load_dotenv()


def load_and_merge_files():
    file_names = ["faq.txt", "bank_policy.txt", "loan_policy.txt"]
    output_file = "merged_bank_files.txt"

    try:
        if not os.path.exists(output_file):
            with open(output_file, 'w', encoding="utf-8", newline="\n") as f:
                for file in file_names:
                    try:
                        data = load_data(file)
                    except UnicodeDecodeError:
                        # Retry reading with latin-1 if utf-8 fails
                        with open(file, "r", encoding="latin-1") as alt_f:
                            data = alt_f.read()
                    except Exception as e:
                        print(f"Error reading {file}: {e}")
                        data = ""

                    if data is None:
                        data = ""
                    f.write(data)
                    f.write("\n")

        # Load merged file content
        merged_files = load_data(output_file)
        return merged_files

    except Exception as e:
        print(f"Error merging files: {e}")
        return ""


def BANK_AI_ASSISTANT():
    faq_assistant = AzureOpenAI(
        api_version="2024-12-01-preview",
        azure_endpoint=os.getenv("API_ENDPOINT"),
        api_key=os.getenv("API_KEY"),
    )

    chat_history = []
    history_limit = 4

    while True:
        bank_data = load_and_merge_files()
        user_input = input("Ask a question (To quit, press 'q'): ")

        prompt = f"""
                    {user_input}
                    <context>
                    {bank_data}
                    </context>
                """

        if user_input.strip().lower() in ["q", "quit", "exit"]:
            print("👋 Goodbye!")
            exit()

        recent = chat_history[-history_limit:]
        history_for_system = json.dumps(recent, ensure_ascii=False)
        try:
            response = faq_assistant.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"""
                        You are a concise, helpful banking assistant. ALWAYS use only the information provided inside the <context> block to answer user questions.
                        If the answer is NOT found in <context>, reply exactly with the single phrase: "The answer is not available in my current knowledge base. Please contact customer care for assistance." 
                        When an answer is found, give a short (<=120 words) clear answer, include one short actionable step the user can take (if relevant), and finish with a one-sentence suggested follow-up question.
                        Do NOT invent facts or provide information not present in <context>.
                        Recent conversation history (most recent {len(recent)} turns):\n{history_for_system}
                        """,
                    },

                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-4o-mini",
                temperature=0,
            )

            response = response.choices[0].message.content
            chat_history.append({"role": "user", "content": user_input})
            chat_history.append({"role": "assistant", "content": response})
            print(response)

        except Exception as e:
            print(f"Error message: {e}")


if __name__ == '__main__':
    BANK_AI_ASSISTANT()
