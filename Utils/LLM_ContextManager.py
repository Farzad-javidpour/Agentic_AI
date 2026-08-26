class ContextManager:

    def __init__(self):
        self._messages = []

    def add(self, role: str, content: str):
        self._messages.append({
            "role": role,
            "content": content
        })

    def get_context(self) -> list[dict]:
        return self._messages.copy()

    def clear(self):
        self._messages.clear()

    def count(self):
        return len(self._messages)