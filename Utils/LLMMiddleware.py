import ollama


class OllamaLLM:
    def __init__(self, model="llama3.1", host="http://localhost:11434"):
        self.model = model
        self.client = ollama.Client(host=host)

    def chat(self, prompt, system_prompt=None):
        messages = []

        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })

        messages.append({
            "role": "user",
            "content": prompt
        })

        response = self.client.chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]
