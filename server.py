from flask_app import app
from flask_app.controllers import characters, controller_user, controller_content

if __name__ == "__main__":
    app.run(debug=True)