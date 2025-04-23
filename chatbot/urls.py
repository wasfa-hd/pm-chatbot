from django.urls import path
from .views import chat_with_gpt, chat_page

urlpatterns = [
    path('', chat_page, name='chat_page'),  # 👈 HTML page at root
    path('chat/', chat_with_gpt, name='chat_with_gpt'),  # API endpoint
]
