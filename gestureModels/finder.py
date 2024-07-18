import requests

# Finding a Github repository
url = "https://api.github.com/search/repositories"

query = "gesture recognition"

# Searches Github repositories for query in order of popularity
params = {
    "q": query,
    "sort": "stars",
    "order": "desc"
}

# GET request
response = requests.get(url, params=params)
         
if response.status_code == 200:
    data = response.json()
    # Gets the basic name and url of the chosen repository
    for repo in data["items"]:
        print(f"Name: {repo['name']}")
        print(f"URL: {repo['html_url']}")
else:
    print("request failed")

# Running this gives me this model: https://github.com/SparshaSaha/Hand-Gesture-Recognition-Using-Background-Elllimination-and-Convolution-Neural-Network
# which I will be using since it is well documented and has an accuracy of 95% from the README.

# I have modified ContinuousGesturePredictor.py (I added code at the very bottom under
# Refactored code) and I have also added a new file called flaskTesting.py

