# kịch bản test hoạt động của 4 phương thức: GET, POST, PUT, DELETE

import pytest
import api_url
import custom_call
import common_utility
import file
id = None


def test_get():
    url = api_url.GET_URL
    headers = common_utility.get_header()
    response = custom_call.call_api_custom("GET", url, headers=headers, status=200)
    assert response.status_code == 200
    print(response.json())
    print("API success")
    file.write_file("C:\\api-testing\\config\\start.json",response.json())


def test_post():
    url = api_url.GET_URL
    headers = common_utility.get_header()
    c_u = file.read_file("C:\\api-testing\\config\\create.json")
    c_u["email"] = common_utility.get_email()
    response = custom_call.call_api_custom("POST", url, headers=headers, r_json=c_u, status=201)
    re_json = response.json()
    assert response.status_code == 201
    global id
    id = re_json["id"]
    print(re_json)
    print("API success")


def test_put():
    global id
    url = api_url.GET_URL + f"/{id}"
    headers = common_utility.get_header()
    c_u = file.read_file("C:\\api-testing\\config\\update.json")
    response = custom_call.call_api_custom("PUT", url, headers=headers, r_json=c_u, status=200)
    assert response.status_code == 200
    print(response.json())
    print("API success")


def test_delete():
    global id
    url = api_url.GET_URL + f"/{id}"
    headers = common_utility.get_header()
    response = custom_call.call_api_custom("DELETE", url, headers=headers, status=204)
    assert response.status_code == 204
    print("API success")