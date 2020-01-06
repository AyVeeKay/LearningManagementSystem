from application import app
from application.entities.user.user_model import *


@app.route('/')
def index():
    return "The main page for LMS project"


if __name__ == '__main__':

    import datetime
    # db.create_all()
    # u = User(
    #     public_id="admin",
    #
    #     first_name="Admin's first name",
    #     middle_name="Admin's middle name",
    #     last_name="Admin's last name",
    #
    #     email="admins_email@gmail.com",
    #     password="admin",
    #     registered_on=datetime.datetime.now(),
    #     admin=True,
    # )
    # db.session.add(u)
    # db.session.commit()
    print(User.query.get(1).password_hash)
    app.run(debug=True)


