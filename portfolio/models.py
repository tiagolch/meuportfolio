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

    
<<<<<<< HEAD
class RedeSocial(models.Model):
    linkedin = models.CharField(max_length=300, verbose_name='LinkedIn')
    github = models.CharField(max_length=300, verbose_name='GitHub')
    whatsapp = models.CharField(max_length=14, verbose_name='Whatsapp')

    def __str__(self):
        return self.linkedin
=======
class CargoPretendido(models.Model):
    cargo = models.CharField(max_length=50, verbose_name='Cargo Pretendido')

    def __str__(self):

        return self.cargo
>>>>>>> 999caacb5893fada876a27122d82330667d318b0
