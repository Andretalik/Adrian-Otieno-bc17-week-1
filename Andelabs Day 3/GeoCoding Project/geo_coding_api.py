import requests

# https://maps.googleapis.com/maps/api/geocode/json?address=nairobi&key=AIzaSyBP46knHGvg5jxJkrgsGLUdwd5DzdTltno
google_api = 'key=AIzaSyBP46knHGvg5jxJkrgsGLUdwd5DzdTltno'


def geocode_search(term):
    api_key = google_api
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    address_term = term.replace(' ', '+')
    final_url = url + "address=" + address_term + "&" + api_key
    json_object = requests.get(final_url)
    data = json_object.json()
    # decoded_data = json.load(data)
    # print(data["results"][0]["geometry"]["location"].keys())
    # print(len(data["results"]))

    print("Latitude: ", data["results"][0]["geometry"]["location"]["lat"], ", ","Longitude", data["results"][0]["geometry"]["location"]["lng"] )
