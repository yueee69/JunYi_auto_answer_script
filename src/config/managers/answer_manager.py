import os

from .BASE_DRIVER import BaseDriver

class AnswerManager(BaseDriver):
    def __init__(self):
        super().__init__()
        self.path = 'config/app/answer.json'
        self.load_json()
    
    def get_base_url(self, url: str, complete: bool = False) -> str:
        cache = self._cache.get(self.path, {})
        data: str = cache.get("base", None)
        if data is None:
            raise ValueError("Base URL not found in answer.json")

        if complete:
            return data + url
        return data
    
    def extract_qid(self, url: str) -> str:
        path = url.split("junyiacademy.org/")[-1]
        segments = [s for s in path.split("/") if s]

        try:
            last = segments[-1]
            if last.startswith("jr-"):
                last = last.replace("jr-", "")
            return last
        
        except IndexError:
            raise ValueError("請輸入正確的URL https://www.junyiacademy.org/XXXXXXXXXXXXXXXX")
        
    def needs_exam_prefix(self, url: str) -> bool:
        path = url.split("junyiacademy.org/")[-1]
        segments = [s for s in path.split("/") if s]

        return (segments[0] == "exam" and not segments[-1].startswith("jr-"))

    def get_answer_url(self, url: str) -> str:
        qid = self.extract_qid(url)

        if self.needs_exam_prefix(url):
            return f"https://www.junyiacademy.org/api/v2/perseus/exam/{qid}/get_question"
        else:
            print("目前不支援國中端")
            os.system("pause")
            return
            return f"https://www.junyiacademy.org/api/v2/perseus/{qid}/get_question"
