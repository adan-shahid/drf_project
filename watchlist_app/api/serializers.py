from rest_framework import serializers

class movieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()
#TILL NOW, WE'VE CREATED A SERIALIZER THAT WILL MAP ALL THE VALUES