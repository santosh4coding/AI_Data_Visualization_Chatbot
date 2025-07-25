# AI Data Visualization Chatbot

An AI-powered data visualization and insight generation tool built using **Streamlit**. Upload your CSV/Excel files, apply filters, describe your desired chart or question in natural language, and let the AI generate interactive charts and insights — all within seconds.

---

## Features

- Upload **CSV or Excel** datasets
- Apply dynamic filters (Region, Branch ID, etc.)
- Use **natural language prompts** to ask for charts
- Generates Plotly-powered visualizations
- AI-generated **narrative insights**
- Download filtered datasets and generated charts as PNGs
- Dark mode toggle for better readability

---

## Project Structure

AI_Data_Visualization_Chatbot/
├── app.py # Main Streamlit app
├── backend/ # AI logic modules
│ ├── chart_generator.py # Chart creation logic
│ ├── model_utils.py # Prompt parsing / model interaction
│ └── insights.py # AI-generated insights
├── templates/ # Streamlit templates if needed
├── assets/ # Optional: logo or preview images
├── requirements.txt # Dependencies list
└── README.md

yaml
Copy
Edit

<img width="3820" height="2136" alt="image" src="https://github.com/user-attachments/assets/f210bf17-21a9-4f31-93f7-2158fd89ec9b" />


## Installation

### 1. Clone the repository

```bash
git clone git@github.com:santosh4coding/AI_Data_Visualization_Chatbot.git
cd AI_Data_Visualization_Chatbot
2. (Optional) Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

▶Running the App
bash
Copy
Edit
streamlit run app.py
Then open your browser to http://localhost:8501

<!-- ![Preview](assets/preview.png) -->
Prompt Examples
Show SB Balance by Region as a pie chart

Line chart of monthly deposits over the past year

Top 5 Branches by loan disbursement

Bar chart of account openings in May 2024

Requirements
Add these to requirements.txt if not already included:

graphql
Copy
Edit
streamlit
pandas
plotly
openai            # or whichever LLM backend you're using
kaleido           # for chart image export

To-Do
 Add authentication for internal use

 Integrate with local LLM (e.g., Mistral via Ollama)

 Export insights to PDF

 Deploy on Streamlit Cloud or Docker

License
This project is licensed under the MIT License.
Feel free to use and adapt for your organization.

Author
Santosh Kumar
Chiru
