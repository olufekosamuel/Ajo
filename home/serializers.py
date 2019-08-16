from rest_framework import serializers
from .models import AjoGroup, AjoMembers, AjoGenerator
from rest_framework.validators import UniqueValidator

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjoGroup
        fields = ('id','admin', 'name', 'description', 'amount', 'capacity',)

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjoMembers
        fields = '__all__'

class GeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjoGenerator
        fields = '__all__'

class AcceptorSerializer(serializers.Serializer):
    uid = serializers.CharField()