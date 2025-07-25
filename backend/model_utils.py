import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "command-r"

def clean_chart_code(response_text: str) -> str:
    code = response_text.strip()
    if "```" in code:
        parts = code.split("```")
        code = parts[1] if len(parts) > 1 else parts[0]
    cleaned = code.replace("python", "").replace("...", "").strip()
    return cleaned

def get_chart_instructions(prompt, df):
    sample_data = df.head(3).to_dict()
    full_prompt = f"""You are a Python data visualization assistant.
Your task is to:
✅ Understand user intent from natural language.
✅ Choose appropriate chart type (bar, pie, line, etc.) based on the query.
✅ Apply basic logic (like top/bottom N filtering, group-by, aggregation) if the prompt implies it.
✅ Generate clean Plotly Express code using 'df'.
✅ Use 'fig = ...' syntax and return the fig.
❌ Do NOT use ellipses (...) or placeholders.
❌ Do NOT output markdown or text, only raw code.

Sample Data: {sample_data}
User Request: {prompt}

Return code only below:
```python
# Plotly Express chart using df
"""

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    })

    result = response.json()["response"]
    return clean_chart_code(result)
