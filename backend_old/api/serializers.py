from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Question, LinkClick

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user 
    

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["question", "answer", "date"]
        extra_kwargs = {"answer": {"read_only": True}}


class LinkClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["link_clicked", "date"]
    

    

