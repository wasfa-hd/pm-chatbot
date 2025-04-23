from openai import OpenAI
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a helpful project manager assistant...
"""

@csrf_exempt
def chat_with_gpt(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message")
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content.strip()
            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request"}, status=400)

def chat_page(request):
    return render(request, "chatbot/chat.html")
