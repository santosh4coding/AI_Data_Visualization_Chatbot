import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

def get_insights(prompt, df):
    sample_data = df.head(5).to_dict()
    full_prompt = f"""You are a data analyst. Based on the following sample data and user request, provide key insights.
Avoid generic statements. Mention any trends, outliers, or comparisons relevant to the data and the request.

Sample Data: {sample_data}
User Request: {prompt}
"""

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    })

    return response.json()["response"].strip()
