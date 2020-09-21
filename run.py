from flask import Flask
from database.database import db
from database.database import migrate
from user_api.views.user_views import app_user
# from app_jobs.views.jobs_views import app_jobs
# from app_schooling.views.schooling_views import app_schooling

app = Flask(__name__)
app.config.from_object('settings')
db.init_app(app)
migrate.init_app(app,db)

app.register_blueprint(app_user)
# app.register_blueprint(app_jobs)
# app.register_blueprint(app_schooling)

app.run()