from .models import Student
from rest_framework import serializers

# validators
# def start_with_d(value):
#     if value[0].lower() != 'd':
#         raise serializers.ValidationError('Name should be start with D')
#
# class StudentSerializer(serializers.Serializer):
#     #id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100,validators=[start_with_d])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#     def create(self,validated_data):
#        return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#       instance.name = validated_data.get('name',instance.name)
#       instance.roll = validated_data.get('roll',instance.roll)
#       instance.city = validated_data.get('city',instance.city)
#       instance.save()
#       return instance
#
#       # Field level Validation
#
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value
#
#     def validate(self,data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'happy' and ct.lower() != 'gandhinager':
#             raise serializers.ValidationError('City must be  Gandhinagar')
#         return data


# for direct perform crud in postman in rest framework
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.ModelSerializer(read_only=True)
    class Meta:
        model = Student
        fields = "__all__"
        # read_only_fields = ['name','roll']
        # extra_kwargs = {'name':{'read_only':True}}

    def validate_roll(self, value):
      if value >= 200:
        raise serializers.ValidationError('Seat Full')
      return value