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
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y')

    def get_data_atualizacao(self):
        return self.data_atualizacao.strftime('%d/%m/%Y')


class SobreMim(models.Model):
    sobremim = models.CharField(max_length=2000, verbose_name='Sobre Mim')

    class Meta:
        verbose_name = 'Sobre Mim'
        verbose_name_plural = 'Sobre Mim'

    def __str__(self):
        return self.sobremim


class RedeSocial(models.Model):
    linkedin = models.CharField(max_length=300, verbose_name='LinkedIn')
    github = models.CharField(max_length=300, verbose_name='GitHub')
    whatsapp = models.CharField(max_length=14, verbose_name='Whatsapp')

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

    def __str__(self):
        return self.linkedin

class CargoPretendido(models.Model):
    cargo = models.CharField(max_length=50, verbose_name='Cargo Pretendido')

    class Meta:
        verbose_name = 'Cargo Pretendido'
        verbose_name_plural = 'Cargos Pretendidos'

    def __str__(self):
        return self.cargo


class Experiencia(models.Model):
    cargo = models.CharField(max_length=25, verbose_name='Cargo')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')
    descricao = models.CharField(max_length=500, verbose_name='Descrição')
    data_inicio = models.DateField(verbose_name='Data de Inicio')
    data_final = models.DateField(blank=True, null=True, verbose_name='Data de fim')
    atual = models.BooleanField(default=False, verbose_name='Atual')

    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiencias'

    def __str__(self):
        return self.cargo

    def get_data_inicio(self):
        return self.data_criacao.strftime('%m/%Y')

    def get_data_final(self):
        return self.data_final.strftime('%m/%Y')
        
