# Kịch bản test với trường hợp sai Authorization và không có Authorization
import pytest
import api_url
import custom_call
import common_utility
import file
id = None
id_1 = None
id_2 = None
# Fixture để cung cấp header với authorization sai hoặc không có authorization
@pytest.fixture(params=[
    common_utility.get_header_error1(),  # Trường hợp không có Authorization
    common_utility.get_header_error2()   # Trường hợp Authorization sai
])
def auth_error_header(request):
    return request.param

def test_get_auth(auth_error_header):
    url = api_url.GET_URL
    headers = auth_error_header
    response = custom_call.call_api_custom("GET", url, headers=headers, status=200)
    assert response.status_code == 200
    print(response.json())
    print("API success")


def test_post_auth(auth_error_header):
    url = api_url.GET_URL
    headers = auth_error_header
    c_u = file.read_file("C:\\api-testing\\config\\create.json")
    c_u["email"] = common_utility.get_email()
    response = custom_call.call_api_custom("POST", url, headers=headers, r_json=c_u, status=201)
    re_json = response.json()
    assert response.status_code == 201
    global id
    id = re_json["id"]
    print(re_json)
    print("API success")

def post():
    url = api_url.GET_URL
    headers = common_utility.get_header()
    c_u = file.read_file("C:\\api-testing\\config\\create.json")
    c_u["email"] = common_utility.get_email()
    response = custom_call.call_api_custom("POST", url, headers=headers, r_json=c_u, status=201)
    re_json = response.json()
    assert response.status_code == 201
    global id
    id = re_json["id"]
    return id

def test_put_auth(auth_error_header):
    global id
    global id_1
    global id_2
    if(auth_error_header == common_utility.get_header_error2()):
        id_2 = post()
        id = id_2
    if(auth_error_header == common_utility.get_header_error1()):
        id_1 = 6823549
        id = id_1
    url = api_url.GET_URL + f"/{id}"
    headers = auth_error_header
    c_u = file.read_file("C:\\api-testing\\config\\update.json")
    response = custom_call.call_api_custom("PUT", url, headers=headers, r_json=c_u, status=200)
    assert response.status_code == 200
    print(response.json())
    print("API success")


def test_delete_auth(auth_error_header):
    global id
    global id_1
    global id_2
    if(auth_error_header == common_utility.get_header_error2()):
        id = id_2
    if(auth_error_header == common_utility.get_header_error1()):
        id = id_1
    url = api_url.GET_URL + f"/{id}"
    headers = auth_error_header
    response = custom_call.call_api_custom("DELETE", url, headers=headers, status=204)
    assert response.status_code == 204
    print("API success")