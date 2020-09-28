# Desafio da Empresa Pública, em parceria com a empresa ProWay.

Esse pequeno sistema foi desenvolvido com o objetivo de permitir que pessoas cadastradas possam lançar as pontuações de suas partidas de basquete, e ao final tenham acesso a uma listagem conforme o rank das partidas cadastradas.

Para tal foram selecionadas as seguintes técnologias:

* [Python-Flask] Foi se utilizada a linguagem python tanto por ser robusta e eficiente, quanto pelo microframework Flask ser bastante eficiente, e possuir fácil manutenção em vista de sua leve curva de aprendizado.

* [RM - Flask-SQLAlchemy] Foi utilizado o ORM SQLAlchemy em sua versão integrada com o Flask, para que se tivesse uma separação da camada de dados do banco da codificação, permitindo dessa forma que possamos modificar o banco utilizado conforme desejado (Como pode ser observado no campo settings, onde se tem encaminhamento para um banco de dados MySQL e PostgreSQL).

* [Banco de Dados Postgresql] Como dito anteriormente, com o ORM a seleção pelo banco de dados se tornou secundário, neste caso selecionei o postgresql por conta da hospedagem gratuíta utilizada. Caso se tenha acesso a um banco mysql ou de outro baseado em linguagem SQL, basta alterar os dados de conexão do mesmo.

* [Frontend - Boostrap] Caractéristicas do framework para frontend Bootstrap foram utilizadas para garantir uma melhor visualização e maior harmonia das paginas, dessa forma garantindo uma melhor qualidade visual.

* [Deploy - Heroku] Atualmente esse projeto se encontra para acesso na rede através do endereço abaixo:
 ```basketball-publica.herokuapp.com```

Como foi utilizada a opção de conta de desenvolvimento por Hobby (gratuita), isso faz com que possa ter algumas limitações (até 20 acessos simultaneos, 600 Minutos de conexão por dia).
Observar que existe uma marcação no arquivo main.py onde definimos a configuração a endereço e porta necessários para rodar no Heroku. Para ativar/desativar o mesmo basta comentar esse pedaço, ou retirar o comentário - e comentar a parte de rodar local.

## Requisitos para rodar o projeto de forma Local:

Para rodar o projeto de forma local é necessário se possuir ao menos o Python instalado, em versão 3.8 ou maior, versões inferiores mas acima do 3 podem vir a funcionar, porém pode haver dependencias e falhas nos mesmos.

Atualmente o banco utilizado é uma base PostgreSQL disponível online através do site heroku, porém caso se deseje configurar uma de forma local, basta se instalar a base apropriada (atentar que o projeto traz conectores para banco MySQL -pymysql- e para PostgreSQL -psycopg2), e rodar o arquivo para configurar a base inicial correspondente (mysql_init_db ou postgresql_init_db).

Para se baixar o arquivo diretamente do git pode se utilizar o comando abaixo:
 ``` git clone https://github.com/VitorinoAssuncao/basket.git ```
 GitHuble CLI
 ``` gh repo clone VitorinoAssuncao/basket ```

Ou simplesmente acessando  a pagina e selecionando a opção de preferencia para download.

### Instalando os requisitos e acessando o ambiente virtual:

Caso já tenha usado ambientes virtuais, deverá seguir o processo de criação comum ao mesmo, caso nunca tenha feito isso em python é questão de alguns comandos simples:

Em seu terminal python digitar a seguinte linha de comando:
 ``` virtualenv dev_env ```

Com isso será criada uma nova pasta em seu ambiente com uma estrutura base do python e o instalador pip, após isso é necessário se acionar o ambiente virtual com o seguinte comando:
 ``` dev_env\Scripts\activate```
    *Note que esse comando deverá ser feito da pasta anterior ao dev_env, seja ela raiz ou não.*

Feito isso, basta rodar o seguinte comando que o instalador do python irá instalar todas as dependências deste projeto:
 ```pip install -r requirements.txt```

## Estruturas Relevantes:

Este projeto consiste de duas mini-aplicações que trabalham em momentos específicos:

*[user_api] Esta é a estrutura responsável por cadastro de usuários, seu login e verificações necessárias, assim como integrações futuras com novas estruturas. É essêncial e o passo inicial da aplicação, em vista que é necessário se ter um usuário para poder lançar os jogos.

*[basketball_api] Esta é a estrutura responsável pelos cadastros de partidas, controle de informações das partidas, assim como a visualização do rank por temporada, para poder funcionar apropriadamente é preciso que a varíavel de ambiente "user_id" esteja preenchida, de forma que o sistema sempre saiba qual o usuário que está mexendo na pagina.

## EndPoints

Neste projeto alguns endpoints estão criados, porém fora de uso em vista de que não possuem uma tela, ou uso imediato (como users.getall que permitiria pegar todos os usuários no sistema, ideal para uma futura tela de administração, porém atualmente comentada e assim desativada), porém os ativos estão todos ligados a páginas e eventos especificos, sendo os principais abaixo:

``` "/" : A rota raiz atualmente do sistema leva para a tela de login de usuários, de forma a deixar que este é o primeiro passo para outras áreas do sistema. Em caso de acessar a opção de cadastro ("/users/registry") ao termino do mesmo o usuário será levado imediatamente para a parte interna do sistema.```

```"/users/<id>": pegando o ID da sessão, essa rota é que carregará as informações principais do usuário.```

```"/games": pagina de origem para o cadastro de novos jogos, ao termino do registro da mesma irá levar o usuário a confirmar os dados ("/games/<game_id>")```

```"/game_user/<user_id>&<seasson>": Rota que carrega os dados para rankeamento de todas as partidas lançadas, para aquela temporada e usuário, tanto rankeamento quanto informações de recorde são computadas em tempo de tela.```