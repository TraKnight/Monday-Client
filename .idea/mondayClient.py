import requests



class Monday():

    def __init__(self,api,board):
        self.api=api
        self.board=board
        query = '{boards (ids:'+board+'){name id columns{title id} groups{id title}  items{name id subscribers{id name}column_values{id text} }}}'
        data={'query':query}
        self.request(self.api)

    #creates json file for Monday request
        with open('mondayDict.json','w') as file_:
         print("file Created")

    def request(self,auth):
        headers= {"Authorization":auth}
        request= requests.get(url=self.api, json=self.data,headers=headers)









