from .models import *
from rest_framework import serializers
from django.core.exceptions import ValidationError



class Review_serializer(serializers.ModelSerializer):
    # watchlist = WatchList_serializer(many=True,read_only = True)
    class Meta:
        model = Review
        exclude = ['watchlist',]
        #fields = "__all__"



class WatchList_serializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    reviews = Review_serializer(many=True,read_only=True)


    class Meta:
        model = WatchList
        fields = "__all__"

    def validate_name(self,value):
        if len(value) < 2:
            raise ValidationError('too shortt name')
        else:
            return value
        
    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError('not be same')
        else:
            return data
        
    def get_len_name(self,object):
        lenth = len(object.title)
        return lenth

    



class StreamPlatform_serializer(serializers.ModelSerializer):
    # watchlist = WatchList_serializer(many=True,read_only = True)
    watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie_detail')
    class Meta:
        model = StreamPlatform
        fields = "__all__"




