from database.database import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key=True)
    user_login = db.Column(db.String,nullable=False)
    user_password = db.Column(db.String,nullable=False)
    user_name = db.Column(db.String,nullable=True)
    user_email = db.Column(db.String,nullable=False)

    def __init__(self,**args):
        super(User,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id' : self.user_id,
            'login': self.user_login,
            'name' : self.user_name,
            'email':self.user_email
        }