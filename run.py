from flask import Flask
from database.database import db
from database.database import migrate
from user_api.views.user_views import app_user
from basketball_api.views.game_views import app_game

app = Flask(__name__)
app.config.from_object('settings')
db.init_app(app)
migrate.init_app(app,db)

app.register_blueprint(app_user)
app.register_blueprint(app_game)

def app_run():
    app.run()