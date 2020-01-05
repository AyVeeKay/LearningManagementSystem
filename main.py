from application import app


@app.route('/')
def index():
    return "The main page for LMS project"


if __name__ == '__main__':
    app.run(debug=True)
