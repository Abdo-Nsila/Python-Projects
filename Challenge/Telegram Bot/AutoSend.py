import requests

TOKEN = '6332606855:AAGT8fy3H6npQ9x7aKYqEppIM3EhjirwZjE'
CHAT_ID = 1892665321

files = {'photo': open('C:\\Users\\aa\\Downloads\\fire.jpg', 'rb')}

response = requests.post(
    f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}',
    files=files
)

print(response.status_code)
