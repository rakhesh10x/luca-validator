class ExecutionAgent:
    async def run(self, state):
        print("🔥 NEW ExecutionAgent RUNNING")

        files = state.get("files", [])
        results = []

        for file in files:
            fname = file["name"]
            content = file.get("content", "").split("\n")

            file_result = {
                "file": fname,
                "rules": []
            }

            # Skip unsupported
            if file.get("type") == "unsupported":
                file_result["rules"].append({
                    "rule": "Unsupported File",
                    "status": "SKIPPED",
                    "details": "File type not supported"
                })
                results.append(file_result)
                continue

            # ===== RULE 1: EOS =====
            failed_lines = [
                i + 1 for i, line in enumerate(content)
                if line.strip() and not line.strip().endswith("<eos>")
            ]

            file_result["rules"].append({
                "rule": "Ends with EOS",
                "status": "PASSED" if not failed_lines else "FAILED",
                "details": "All lines valid" if not failed_lines else f"Missing <eos> at lines {failed_lines}"
            })

            # ===== RULE 2: Empty lines =====
            empty_lines = [
                i + 1 for i, line in enumerate(content)
                if line.strip() == ""
            ]

            file_result["rules"].append({
                "rule": "No empty lines",
                "status": "PASSED" if not empty_lines else "FAILED",
                "details": "No empty lines" if not empty_lines else f"Empty lines at {empty_lines}"
            })

            # ===== RULE 3: Format =====
            format_errors = [
                i + 1 for i, line in enumerate(content)
                if line.strip() and not (
                    "[INSTRUCT=4]" in line and
                    "[RESPONSE=5]" in line and
                    "[END=6]" in line
                )
            ]

            file_result["rules"].append({
                "rule": "INSTRUCT RESPONSE format",
                "status": "PASSED" if not format_errors else "FAILED",
                "details": "Correct format" if not format_errors else f"Format issues at lines {format_errors}"
            })

            results.append(file_result)

        state["results"] = results   # ✅ IMPORTANT FIX
        return {"results": results}