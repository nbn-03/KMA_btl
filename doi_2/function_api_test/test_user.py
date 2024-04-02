import pytest
import api_url
import custom_call
import common_utility
import gorest
id = None

@pytest.mark.get_user
def test_get_user():
    url = api_url.GET_URL
    headers = common_utility.get_header()
    response = custom_call.call_api_custom("GET", url, headers=headers, status=200)
    assert response.status_code == 200
    print(response.json())
    print("API success")

@pytest.mark.post_user
def test_post_user():
    url = api_url.GET_URL
    headers = common_utility.get_header()
    c_u = gorest.CREATE_USER
    c_u["email"] = common_utility.get_email()
    response = custom_call.call_api_custom("POST", url, headers=headers, r_json=c_u, status=201)
    re_json = response.json()
    assert response.status_code == 201
    print(re_json)
    global id
    id = re_json["id"]
    print("API success")


@pytest.mark.put_user
def test_put_user():
    global id
    c_u = gorest.UPDATE_USER
    url = api_url.GET_URL + f"/{id}"
    headers = common_utility.get_header()
    response = custom_call.call_api_custom("PUT", url, headers=headers, r_json=c_u, status=200)
    assert response.status_code == 200
    print(response.json())
    print("API success")

@pytest.mark.delete_user
def test_delete_user():
    global id
    url = api_url.GET_URL + f"/{id}"
    headers = common_utility.get_header()
    response = custom_call.call_api_custom("DELETE", url, headers=headers, status=204)
    assert response.status_code == 204
    print("API success")