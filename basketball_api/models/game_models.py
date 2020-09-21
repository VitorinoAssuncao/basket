from database.database import db

class Game(db.Model):
    __tablename__ = 'games'
    game_id = db.Column(db.Integer,primary_key=True)
    game_user_id = db.Column(db.Integer,nullable=False)
    game_number = db.Column(db.Integer,nullable=False)
    game_seasson = db.Column(db.Integer,nullable=False)
    game_points = db.Column(db.Integer,nullable=False)

    def __init__(self,**args):
        super(Game,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id' : self.game_id,
            'user_id': self.game_user_id,
            'number' : self.game_number,
            'seasson':self.game_seasson,
            'points':self.game_points
        }