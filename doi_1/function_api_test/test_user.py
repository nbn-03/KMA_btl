import pytest
import api_url
import custom_call
import common_utility
import file


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
    c_u = file.read_file_c()
    c_u["email"] = common_utility.get_email()
    response = custom_call.call_api_custom("POST", url, headers=headers, r_json=c_u, status=201)
    re_json = response.json()
    assert response.status_code == 201
    file.update_file_c(re_json)
    print(re_json)
    print("API success")


@pytest.mark.put_user
def test_put_user():
    data = file.read_file_c()
    id = data["id"]
    url = api_url.GET_URL + f"/{id}"
    headers = common_utility.get_header()
    c_u = file.read_file_u()
    response = custom_call.call_api_custom("PUT", url, headers=headers, r_json=c_u, status=200)
    assert response.status_code == 200
    print(response.json())
    file.update_file_c(response.json())
    print("API success")

@pytest.mark.delete_user
def test_delete_user():
    data = file.read_file_c()
    id = data["id"]
    url = api_url.GET_URL + f"/{id}"
    headers = common_utility.get_header()
    response = custom_call.call_api_custom("DELETE", url, headers=headers, status=204)
    assert response.status_code == 204
    print("API success")