import requests

def len_joke():
    joke = get_joke()
    print()
    print('The joke from get_joke():', joke)
    print()

    return len(joke)

def get_joke():
    url = 'http://api.icndb.com/jokes/random'

    print()
    print(type(requests.exceptions.Timeout))
    print()

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        return 'No jokes'
    except requests.exceptions.ConnectionError:
        return 'ConnectionError was raised'
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code

        if status_code in [503, 504]:
            pass
        else:
            pass
        return 'HTTPError was raised'

    else:
        if response.status_code == 200:
            joke = response.json()['value']['joke']
        else:
            joke = 'No jokes'
    return joke

if __name__ == '__main__':
    print(get_joke())