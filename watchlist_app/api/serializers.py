from rest_framework import serializers
from watchlist_app.models import movie

#NOW WE ARE GOING TO WRTIE MODEL SERIALIZER

class movieSerializer(serializers.ModelSerializer):
    name_length = serializers.SerializerMethodField()

    class Meta:
        model = movie
        fields = '__all__'
    
    def get_name_length(self, object): #THIS 'OBJECT' HAS ACCESS TO ALL OUR MODEL FIELDS
        length = len(object.name)
        return length

    def validate(self, data): #OBJECT LEVEL VALIDATION
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title & Description should not be same!")
        else:
            return data


    def validate_name(self, value): #FIELD LEVEL VALIDATION ON THE FIELD 'name'
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        else:
            return value


# class movieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     is_active = serializers.BooleanField()
# #TILL NOW, WE'VE CREATED A SERIALIZER THAT WILL MAP ALL THE VALUES

#     def create(self, validated_data):
#         return movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance
    
#     def validate(self, data): #OBJECT LEVEL VALIDATION
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title & Description should not be same!")
#         else:
#             return data


#     def validate_name(self, value): #FIELD LEVEL VALIDATION ON THE FIELD 'name'
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value