import requests

username = 'naxalov'

def get_wpm_accuracy(username:str,time:int)->dict:
    url = f'https://api.monkeytype.com/users/{username}/profile'
    response = requests.get(url)
    # Get the JSON data from the response
    data = response.json()
    time = data['data']['personalBests']['time'][str(time)][0]
    # Get accuracy
    accuracy = time['acc']
    # Get wpm
    wpm = time['wpm']
    return {'wpm':wpm,'accuracy':accuracy}
    
    
print(get_wpm_accuracy(username,15))