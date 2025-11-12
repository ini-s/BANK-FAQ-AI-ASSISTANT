import json
import os

from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()


def load_data():
    try:
        with open("bank_faq.txt", 'r') as file:
            content = file.read()
            return content

    except Exception as e:
        print(e)
        return content


def BANK_FAQ_AI_ASSISTANT():
    faq_assistant = AzureOpenAI(
        api_version="2024-12-01-preview",
        azure_endpoint=os.getenv("API_ENDPOINT"),
        api_key=os.getenv("API_KEY"),
    )

    while True:

        user_input = input("Ask a question (To quit, press 'q'): ")

        content = load_data()

        prompt = f"""
                    {user_input}
                    <context>
                    {content}
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
                        You are a banking assistant and your job is to provide answers to frequently asked questions(FAQs).
                        Focus on using only the questions and answers provided as q and a in the <context>.
                        For questions not provided in the <context>, tell the user to contact customer care.
                        For questions not related to the bank, tell that you can only answer questions related to the bank.
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
    BANK_FAQ_AI_ASSISTANT()
