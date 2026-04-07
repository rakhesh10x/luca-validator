import gdown
from pathlib import Path

class DriveDownloader:
    @staticmethod
    async def download(drive_link: str) -> str:
        output_dir = "downloaded_dataset"
        Path(output_dir).mkdir(exist_ok=True)
        
        try:
            gdown.download_folder(drive_link, output=output_dir, quiet=False, remaining_ok=True)
            print(f"✅ DriveDownloader: Files downloaded to {output_dir}")
            return output_dir
        except Exception as e:
            print(f"❌ Drive download failed: {e}")
            return None