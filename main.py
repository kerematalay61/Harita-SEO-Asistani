from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Harita SEO Asistanı Sistemi Aktif!"

if __name__ == "__main__":
    app.run(debug=True)
from routes import routes
app.register_blueprint(routes)
from scheduler import start_scheduler
start_scheduler()
