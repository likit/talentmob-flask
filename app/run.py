import os

from main import create_app
from config import app_config


app = create_app(app_config[os.getenv('FLASK_CONFIG')])

from main import mainbp as main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)