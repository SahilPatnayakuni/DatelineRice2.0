import requests

address = 'https://people.api.rice.edu/v1.0/people/'
def matches(first_name, last_name, num_retry):
    url = address + last_name + '/' + first_name
    r = requests.get(url)
    jr = r.json()

    # Currently it is failing on valid request
    # Will retry a certain amount of times

    if jr['success'] == False:
        if num_retry > 0:
            # Potentially should log here if retrying
            print("Unsuccessful, retrying request")
            return matches(first_name, last_name, num_retry - 1)
        else:
            return jr
    else:
        return jr


# Initial Testing
print(matches("Harrison", "Brown", 3))
