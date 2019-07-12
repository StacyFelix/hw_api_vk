import requests


class User:
    token = '0f84be2b38b217e91846b66deeedfa9782f3c03105ecbe971aca0bb4d20205862aef8e3c31659c019e5ce'

    def __init__(self, user_id):
        # self.token = token
        self.user_id = user_id

    def get_params(self):
        return {
            'access_token': self.token,
            'v': '5.52'
        }

    def get_list_friends(self):
        URL_API_VK = 'https://api.vk.com/method/friends.get'
        params = self.get_params()
        params['user_id'] = self.user_id
        response = requests.get(URL_API_VK, params=params)
        return response.json()["response"]['items']

    def __and__(self, other):
        list_friends_1 = self.get_list_friends()
        list_friends_2 = other.get_list_friends()

        list_id_common_friends = list(set(list_friends_1).intersection(list_friends_2))
        # return list_id_common_friends
        list_common_friends = []
        for id in list_id_common_friends:
            list_common_friends.append(User(id))
        return list_common_friends

    def __str__(self):
        return f"https://vk.com/id{str(self.user_id)}"


user_381175355 = User(381175355)
user_3944540 = User(3944540)

print(user_381175355.__and__(user_3944540))
print(user_381175355 & user_3944540)
print(user_381175355)
print(user_3944540)