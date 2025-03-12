# llm/config.py

# Path to your fine-tuned model (update if necessary)
MODEL_PATH = "C:/AI_Model/fine_tuned_model"

# Conversation manager configuration
MAX_HISTORY_CHARS = 2000

# Generation parameters for the model
GENERATE_MAX_LENGTH = 300
GENERATE_TEMPERATURE = 0.9
GENERATE_TOP_K = 50
GENERATE_TOP_P = 0.95
GENERATE_DO_SAMPLE = True
GENERATE_REPETITION_PENALTY = 1.1
