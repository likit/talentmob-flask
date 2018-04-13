import os

from app import create_app
from config import app_config


app = create_app(app_config[os.getenv('FLASK_CONFIG', default='development')])

from main import mainbp as main_blueprint
app.register_blueprint(main_blueprint)

from articles import article_bp as article_blueprint
app.register_blueprint(article_blueprint)

if __name__ == '__main__':
    app.run(debug=True)