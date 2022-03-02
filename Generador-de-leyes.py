import os
import openai

# Select the theme or leave blank for auto theme generation
theme = "" 

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-001",
  prompt="Lo siguiente es un la ley creada en 2022 sobre un tema en específico en chile.\n###\nTema: ",
  temperature=0.7,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
