import requests

address = 'https://people.api.rice.edu/v1.0/people/'
def matches(first_name, last_name):
    url = address + last_name + '/' + first_name
    r = requests.get(url)
    jr = r.json()
    return jr


