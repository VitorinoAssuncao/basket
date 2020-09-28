#
Desafio da Empresa Pública, em parceria com a empresa ProWay.

Esse pequeno sistema foi desenvolvido com o objetivo de permitir que pessoas cadastradas possam lançar as pontuações de suas partidas de basquete, e ao final tenham acesso a uma listagem conforme o rank das partidas cadastradas.

Para tal foram selecionadas as seguintes técnologias:

• Python-Flask: Foi se utilizada a linguagem python tanto por ser robusta e eficiente, quanto pelo microframework Flask ser bastante eficiente, e possuir fácil manutenção em vista de sua leve curva de aprendizado.

• ORM - Flask-SQLAlchemy: Foi utilizado o ORM SQLAlchemy em sua versão integrada com o Flask, para que se tivesse uma separação da camada de dados do banco da codificação, permitindo dessa forma que possamos modificar o banco utilizado conforme desejado (Como pode ser observado no campo settings, onde se tem encaminhamento para um banco de dados MySQL e PostgreSQL).

• Banco de Dados Postgresql: Como dito anteriormente, com o ORM a seleção pelo banco de dados se tornou secundário, neste caso selecionei o postgresql por conta da hospedagem gratuíta utilizada. Caso se tenha acesso a um banco mysql ou de outro baseado em linguagem SQL, basta alterar os dados de conexão do mesmo.

• Frontend - Boostrap: Caractéristicas do framework para frontend Bootstrap foram utilizadas para garantir uma melhor visualização e maior harmonia das paginas, dessa forma garantindo uma melhor qualidade visual.

• Deploy - Heroku: Atualmente esse projeto se encontra para acesso na rede através do endereço abaixo:
 >> basketball-publica.herokuapp.com