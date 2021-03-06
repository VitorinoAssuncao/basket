import os
from flask import Flask
from database.database import db
from database.database import migrate
from app.user_api.views.user_views import app_user
from app.basketball_api.views.game_views import app_game

app = Flask(__name__)
app.config.from_object('settings')
db.init_app(app)
migrate.init_app(app,db)

app.register_blueprint(app_user)
app.register_blueprint(app_game)

# Configuração para rodar a aplicação diretamente via heroku

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# Configuração para rodar a aplicação de forma local
# app.run()