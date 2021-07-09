from django.db import models

class Pessoa(models.Model):
    nome = models.CharField( max_length=25, verbose_name='Primeiro Nome')
    sobrenome = models.CharField( max_length=25, verbose_name='Sobrenome')
    nome_visualizacao = models.CharField(max_length=50, verbose_name='Nome de Visualização')
    email = models.EmailField(verbose_name='Email')
    imagem_perfil = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pessoa'

    def __str__(self):
        return self.nome

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y')

    def get_data_atualizacao(self):
        return self.data_atualizacao.strftime('%d/%m/%Y')


class SobreMim(models.Model):
    sobremim = models.CharField(max_length=2000, verbose_name='Sobre Mim')

    def __str__(self):
        return self.sobremim

    
class CargoPretendido(models.Model):
    cargo = models.CharField(max_length=50, verbose_name='Cargo Pretendido')

    def __str__(self):

        return self.cargo