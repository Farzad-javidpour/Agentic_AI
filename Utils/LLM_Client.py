import ollama
from datetime import datetime


class OllamaClient:

    def __init__(
        self,
        host="http://localhost:11434"
    ):
        self.host = host
        self.client = ollama.Client(host=host)

    def chat(
        self,
        model,
        messages
    ):

        start_time = datetime.now()

        try:

            response = self.client.chat(
                model=model,
                messages=messages
            )

            answer = response["message"]["content"]

            prompt_tokens = response.get(
                "prompt_eval_count",
                0
            )

            completion_tokens = response.get(
                "eval_count",
                0
            )

            total_tokens = (
                prompt_tokens +
                completion_tokens
            )

            end_time = datetime.now()

            duration_seconds = (
                end_time - start_time
            ).total_seconds()

            tokens_per_second = (
                completion_tokens / duration_seconds
                if duration_seconds > 0
                else 0
            )

            return {
                "success": True,

                "response": answer,

                "usage": {
                    "prompt_tokens": prompt_tokens,
                    "completion_tokens": completion_tokens,
                    "total_tokens": total_tokens
                },

                "model": {
                    "name": model
                },

                "performance": {
                    "duration_ms": round(
                        duration_seconds * 1000,
                        2
                    ),

                    "tokens_per_second": round(
                        tokens_per_second,
                        2
                    )
                },

                "timestamp": end_time.isoformat()
            }

        except Exception as e:

            return {
                "success": False,

                "response": None,

                "error": {
                    "type": type(e).__name__,
                    "message": str(e)
                },

                "model": {
                    "name": model
                },

                "timestamp": datetime.now().isoformat()
            }