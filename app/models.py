from app import db
from datetime import datetime as dt
from app import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(250))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def create_password_hash(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, current_password):
        return check_password_hash(self.password, current_password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# HASHING AND SALTING

# lucas-hash
# derek-hash

# HASHING
# password = abc123
# translation => er7p98789arhuo8bozufjn2

# SALTING
# real password for password 1 = abc123
# original = er7p98789arhuo8bozufjn2
# salt = 2q480we89b801dfuuoijsriodfuo

# real password for password 2 = abc123
# original = er7p98789arhuo8bozufjn2
# salt = 84yar8h90fd9n80uO2YAH09

# REAL_PASSWORD = ABC123
# salt = 84yar8h90fd9n80uO2YAH09