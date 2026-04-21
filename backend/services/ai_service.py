from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HF_TOKEN")
)

def ask_ai(question, materials):
    context = "\n".join([
        f"{m.name}: densidade={m.density}, resistência={m.strength}, maleabilidade={m.malleability}"
        for m in materials
    ])

    prompt = f"""
Você é um engenheiro especialista em materiais automotivos.

Dados:
{context}

Pergunta:
{question}

Responda de forma técnica e objetiva.
"""

    response = client.text_generation(
        prompt,
        max_new_tokens=300
    )

    return response