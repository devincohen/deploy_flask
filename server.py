from flask_app import app
# ...server.py
from flask_app.controllers import site_users

from flask_app.models.site_user import Site_User

if __name__ == '__main__':
    app.run(debug = True)