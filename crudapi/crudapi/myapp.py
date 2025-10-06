import requests 
import json 

URL = "http://127.0.0.1:8000/student_api/" 

def get_data(id = None) : 
    params = {'id' : id} if id is not None else {} 
    print(params)
    r = requests.get(url=URL, params=params) 
    print(r.json()) 

# get_data(3) 

def create_data() : 
    params = {
        'name' : 'Sameer Jugno', 
        'roll' : 4848, 
        'city' : 'Lahore'
    }
    print(params)
    json_data = json.dumps(params) 
    print(json_data)
    response = requests.post(url=URL, json = params)
    print(response.json()) 

# create_data() 

def update_data() : 
    data = {
        'id' : 2,
        'name' : 'Sarfraz Khan', 
        'roll' : 138 , 
        'city' : 'Kabul'
    }

    json_data = json.dumps(data) 
    response = requests.put(URL, data = json_data) 
    print(response.json()) 

# update_data() 

def delete_data() :
    data = {'id' : 4} 
    # json_data = json.dumps(data)
    response = requests.delete(URL, json = data) 
    print(response.json()) 

delete_data() 