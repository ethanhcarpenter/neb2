from llama_cpp import Llama
import os

class LocalAIChatbot:
    def __init__(self, model_path, n_ctx=2048, n_gpu_layers=-1):
        self.model = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_gpu_layers=n_gpu_layers,
            n_threads=os.cpu_count(),
            n_batch=512
        )
        self.chat_history = []

    def chat(self, user_message, max_tokens=128):
        self.chat_history.append({"role": "user", "content": user_message})

        prompt = self._build_prompt()

        response = self.model(
            prompt,
            max_tokens=max_tokens,
            stop=["User:", "AI:"]
        )
        ai_response = response["choices"][0]["text"].strip()

        if ai_response.lower().startswith("ai:"):
            ai_response = ai_response[3:].strip()

        self.chat_history.append({"role": "assistant", "content": ai_response})
        return ai_response,prompt


    def _build_prompt(self, history_limit=30):
        prompt = "The following is a conversation between a helpful AI assistant and a user.\n"

        for entry in self.chat_history[-history_limit * 2:]:  # last N exchanges
            role = "AI" if entry["role"] == "assistant" else "User"
            prompt += f"{role}: {entry['content']}\n"

        prompt += "AI:"
        return prompt


    def reset(self):
        """Clears the chat history."""
        self.chat_history = []
