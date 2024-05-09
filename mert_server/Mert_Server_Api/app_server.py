import requests
import json
def serves_fonk():
    url = "http://172.29.29.15:8001/todos/Todos/"
    response = requests.get(url)
    title_list = json.loads(response.text)
    for item in title_list:
        print(item["title"])
        

def title_giris():
    
    serves_fonk()

    json_list = {
        "title":"",
        "description":"",
        "completed": False
    }

    title_veri=input("Type the title you want")
    description=input("Type the description you want")


    json_list["title"] = title_veri
    json_list["description"] = description



    url = "http://172.29.29.15:8001/todos/Todos/"

    x = requests.post(url, json = json_list)
    
    