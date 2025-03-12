# My Conversational LLM

This project implements a conversational AI assistant using a fine-tuned TinyLlama 1.1B Chat model with the PEFT library. It features:

- **Conversation History Management:**  
  Maintains context over multiple exchanges using a dedicated conversation manager.

- **Robust Model Inference:**  
  Generates responses that include previous conversation context.

- **Sophisticated GUI:**  
  A tkinter-based chat interface that displays conversation history and allows for interactive messaging.

## Directory Structure

```
my_conversational_llm/
├── app.py
├── gui/
│   ├── chat_interface.py
│   └── __init__.py
├── llm/
│   ├── config.py
│   ├── conversation_manager.py
│   ├── model.py
│   └── __init__.py
├── requirements.txt
└── README.md
```
