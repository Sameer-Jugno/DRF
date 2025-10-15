from rest_framework import serializers 
from api.models import Student
class StudentSerializer(serializers.Serializer) : 
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save() 
        return instance 
    
    def validate_roll(self, val) : 
        if (val < 0) : 
            raise serializers.ValidationError("Invalid roll number")
        return val 
    
    def validate(self, obj) : 
        nm = obj.get('name')
        roll = obj.get('roll')

        if nm == 'Sameer' and roll == 48 : 
            raise serializers.ValidationError("Already Exist")
        
        return obj 