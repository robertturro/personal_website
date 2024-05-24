from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, QuestionSerializer, LinkClickSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Question, LinkClick
from .rag import *


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CreateQuestion(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer, request):
        if serializer.is_valid():
            question = request.POST.get("#question")
            context = get_context(question)
            prompt = create_prompt(context, question)
            response = get_response(prompt)

            serializer.save(answer=response)
        else:
            print(serializer.errors)

    #def get_querset(self):



class CreateLinkClick(generics.CreateAPIView):
    queryset = LinkClick.objects.all()
    serializer_class = LinkClickSerializer
    permission_classes = [AllowAny]








