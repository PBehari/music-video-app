# Import packages
from flask import Flask, render_template

# Import our custom API method
from api.music_video import get_api_data

# Initialise Flask
app = Flask(__name__)

# Route Decorator
@app.route("/")
def index():
    # Call API method
    data = get_api_data()

    return render_template("index.html", items=data)

# Start the webserver
if __name__ == "__main__":
    app.run(debug=True)
