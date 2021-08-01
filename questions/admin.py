from django.contrib import admin
from .models.questionmodel import QuestionModel #Question
from .models.area import Area, QuestionList



class QuestionModelAdmin(admin.ModelAdmin):
    ordering = ('-area',)
    search_fields = ['area', 'tema', ]

#class QuestionAdmin(admin.ModelAdmin):
#    ordering = ('-area',)
#    search_fields = ['area', 'tema', ]

class AreaAdmin(admin.ModelAdmin):
    ordering = ('-area',)
    search_fields = ['area']

admin.site.register(QuestionModel, QuestionModelAdmin)
#admin.site.register(Question)
admin.site.register(Area, AreaAdmin)
admin.site.register(QuestionList)

# Register your models here.
