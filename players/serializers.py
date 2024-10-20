from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Player, Profile, FavoritePlayer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar']

class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar_url']

    def get_avatar_url(self, obj):
        if hasattr(obj, 'profile') and obj.profile.avatar:
            return obj.profile.avatar.url
        return None

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate

        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")

class PlayerSerializer(serializers.ModelSerializer):
    favourite = serializers.SerializerMethodField()
    avatar_url = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Player
        fields = '__all__'

    def get_favourite(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            return FavoritePlayer.objects.filter(user=request.user, player=obj).exists()
        return False

class FavoritePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePlayer
        fields = ['id', 'user', 'player', 'added_at']
        read_only_fields = ['added_at']