import streamlit as st
from backend.compile_ai import compile_ai
from backend.compare import compare
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Compiler Pro", layout="centered")

st.title("🚀 AI Compiler PRO")
st.markdown("### Deep Learning Based Optimization System")

st.sidebar.title("About")
st.sidebar.info("AI + Compiler + Deep Learning System")

file = st.file_uploader("Upload C File", type=["c"])

if file:
    with open("temp.c", "wb") as f:
        f.write(file.read())

    st.success("File uploaded!")

    if st.button("Run AI Optimization"):
        opt, time_ai = compile_ai("temp.c")

        st.write(f"### AI Selected: -{opt}")
        st.write(f"Execution Time: {time_ai:.5f}")

        opts, times = compare("temp.c")

        fig, ax = plt.subplots()
        ax.bar(opts, times)
        ax.set_title("AI vs Traditional Optimization")
        st.pyplot(fig)