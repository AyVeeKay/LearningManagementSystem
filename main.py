from application import app
from application.blueprint import blueprint


if __name__ == "__main__":
    app.register_blueprint(blueprint)
    app.run(debug=True)


