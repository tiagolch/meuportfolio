# MEUPORTIFOLIO
Um projeto desenvolvido em parceria com intuito de ser open source. Essa idéa surgiu para a criação e edição
de uma pagina a ser utilizada como portfolio ou currículo web.

Os pré-requisitos é Ter instalado Python 3+, pip e instalar o requirements do projeto.

`pip install -r requirements.txt`

Após instalar, rodar os comando abaixo para criar o banco de dados.

`python manage.py makemigrations`

`python manage.py migrate`

Com o banco de dados criado, crie o superuser para a tela de administração do django. O mesmo irá 
pedir um nome de usuário, e-mail e senha.

`python manage.py createsuperuser`

Por fim basta rodar o projeto.

`python manage.py runserver`
