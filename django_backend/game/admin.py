from django.contrib import admin
from game.models import User, Game, Word
from . import models
from django.db.models.aggregates import Sum

#class DateAdmin(admin.ModelAdmin):
#    readonly_fields = ('id', 'date',)



#admin.site.register(User)
#admin.site.register(Game, DateAdmin)
#admin.site.register(Word)


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['game', 'turn', 'player', 'word', 'score']

        

@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'total_score']
    @admin.display(ordering='total_score') 
    def total_score(self, game):
        
        return game.total_score

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            total_score = Sum('word__score')
        )

    
    
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']#, 'total_score']    
    # @admin.display(ordering='total_score') 
    # def total_score(self, user):
        
    #     return user.total_score

    # def get_queryset(self, request):
    #     return super().get_queryset(request).annotate(
    #         total_score = Sum('word__score')
    #     )