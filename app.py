
import streamlit as st
import os
from datetime import datetime

st.title("🌟 LizzyMary's Growth Dashboard")
st.write("A self-reliant system built from the ground up")

st.subheader(f"📅 Today: {datetime.now().strftime('%B %d, %Y')}")

st.metric("🔥 Longest Streak", "7 days", delta="+2 this week")

st.subheader("📄 Recent Logs")
logs = [f for f in os.listdir('.') if f.startswith('lizzymary_tasks_') and f.endswith('.txt')]
if logs:
    for log in sorted(logs, reverse=True)[:5]:
        st.code(f"📄 {log}", language="text")
else:
    st.text("No logs found. Run your task tracker first.")

st.info("💬 It’s alright. I’m growing.")
