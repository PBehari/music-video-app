# Import packages
import requests

# methods
def get_api_data():
    # Make call to API url
    response = requests.get(url="https://openwhyd.org/hot/electro?format=json", timeout=10)
    # Get response in JSON format
    results = response.json()

    # Check if "tracks" field is available in the response
    if "tracks" in results:
        for result in results.get("tracks", []):
            yield {
                "name": result.get("name"),
                "image": result.get("img"),
                "track_url": result.get("trackUrl"),
                "score": result.get("score"),
            }

    yield {}
