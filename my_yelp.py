#Maintainer Qamber Mehdi
# Created on August 25, 2018

import requests, json

def search_businesses(search_term, search_location):

    api_key = "K2GTgs7ZgRQEXZ2_9BzfZO6pg_ijOuZ3vwG8fCljHGTmLrmU00fR5R8EEFHmH6qrzHg06BrXzIZ224bNL3qnwC7R4Sefmg6mwQUNaqt8fpyZvx2l_5JwKkuDythVXHYx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = json.loads(businesses_object.text)

    businesses_list = businesses_dict['businesses']
    #
    list_of_businesses = []
    for each in businesses_list:
        list_of_businesses.append(each)
    return list_of_businesses
