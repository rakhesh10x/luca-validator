import json
import numpy as np
import torch
from pathlib import Path

class FileHandler:
    @staticmethod
    def load_file(file_path: str):
        path = Path(file_path)
        ext = path.suffix.lower()
        
        try:
            if ext == ".jsonl":
                with open(path, "r", encoding="utf-8") as f:
                    return [json.loads(line) for line in f if line.strip()]
            elif ext == ".json":
                return json.load(open(path, "r", encoding="utf-8"))
            elif ext == ".txt":
                return path.read_text(encoding="utf-8").splitlines()
            elif ext == ".npy":
                return np.load(path, allow_pickle=True)
            elif ext == ".pt":
                return torch.load(path, weights_only=True)
            else:
                return None
        except Exception as e:
            print(f"❌ File load error {path}: {e}")
            return None