import os

from openai import AzureOpenAI
from dotenv import load_dotenv
from utils import *

load_dotenv()


def load_and_merge_files():
    try:
        file_names = ["faq.txt", "bank_policy.txt", "loan_policy.txt"]
        output_file = "merged_bank_files.txt"

        if not os.path.exist(output_file):
            with open(output_file, 'w', encoding="utf-8", newline="\n") as f:
                for file in file_names:
                    data = load_data(file)
                    f.write(data)

        merged_files = load_data("merged_bank_files.txt")
        return merged_files

    except Exception as e:
        print(e)


def BANK_AI_ASSISTANT():
    faq_assistant = AzureOpenAI(
        api_version="2024-12-01-preview",
        azure_endpoint=os.getenv("API_ENDPOINT"),
        api_key=os.getenv("API_KEY"),
    )

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

        try:
            response = faq_assistant.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"""
                        You are a banking assistant and your job is to provide answers to customer(user) questions.
                        You are to answer only banking related questions using only the information provided in <context>.
                        For questions unrelated to the bank, tell the customer(user) that you can only respond to banking related questions.
                        Questions and answers are provided in <context> as q for question and a for answer while other content in <context> will guide
                        you to answer other customer(user) questions that are banking related.
                        If the answer to a question asked is not provided in <context>, tell the user to contact customer care.
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

            print(response.choices[0].message.content)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    BANK_AI_ASSISTANT()
