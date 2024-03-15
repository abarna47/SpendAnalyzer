import requests

CATEGORY_PROMPT = """
Given a spending category from popular bank or credit card statements, tell me which of the
following categories it belongs to.
```
Housing
Transportation
Food
Personal insurance and pensions
Healthcare
Entertainment
Cash contributions
Apparel and services
Education
Utilities
```
Give me only the most similar category from the list above. Do not include anything else with your answer.
Category: 
"""


class OpenAiApi:
    def __init__(self):
        self.url = "https://api.openai.com/v1/engines/davinci-codex/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer xxxx",  # Replace 'xxxx' with your actual API key
        }

    def get_category(self, statement_category):
        data = {
            "prompt": f"{CATEGORY_PROMPT}{statement_category}",
            "max_tokens": 60
        }

        response = requests.post(self.url, headers=self.headers, json=data)
        return response.json()['choices'][0]['text'].strip()
