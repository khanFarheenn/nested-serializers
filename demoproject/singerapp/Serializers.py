from rest_framework import serializers
from .models import Singer, Song



# class SongsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Song
#         fields = ['id', 'title', 'duration']

# class SingersSerializer(serializers.ModelSerializer):
#     songs = SongsSerializer(many=True, read_only=True)

#     class Meta:
#         model = Singer
#         fields = ['id', 'name', 'gender', 'songs']






class SongsSerializer(serializers.ModelSerializer):
    # singer = SingersSerializer()  # Nested Serializer for the Singer
    # singer = SingersSerializer(many=True)  # Nested Serializer for the Singer

    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


# other way to work nested serialzer
class SingersSerializer(serializers.ModelSerializer):
    songs = SongsSerializer(many=True)
    # songs = serializers.SerializerMethodField()
    
 
    # def get_songs(self, obj):
    #     return SongsSerializer(obj.songs.all(), many=True).data

    class Meta:
        model = Singer
        fields = '__all__'
