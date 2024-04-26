# kịch bản test với trường hợp thừa thiếu và sai param khi POST
#kịch bản test với trường hợp sai và thừa param khi PUT

import pytest
import api_url
import custom_call
import common_utility
import file
id = None
c = None
u = None

@pytest.fixture(params=[
    file.read_file("C:\\api-testing\\config\\c_p_d.json"),# post thừa
    file.read_file("C:\\api-testing\\config\\c_p_t.json"),# post thiếu
    file.read_file("C:\\api-testing\\config\\c_p_s.json") # post sai
])
def param_error1(request):
    global c 
    c = request.param
    return c

@pytest.fixture(params=[
    file.read_file("C:\\api-testing\\config\\u_p_d.json"),# update thừa
    file.read_file("C:\\api-testing\\config\\u_p_s.json") # update sai
])

def param_error2(request):
    global u
    u = request.param
    return u

def test_post_param(param_error1):
    url = api_url.GET_URL
    headers = common_utility.get_header()
    c = param_error1
    c["email"] = common_utility.get_email()
    response = custom_call.call_api_custom("POST", url, headers=headers, r_json=c, status=201)
    re_json = response.json()
    assert response.status_code == 201
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


def test_put_param(param_error2):
    global id
    id = post()
    url = api_url.GET_URL + f"/{id}"
    headers = common_utility.get_header()
    u = param_error2
    response = custom_call.call_api_custom("PUT", url, headers=headers, r_json=u, status=200)
    assert response.status_code == 200
    print(response.json())
    print("API success")

