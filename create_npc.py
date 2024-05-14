import random

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_model_and_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_npc_sheet(prompt, model, tokenizer, max_tokens=200, temp=0.7):
    inputs = tokenizer(prompt, return_tensors="pt")
    output_sequences = model.generate(
        input_ids=inputs["input_ids"],
        max_length=max_tokens,
        temperature=temp,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
    )
    npc_sheet = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    return npc_sheet

def main():
    model_name = "gpt-2"
    npc_name = "Aldric"
    npc_clan = "Ventrue"
    npc_age = "Elder"
    npc_background = (
        "Year 1209 in Europe, known for his political acumen and ruthless tactics."
        "A powerful Ventrue elder"
        "who has been a prominent figure in the Camarilla for centuries."
    )

    prompt = (
        f"Generate a detailed NPC sheet for {npc_name}, a {npc_age} {npc_clan} in Vampire: The Masquerade Dark Ages V20. "
        f"Set in the year 1209 in Europe. Include attributes, skills, disciplines, and background. "
        f"Background: {npc_background}"
    )

    model, tokenizer = load_model_and_tokenizer(model_name)
    npc_sheet = generate_npc_sheet(prompt, model, tokenizer)

    print("\nGenerated NPC Sheet:")
    print(npc_sheet)

if __name__ == "__main__":
    main()
