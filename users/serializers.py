from .models import Profile
from rest_framework import serializers

class UserSeri(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model=Profile
        fields=['user', 'location', 'image']