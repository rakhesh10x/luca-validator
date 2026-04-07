from langchain_openai import ChatOpenAI
import gdown

class AccessValidatorAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    async def run(self, state):
        link = state["drive_link"]
        try:
            file_id = gdown.parse_url(link)[1]
            status = "PUBLIC" if file_id else "RESTRICTED"
            print(f"✅ AccessValidator: {status}")
            return {"access_status": status}
        except:
            return {"access_status": "RESTRICTED", "error": "Drive link not public"}