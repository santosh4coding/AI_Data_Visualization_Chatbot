import streamlit as st
import pandas as pd
from backend.chart_generator import generate_chart
from backend.model_utils import get_chart_instructions
from backend.insights import get_insights
from io import BytesIO
from plotly.io import write_image
from plotly.graph_objs import Figure

st.set_page_config(page_title="AI Chart Studio", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.title("📁 Upload & Filter")

    uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
    theme = st.toggle("🌗 Dark Mode", value=True)

    df = None
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)

        # Sidebar filters
        if 'Region' in df.columns:
            regions = st.multiselect("Filter by Region", df['Region'].unique())
            if regions:
                df = df[df['Region'].isin(regions)]

        if 'Branch ID' in df.columns:
            branches = st.multiselect("Filter by Branch ID", df['Branch ID'].unique())
            if branches:
                df = df[df['Branch ID'].isin(branches)]

        st.download_button("⬇️ Download Filtered Data", df.to_csv(index=False).encode(), "filtered_data.csv")

# --- Main UI ---
st.markdown("<h1 style='text-align:center;'>AI-Powered Visualization Dashboard</h1>", unsafe_allow_html=True)

if uploaded_file and df is not None:
    st.subheader("📋 Data Preview")
    st.dataframe(df.head(5), use_container_width=True)

    st.markdown("### 🤖 Ask a question or describe a chart")
    user_prompt = st.text_input("Prompt", placeholder="e.g., Show SB Balance by Region in pie chart")

    if user_prompt:
        with st.spinner("🔎 Analyzing your prompt and generating chart..."):
            chart_code = get_chart_instructions(user_prompt, df)
            chart = generate_chart(df, chart_code)

            if isinstance(chart, Figure):
                # Save chart as image for download
                fig_buf = BytesIO()
                write_image(chart, fig_buf, format="png")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### 📈 Generated Chart")
                    st.plotly_chart(chart, use_container_width=True)
                    st.download_button("📤 Download Chart", fig_buf.getvalue(), "generated_chart.png", "image/png")

                with col2:
                    st.markdown("### 📌 AI-Generated Insights")
                    insights = get_insights(user_prompt, df)
                    st.info(insights)
            else:
                st.error(f"❌ Chart generation failed:\n{chart}")
else:
    st.info("👈 Please upload a dataset from the sidebar to get started.")
