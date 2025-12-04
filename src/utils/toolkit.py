from config.manager import MainManager

class Tool:
    @staticmethod
    def get_format_url(url: str) -> str:
        manager = MainManager()
        base = manager.answer_manager.get_base_url(url)

        if url.startswith(base):
            url = url.replace(base, '')
        return url