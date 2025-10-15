from rest_framework import serializers 
from api.models import Student

# Regular Serializer 
# def validation(value): 
#     if value > 0 : 
#         raise serializers.ValidationError("Value should be < 50")

# class StudentSerializer(serializers.Serializer) : 
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField(validators=[validation])
#     city = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save() 
#         return instance 
    
#     def validate_roll(self, val) : 
#         if (val < 0) : 
#             raise serializers.ValidationError("Invalid roll number")
#         return val 
    
#     def validate(self, obj) : 

#         nm = obj.get('name')
#         roll = obj.get('roll')

#         if nm == 'Sameer' and roll == 48 : 
#             raise serializers.ValidationError("Already Exist")
        
#         return obj 



def validation(value): 
    if value > 0 : 
        raise serializers.ValidationError("Value should be > 0")
# Model Based Serializer  
class StudentSerializer(serializers.ModelSerializer) : 

    # name=serializers.CharField(read_only=True)
    roll = serializers.IntegerField(validators=[validation])
    class Meta : 
        model = Student 
        fields = '__all__'

        # read only validation 
        # read_only_fields=['name', 'roll']

    # Field Level Validation 
    def validate_roll(self, val) : 
        if val > 100 : 
            raise serializers.ValidationError("Value Should be < 100")
        return val 
    
    def validate(self, attrs) : 
        nm = attrs.get('name')
        roll = attrs.get('roll')

        if nm == 'Sameer'  : 
            raise serializers.ValidationError("Already Exist")
        return attrs 