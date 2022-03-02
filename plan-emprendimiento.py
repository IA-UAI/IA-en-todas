import os
import openai

# Select the theme or leave blank for auto theme generation
theme = "mouse para gente zurda" 

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-001",
  prompt=f"Lo siguiente generará un plan de acción de ingeniería para poder realizar un proyecto de emprendimiento. \nEl plan de acción deberá ser detallado, definirá los objetivos, tendrá consejos útiles y las herramientas necesarias que se utilizaran para el desarrollo específico del proyecto.\n\nProyecto de emprendimiento: {theme}",
  temperature=0.86,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0.52,
  presence_penalty=0.46
)
