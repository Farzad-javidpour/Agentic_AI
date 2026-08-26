class Skill:

    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

    def get_skill(self) -> str:
        return self.content