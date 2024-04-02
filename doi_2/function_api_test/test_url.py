"""
import api_url
import custom_call
import common_utility
import gorest
def test_url():
    url = api_url.GET_URL
    headers = common_utility.get_header()
    c_u = gorest.CREATE_USER
    response = custom_call.call_api_custom("GET", url, headers=headers, status=200)
    json_data = response.json()
    print(json_data)
    print("API success")
    #response = custom_call.call_api_custom("POST",url, headers=headers, r_json=c_u, status=201)
    #print(response.json())
    #print("API success")
test_url()
"""