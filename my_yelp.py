import requests

api_key = "K2GTgs7ZgRQEXZ2_9BzfZO6pg_ijOuZ3vwG8fCljHGTmLrmU00fR5R8EEFHmH6qrzHg06BrXzIZ224bNL3qnwC7R4Sefmg6mwQUNaqt8fpyZvx2l_5JwKkuDythVXHYx"

url = "https://api.yelp.com/v3/businesses/search"

my_headers = {
    "Authorization": "Bearer %s" % api_key
}

my_params = {
    "term": "restaurants",
    "location": "chicago",
    "limit": 3,
}

businesses_object = requests.get(url, headers=my_headers, params=my_params)

#print(businesses_object)

businesses_dict = businesses_object.text

print(businesses_dict)

#print(businesses_dict)
