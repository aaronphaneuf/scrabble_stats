from email.headerregistry import DateHeader
from rest_framework import serializers
from .models import Game, User, Word
from django.db.models.aggregates import Sum
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from collections import Counter, defaultdict
import datetime

class UserSerializer(serializers.ModelSerializer):
    #words = serializers.SerializerMethodField()
    test = serializers.SerializerMethodField()
    class Meta:
        
        model = User
        fields = ['id', 'name', 'email','test']#,'words']

    def get_test(self, obj):
        data = WordSerializer(obj.letter, many=True).data
        #data = 'hi'
        return data

    # def get_words(self, obj):
    #     x = WordSerializer(obj.player, many=True).data
    #     #print(x[1]['game'])
    #     return x

class WordSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(source='player.name')
    winner = serializers.CharField(source='game.winner')
        
    class Meta:
        
        model = Word
        fields = ['game', 'winner', 'turn', 'player', 'player_name', 'word', 'score']

        def __str__(self):
            return str(self.player.name)

class CreateWordSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Word
        fields = ['game', 'turn', 'player', 'word', 'score']

class CreateGameSerializer(serializers.ModelSerializer):
    #words = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()
    test = serializers.SerializerMethodField()

    class Meta:
        
        model = Game
        fields = ['player', 'users', 'test']

    def get_users(self, obj):
        x = UserSerializer(obj.user, many=True).data
        #print(x[1]['game'])
        return x

    def get_test(self,obj):
        print('hello!')
        return 'hello'
    
    # def get_words(self, obj):
    #     x = WordSerializer(obj.word, many=True).data
    #     #print(x[1]['game'])
    #     return WordSerializer(obj.word, many=True).data
   

    

class GameSerializer(serializers.ModelSerializer):
    
    
    #word2 = serializers.RelatedField(source='game.score', read_only=True)
    data = serializers.SerializerMethodField(read_only=True)
    #x = serializers.SerializerMethodField(read_only=True)
    player_names = serializers.SerializerMethodField(read_only=True)
    test = serializers.SerializerMethodField()
    game_score = serializers.SerializerMethodField()
    player_array = serializers.SerializerMethodField()

    
    #words = WordSerializer(many=True, read_only=True)
    

    #user_name= serializers.ReadOnlyField(source='user.name')
    
    #player = serializers.SlugRelatedField(slug_field='score', queryset=Word.objects.all())

    #category_name = ReadOnlyField(source='game.score')
    

    #data = WordSerializer(read_only=True)
    class Meta:
        
        
        model = Game
        fields = ['id','player', 'player_array', 'date' ,'data' , 'player_names', 'test', 'game_score'] #'total_score']#'user_name'] #'player']#,'category_name']#, 'words']# 'users']
        
    def get_data(self, obj):
        x = WordSerializer(obj.word, many=True).data
        #print(x[1]['game'])
        return WordSerializer(obj.word, many=True).data

    def get_player_names(self, obj):
        data = WordSerializer(obj.word, many=True).data
        
        names = []
        for i in data:
            names.append(i['player_name'])
        
        names = sorted(set(names), key=names.index)
        
        return names

    def get_test(self,obj):
        data = WordSerializer(obj.word, many=True).data
        result = defaultdict(int)
        for d in data:
            result[d['player']] += int(d['score'])
        [{'player': player, 'score': score} for player, score in result.items()]
        
        return result

    def get_game_score(self,obj):
        data = WordSerializer(obj.word, many=True).data
        result = defaultdict(int)
        for d in data:
            result[d['player']] += int(d['score'])
        [{'player': player, 'score': score} for player, score in result.items()]
        x = sum(result.values())
        return x

    def get_player_array(self, obj):
        return UserSerializer(obj.player, many=True).data



        
       


    # def get_total_score(self, obj):
    #     qs = Word.objects.filter(player=1, game=obj)
    #     x = Word.objects.all().annotate(total_score=Sum('word__score'))
    #     print(x)
    #     serializer = WordSerializer(instance=x,many=True)
        
    #     print(serializer)
    #     return serializer.data
        
   
    

    
        

   

    #products_count = serializers.IntegerField(read_only=True)


    

    #total_score = serializers.SerializerMethodField(method_name='total_score')
    
    #total_score = serializers.CharField(source='player.game')
    
    #player = Word.objects.all().order_by('score')
    #score_count = serializers.IntegerField(read_only=True)
   
    #def calculate_tax(self, game: Game):
        #return game.id + 5
        
       
