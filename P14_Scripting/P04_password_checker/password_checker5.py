import requests
import hashlib


def request_api_data(query_char):

    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error feching: {res.status_code}check the api and try again')
    return res

def get_password_leak_count(hashes,has_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == has_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char , tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(response)
    return get_password_leak_count(response,tail)

# password = "jgjjgjg"
password = "qwertyuiop"
count = pwned_api_check(password)

print(f'{password} password found {count} times')
