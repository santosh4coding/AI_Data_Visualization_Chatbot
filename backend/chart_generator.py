import plotly.express as px

def generate_chart(df, code_snippet):
    local_scope = {"df": df, "px": px}

    # 🚨 Basic validation for broken LLM output
    if "..." in code_snippet or len(code_snippet.strip()) < 10:
        return "Chart code incomplete or invalid. Please try a different prompt."

    try:
        exec(code_snippet, {}, local_scope)
        return local_scope.get("fig", None)
    except Exception as e:
        return f"Error generating chart: {e}"
