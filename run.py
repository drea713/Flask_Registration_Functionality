from app import app, db
from app.models import Post, User

@app.shell_context_processor
def make_context():
    return {
        'Post': Post,
        'User': User,
        'db': db
    }