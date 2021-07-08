from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 
                    'sobrenome', 
                    'nome_visualizacao', 
                    'get_data_criacao',
                    'get_data_atualizacao',
                    'ativo']
    list_filter = ['data_criacao',
                   'ativo']
    search_fields = ['nome',
                     'sobrenome',
                     'nome_visualizacao']
    list_per_page = 10
