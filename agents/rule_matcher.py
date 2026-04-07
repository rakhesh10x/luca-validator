class RuleMatcherAgent:
    async def run(self, state):
        files = state.get("files", [])
        matched = {}

        for file in files:
            fname = file["name"].lower()
            if fname.endswith(".txt") and any(k in fname for k in ["paragraph", "chatgpt", "copilot", "deepseek", "gemini", "grok", "perplexity", "lechat", "claud", "gork"]):
                matched_rule = "SFT_RULES"
            else:
                matched_rule = "NO_RULE"
            matched[file["name"]] = matched_rule

        print(f"✅ RuleMatcherAgent: {sum(1 for v in matched.values() if v == 'SFT_RULES')} files matched with SFT_RULES")
        return {"matched_rules": matched}