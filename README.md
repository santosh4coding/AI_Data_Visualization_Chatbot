# AI-Powered Chart Generator (Ollama + Streamlit) - Fixed Version

## Features
- Upload CSV or Excel
- Ask natural questions to generate Pie, Bar, Line, etc. charts
- Uses Ollama with mistral locally (offline)
- Cleans AI output for valid matplotlib syntax
- Shows generated Python code

## How to Run

1. Start Mistral in Ollama:
```bash
ollama run mistral
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```
