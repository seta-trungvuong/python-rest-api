from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Category, Post, Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class UserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ["url", "username", "email", "groups", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
            groups=validated_data["groups"],
        )
        # user.groups.set()
        user.set_password(validated_data["password"])
        user.save()
        # Token.objects.create(user=user)
        return user


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=True)
    posts = PostSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = "__all__"
