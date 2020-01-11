from application import app
from application.entities.user.user_model import *
from application.blueprint import blueprint


# @app.route('/')
# def index():
#     return "The main page for LMS project"


if __name__ == '__main__':

    # import datetime
    # db.create_all()
    # u = User(
    #     public_id="vasya",
    #
    #     first_name="Vasiliy",
    #     middle_name="Ivanovich",
    #     last_name="Fedorov",
    #
    #     email="vasya@yandex.ru",
    #     password="vasya",
    #     registered_on=datetime.datetime.now(),
    #     admin=False,
    # )
    # print(u)
    # db.session.add(u)
    # db.session.commit()
    print(User.query.all())
    app.register_blueprint(blueprint)
    app.run(debug=True)


