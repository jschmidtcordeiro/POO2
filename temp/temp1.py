import json
import requests #biblioteca para fazer requisições HTTP

class UserDataError(Exception):
    def __init__(self, url, message):
        self.url = url
        self.message = message

    def __str__(self):
        return 'Error: %s at resource from: %s' % (self.message, self.url)


def parseUsersData(data):
    logins = []
    for user in data:
        if "login" not in user.keys():
            raise UserDataError(url, "User login was not received")
        logins.append(user["login"])
    return logins

def computeWinRate(data):
    for player in data:
        try:
            percentage = player['victories'] / player['plays']
            print(f"The player {player['full_name']} has won {percentage}% of the time")
        except Exception as e:
            print(e)

#retorna um JSON com os dados dos usuários
url = "https://raw.githubusercontent.com/grellert/jsonbin/master/players.jso"

res = requests.get(url)
print(res)
if "404" in res:
    print("404 Not Found")

try:
    usersData = json.loads(res.content)
    print(usersData)
    computeWinRate(usersData)
    # parseUsersData(usersData)
except UserDataError as e:
    print(e)


print("The code has reached the end")
