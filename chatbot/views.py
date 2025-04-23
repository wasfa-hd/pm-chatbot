import openai
import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are a professional yet friendly Project Manager Assistant chatbot, helping users with job-related queries like resumes, interviews, roles, and project guidance.
Answer clearly, concisely, and with structured points or short paragraphs. Use markdown-like formatting for readability:
- Bullet points
- Numbered lists
- Headings where needed
Avoid sounding robotic. Be helpful, human, and supportive.
"""


@csrf_exempt
def chat_with_gpt(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content.strip()
            return JsonResponse({"reply": reply})
        except Exception as e:
            print("GPT error:", e)  
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request"}, status=400)

def chat_page(request):
    return render(request, "chatbot/chat.html")
