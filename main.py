from flask import Flask, render_template
from routes import routes
from scheduler import start_scheduler

app = Flask(__name__)
app.register_blueprint(routes)

@app.route("/")
def index():
    return render_template("login.html") 

if __name__ == "__main__":
    start_scheduler()
    app.run(debug=True)

