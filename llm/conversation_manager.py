# llm/conversation_manager.py

class ConversationManager:
    def __init__(self, max_history_chars=2000):
        self.history = []
        self.max_history_chars = max_history_chars

    def add_turn(self, user_input, ai_response):
        """Append a conversation turn to the history."""
        self.history.append({"user": user_input, "ai": ai_response})

    def get_context(self):
        """Concatenate conversation history into a single prompt string.
        
        If the concatenated context exceeds max_history_chars,
        it truncates older parts to fit within the limit.
        """
        context = ""
        for turn in self.history:
            context += f"User: {turn['user']}\nAI: {turn['ai']}\n"
        if len(context) > self.max_history_chars:
            # Keep only the latest conversation portion within the character limit
            context = context[-self.max_history_chars:]
        return context

    def reset(self):
        """Clear the conversation history."""
        self.history = []
