import os
import openai

# Select the theme or leave blank for auto theme generation
condition = "ADHD"

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-001",
  prompt=f"Lo siguiente es una conversación entre un psicólogo intentando explicarle a su paciente que sufre de una condición psicológica.\nEl psicólogo es amigable y explica los conceptos con claridad a su joven e ingenuo paciente\n###\nCondición psicológica: {codition}\n\nPsicólogo: Me parece que es importante que entiendas lo que está pasando, ¿podemos hablar sobre tu condición psicológica?",
  temperature=0.7,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
