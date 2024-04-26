# kịch bản test POST trùng id, trùng email, sai định dạng email 

import pytest
import api_url
import custom_call
import common_utility
import file
c_u = None

@pytest.fixture(params=[
    file.read_file("C:\\api-testing\\config\\c_d_id.json"),# post trùng id
    file.read_file("C:\\api-testing\\config\\c_d_email_1.json"),# post trùng email
    file.read_file("C:\\api-testing\\config\\c_d_email_2.json") # post sai định dạng email
])
def data_error(request):
    global c_u
    c_u = request.param
    return c_u

def test_post_data(data_error):
    url = api_url.GET_URL
    headers = common_utility.get_header()
    c_u = data_error
    if(c_u == file.read_file("C:\\api-testing\\config\\c_d_id.json")):
        c_u["email"] = common_utility.get_email()
    response = custom_call.call_api_custom("POST", url, headers=headers, r_json=c_u, status=201)
    re_json = response.json()
    assert response.status_code == 201
    print(re_json)
    print("API success")