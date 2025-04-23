from openai import OpenAI
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Initialize OpenAI client using the new SDK style
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt for structured, helpful chatbot replies
SYSTEM_PROMPT = """
You are a professional yet friendly Project Manager Assistant chatbot,
helping users with job-related queries like resumes, interviews, roles, and project guidance.
Answer clearly, concisely, and with structured points or short paragraphs. Use markdown-like formatting:
- Bullet points
- Numbered lists
- Headings where needed
Avoid sounding robotic. Be helpful, human, and supportive.
"""

@csrf_exempt
def chat_with_gpt(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("message", "")
            
            # Make call to OpenAI
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content
            return JsonResponse({"reply": reply})
        
        except Exception as e:
            print("OpenAI error:", e)  # Optional: log to server
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request"}, status=400)


def chat_page(request):
    return render(request, "chatbot/chat.html")
