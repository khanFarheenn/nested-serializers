from rest_framework import serializers
from .models import Singer, Song


# class SongsSerializer(serializers.ModelSerializer):
#     # singer = serializers.PrimaryKeyRelatedField(read_only=True)  # Assuming each song has one singer
#     singer = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='singer-detail'
#     )

#     class Meta:
#         model = Song
#         fields = ['id', 'title', 'singer', 'duration']


class SongsSerializer(serializers.ModelSerializer):
    singer = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='singer-list'
    )

    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']
# other way to work nested serialzer
class SingersSerializer(serializers.ModelSerializer):
    songs = SongsSerializer(many=True, read_only=True)  # This line will nest song data within each singer.

    class Meta:
        model = Singer
        fields = '__all__' 