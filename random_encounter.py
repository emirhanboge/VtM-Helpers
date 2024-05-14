import random

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_model_and_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_encounter(prompt, model, tokenizer, max_tokens=100, temp=1.0):
    inputs = tokenizer(prompt, return_tensors="pt")
    output_sequences = model.generate(
        input_ids=inputs["input_ids"],
        max_length=max_tokens,
        temperature=temp,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
    )
    encounter_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    return encounter_text

def main():
    model_name = "EleutherAI/gpt-j-6b"
    environment = "Forest"
    difficulty = "Medium"
    max_tokens = 150
    temp = 0.7

    model, tokenizer = load_model_and_tokenizer(model_name)
    prompt = f"Generate a {difficulty} encounter in a {environment}:"
    encounter = generate_encounter(prompt, model, tokenizer, max_tokens=max_tokens, temp=temp)

    print("\nGenerated Encounter:")
    print(encounter)

if __name__ == "__main__":
    main()
