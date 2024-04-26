import requests
import pytest
def call_api_custom(method, url, r_json = None, headers = None, status = None):
    response = requests.request(method, url,json = r_json,headers= headers)
    try:
        assert response.status_code == status, f"API ERROR, status code is {response.status_code}"
        return response
    except:
        pytest.fail("API ERROR")
        # nếu điều kiện không đúng, nó sẽ ghi nhận testcase thất bại với thông điệp "API ERROR"
        # và nếu có bất kỳ ngoại lệ nào xảy ra trong quá trình kiểm tra, nó cũng sẽ ghi nhận testcase thất bại với thông điệp

