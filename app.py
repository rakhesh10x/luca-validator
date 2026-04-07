import streamlit as st
import asyncio
from langgraph_workflow import run_validation_pipeline

# 🎯 Title
st.title("🚀 Luca Validator")

# 📥 Inputs
drive_link = st.text_input("Enter Google Drive Link")
rule_sets_input = st.text_area("Enter Rule Sets (JSON format)")

# 🔘 Button
if st.button("Run Validation"):

    if not drive_link:
        st.warning("⚠️ Please enter a Drive link")
    else:
        try:
            # convert rule_sets string → dict
            import json
            rule_sets = json.loads(rule_sets_input) if rule_sets_input else {}

            st.info("⏳ Running validation pipeline...")

            # ✅ ASYNC CALL FIX
            result = asyncio.run(
                run_validation_pipeline(drive_link, rule_sets)
            )

            st.success("✅ Validation Completed")
            st.write(result)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")