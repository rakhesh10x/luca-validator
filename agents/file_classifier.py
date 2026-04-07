from pathlib import Path

class FileClassifierAgent:
    SUPPORTED_EXT = {".json", ".jsonl", ".txt", ".npy", ".pt", ".py"}

    async def run(self, state):
        for file in state.get("files", []):
            ext = Path(file["path"]).suffix.lower()
            file["type"] = ext if ext in self.SUPPORTED_EXT else "unsupported"

            # 🔥 IMPORTANT FIX: READ FILE CONTENT
            try:
                if file["type"] == ".txt":
                    with open(file["path"], "r", encoding="utf-8") as f:
                        file["content"] = f.read()
                else:
                    file["content"] = ""
            except:
                file["content"] = ""

        print("✅ FileClassifierAgent: Files classified + content loaded")
        return {}