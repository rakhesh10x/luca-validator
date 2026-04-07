import streamlit as st

# 🔥 FIX: Make sure project root is in path
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import asyncio
import json

from langgraph_workflow import run_validation_pipeline

# ✅ DB functions
from database import init_db, save_history, get_history

# ✅ Initialize DB
init_db()

# 🎯 Title
st.title("🚀 Luca Validator")

# 📥 Inputs
drive_link = st.text_input("Enter Google Drive Link")
rule_sets_input = st.text_area("Enter Rule Sets (JSON format)")

# ==============================
# 🚀 RUN VALIDATION
# ==============================

if st.button("Run Validation"):

    if not drive_link:
        st.warning("⚠️ Please enter a Drive link")
    else:
        try:
            # convert rule_sets string → dict
            rule_sets = json.loads(rule_sets_input) if rule_sets_input else {}

            st.info("⏳ Running validation pipeline...")

            # ✅ Async execution
            result = asyncio.run(
                run_validation_pipeline(drive_link, rule_sets)
            )

            # ✅ Save history
            save_history(drive_link, result)

            st.success("✅ Validation Completed")

            # ✅ Show result nicely
            st.json(result)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")


# ==============================
# 📜 HISTORY SECTION
# ==============================

st.markdown("## 📜 History")

if st.button("Show History"):
    history = get_history()

    if not history:
        st.info("No history found")
    else:
        for item in history:
            st.write(f"🔹 ID: {item[0]}")
            st.write(f"🔗 Drive Link: {item[1]}")

            # ✅ Convert string → JSON safely
            try:
                parsed_result = json.loads(item[2])
                st.json(parsed_result)
            except:
                st.write(item[2])

            st.write("------")