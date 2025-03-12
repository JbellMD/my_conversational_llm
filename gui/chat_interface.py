# gui/chat_interface.py

import tkinter as tk
from llm.model import generate_response_with_context
from llm.conversation_manager import ConversationManager
from llm.config import MAX_HISTORY_CHARS

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline AI Conversational Assistant")
        self.conversation_manager = ConversationManager(max_history_chars=MAX_HISTORY_CHARS)
        self.setup_widgets()

    def setup_widgets(self):
        # Frame for the chat display with scrollbar
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(padx=10, pady=10)

        self.chat_display = tk.Text(self.chat_frame, height=20, width=60, state="disabled", wrap="word")
        self.scrollbar = tk.Scrollbar(self.chat_frame, command=self.chat_display.yview)
        self.chat_display['yscrollcommand'] = self.scrollbar.set

        self.chat_display.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # User input area
        self.input_box = tk.Text(self.root, height=3, width=60, wrap="word")
        self.input_box.pack(padx=10, pady=(0, 10))
        self.input_box.bind("<Return>", self.handle_enter)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.handle_send)
        self.send_button.pack(pady=(0, 10))

    def handle_enter(self, event):
        # Prevent newline insertion on Enter key and trigger send
        self.handle_send()
        return "break"

    def handle_send(self):
        user_input = self.input_box.get("1.0", "end-1c").strip()
        if not user_input:
            return

        # Display the user's message
        self.update_chat(f"You: {user_input}\n")
        self.input_box.delete("1.0", tk.END)

        # Retrieve the conversation context and generate a response
        context = self.conversation_manager.get_context()
        try:
            ai_response = generate_response_with_context(user_input, context)
        except Exception as e:
            ai_response = f"Error generating response: {e}"

        # Display the AI response
        self.update_chat(f"AI: {ai_response}\n")
        # Save the exchange into conversation history
        self.conversation_manager.add_turn(user_input, ai_response)

    def update_chat(self, message):
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, message)
        self.chat_display.config(state="disabled")
        self.chat_display.see(tk.END)
