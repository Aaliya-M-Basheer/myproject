import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users")

# print(response.status_code)
# print(response.json())

# def test_get_users():

#     response = requests.get(
#         "https://jsonplaceholder.typicode.com/users"
#     )

#     assert response.status_code == 200


import requests

def test_get_users():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    data = response.json()

    assert response.status_code == 200
    assert len(data) > 0
    