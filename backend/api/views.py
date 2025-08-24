from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, QuestionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Question
from .rag import *
from datetime import date
import json
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
#from django.views.decorators.http import condition
#from channels.layers import get_channel_layer
#from asgiref.sync import async_to_sync
#test


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
 

class CreateQuestion(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]


    def post(self, request): 
        data = json.loads(request.body)
        question = data.get('question')

        context = get_context(question)
        prompt = create_prompt(context, question)
        thread = create_thread()
        response = get_response(prompt, thread)

        q = Question(question=question, date=date.today(), answer=response)
        q.save()

        return JsonResponse({'response': response})
        









