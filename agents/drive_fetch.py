import gdown
from pathlib import Path

class DriveFetchAgent:
    async def run(self, state):
        link = state["drive_link"]
        output_dir = "downloaded_dataset"
        Path(output_dir).mkdir(exist_ok=True)
        
        try:
            gdown.download_folder(link, output=output_dir, quiet=False, remaining_ok=True)
            files = []
            for f in Path(output_dir).rglob("*"):
                if f.is_file() and ".git" not in str(f):
                    files.append({"path": str(f), "name": f.name, "size": f.stat().st_size})
            
            print(f"✅ DriveFetchAgent: {len(files)} clean files downloaded")
            return {"files": files}
        except Exception as e:
            return {"files": [], "error": str(e)}