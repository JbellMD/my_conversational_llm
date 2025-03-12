# llm/model.py

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from llm import config

print("🚀 Loading fine-tuned model from:", config.MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(config.MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(config.MODEL_PATH)

def generate_response_with_context(user_input, context):
    """
    Generate an AI response given the user input and conversation context.
    The prompt is constructed by concatenating the previous context with the new input.
    """
    prompt = context + f"User: {user_input}\nAI:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Move model and inputs to GPU if available
    if torch.cuda.is_available():
        input_ids = input_ids.to("cuda")
        model.to("cuda")

    output = model.generate(
        input_ids,
        max_length=config.GENERATE_MAX_LENGTH,
        temperature=config.GENERATE_TEMPERATURE,
        top_k=config.GENERATE_TOP_K,
        top_p=config.GENERATE_TOP_P,
        do_sample=config.GENERATE_DO_SAMPLE,
        repetition_penalty=config.GENERATE_REPETITION_PENALTY,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # If there's an "AI:" marker in the output, return the text following it
    if "AI:" in response:
        response = response.split("AI:")[-1].strip()
    return response

