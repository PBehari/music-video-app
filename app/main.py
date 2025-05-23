# Import packages
from flask import Flask, render_template, request

# Import our custom API method
from api.music_video import get_api_data

# Import utils
from utils.filter import filter_data
from  utils.sorting import Sorting


# Initialise Flask
app = Flask(__name__)

# Route Decorator
@app.route("/")
def index():
    # Get Query params
    action = request.args.get("action")
    key = request.args.get("key")
    val = request.args.get("val")
    sort_order = request.args.get("dir", "asc")

    # Call API method
    data = get_api_data()

    # Apply filter on the data
    if action and action == "filter":
        data = filter_data(data, filter_key=key, filter_val=val)

    # Apply sorting on the data
    if action and action == "sorting":
        # Initialise sorting util
        sorting_util = Sorting()

        # Apply sorting on the data
        reverse = False if sort_order == 'asc' else True
        data = sorting_util.sort_data(data, sort_by=key, reverse=reverse)


    return render_template("index.html", items=data)

# Start the webserver
if __name__ == "__main__":
    app.run(debug=True)
