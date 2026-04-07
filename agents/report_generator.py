class ReportGeneratorAgent:
    async def run(self, state):
        print("🔥 FINAL ReportGenerator RUNNING")

        results = state.get("results", [])
        matched_rules = state.get("matched_rules", {})

        files_report = []
        passed_files = 0

        for file in results:
            fname = file["file"]
            rules = file.get("rules", [])

            # 🔥 FIX 1: Handle SKIPPED properly
            if rules and all(r["status"] == "SKIPPED" for r in rules):
                status = "SKIPPED"
            else:
                status = "PASSED"
                for r in rules:
                    if r["status"] == "FAILED":
                        status = "FAILED"
                        break

            if status == "PASSED":
                passed_files += 1

            # 🔥 FIX 2: Add type + rule_set (PDF requirement)
            file_type = "unknown"
            for f in state.get("files", []):
                if f["name"] == fname:
                    file_type = f.get("type", "unknown")
                    break

            rule_set = matched_rules.get(fname, "SFT_RULES")

            files_report.append({
                "file_name": fname,
                "type": file_type,
                "rule_set": rule_set,
                "status": status,
                "rule_evaluation": rules
            })

        total = len(files_report)

        # 🔥 FIX 3: Correct pass rate (ignore SKIPPED files)
        valid_files = [f for f in files_report if f["status"] != "SKIPPED"]

        if valid_files:
            passed = sum(1 for f in valid_files if f["status"] == "PASSED")
            pass_rate = (passed / len(valid_files)) * 100
        else:
            passed = 0
            pass_rate = 0

        failed = len(valid_files) - passed

        # 🔥 FIX 4: Correct final verdict
        if pass_rate == 100:
            final_status = "PASSED"
        elif pass_rate == 0:
            final_status = "FAILED"
        else:
            final_status = "PARTIAL"

        report = {
            "files": files_report,
            "summary": {
                "total_files": total,
                "passed": passed,
                "failed": failed,
                "pass_rate": f"{pass_rate:.2f}%"
            },
            "final_verdict": final_status
        }

        print(f"✅ FINAL REPORT GENERATED: {final_status} ({pass_rate:.2f}%)")

        state["final_report"] = report
        return {"final_report": report}