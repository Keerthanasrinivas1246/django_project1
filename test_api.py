import requests

response = requests.get("http://127.0.0.1:8000/api/api/")      #api data in stored

if response.status_code == 200:
    data = response.json()

    for i in data:
        print(f"ID : {i['id']}")
        print(f"Male : {i['male']}")
        print(f"Female : {i['female']}")
        print(f"Relationship Status : {i['relationship_status']}")
        print(f"Common Interest : {i['common_interest']}")
        print(f"Favourite Spots : {i['fav_spots']}")
        print("-" * 50)
else:
    print("failed to fetch data.")
