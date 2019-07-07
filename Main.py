
from flask import Flask

from Services import servicesAPI

app = Flask(__name__)

app.register_blueprint(servicesAPI)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
