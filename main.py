import requests
import csv
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
    
# Read users info from csv file
def get_user_info(file_path:str)->dict:
    users = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header
        next(csv_reader)
        for row in csv_reader:
            users.append(
                {
                    'full_name': row[1],
                    'username': row[2],
                }
            )
    return users
    


users = get_user_info('monkeytype.csv')
print(users)
# print(get_wpm_accuracy(username,15))