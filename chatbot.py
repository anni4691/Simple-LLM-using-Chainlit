# -*- coding: utf-8 -*-
"""ChatBot



Original file is located at
    https://colab.research.google.com/drive/1LyBHGtj01e6teTS5lk2Aju0UiL7Et9zq
"""

!pip install chainlit
!pip install ollama
!pip install transformers

!pip install torch

from transformers import pipeline

# Load a small Hugging Face model (OPT-1.3B)
chat_model = pipeline("text-generation", model="facebook/opt-1.3b")

def get_llm_response(prompt):
    response = chat_model(prompt, max_length=150, do_sample=True, temperature=0.7)
    return response[0]['generated_text']

# Commented out IPython magic to ensure Python compatibility.
# %%writefile mental_health_assistant.py
# import chainlit as cl
# from transformers import pipeline
# 
# # Load a smaller model for efficiency
# chat_model = pipeline("text-generation", model="facebook/opt-1.3b")
# 
# # Define the Mental Health Assistant behavior
# ASSISTANT_PROMPT = """
# You are a highly empathetic and intelligent Mental Health Assistant.
# Your job is to analyze users' emotions based on their inputs, detect possible mental health concerns,
# and provide precise self-care guidance.
# 
# When a user describes their feelings, thoughts, or behaviors:
# - Assess their emotional state.
# - Identify potential conditions (e.g., stress, anxiety, burnout).
# - Estimate the severity in percentage (0% to 100%).
# - If symptoms indicate distress, offer actionable self-care strategies (e.g., deep breathing, mindfulness, journaling).
# - If symptoms are severe, recommend professional help in a supportive way.
# - If no major concerns are detected, provide an uplifting message to boost mood and encourage self-love.
# 
# Maintain a warm, non-judgmental, and conversational tone, ensuring users feel heard and supported.
# """
# 
# # Function to generate chatbot responses
# def get_llm_response(user_input):
#     prompt = f"{ASSISTANT_PROMPT}\n\nUser: {user_input}\n\nAssistant:"
#     response = chat_model(prompt, max_length=200, do_sample=True, temperature=0.7)
#     return response[0]['generated_text'].replace(prompt, "").strip()
# 
# @cl.on_message
# async def on_message(message: cl.Message):
#     user_input = message.content.strip()
# 
#     if not user_input:
#         await cl.Message(content="Please type something!").send()
#         return
# 
#     llm_response = get_llm_response(user_input)
# 
#     await cl.Message(content=llm_response).send()
# 
#

!pip install pyngrok

from pyngrok import ngrok

# Connect to ngrok
!ngrok authtoken 2rvtHlhfnYqmfLNP6HoKTkqfyDE_TUD8XDUTQYLuFJKtRNxN

!pkill -f "ngrok"
!pkill -f "chainlit"

import time
from pyngrok import ngrok

# Restart Chainlit
!nohup chainlit run mental_health_assistant.py --port 5000 & sleep 5

# Expose the chatbot via ngrok
public_url = ngrok.connect(5000, "http")
print(f"🔗 Open the chatbot: {public_url}")







