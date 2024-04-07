import file
import api_url
import common_utility
import custom_call

def get():
    url = api_url.GET_URL
    headers = common_utility.get_header()
    response = custom_call.call_api_custom("GET", url, headers=headers, status=200)
    assert response.status_code == 200
    print(response.json())
    file.write_file("C:\\api-testing\\config\\end.json",response.json())

def filter():
    s = file.read_ids_from_json("C:\\api-testing\\config\\start.json")
    e = file.read_ids_from_json("C:\\api-testing\\config\\end.json")
    f = [x for x in e if x not in s]
    print(f)
    return f

def delete():
    for id in filter():
        url = api_url.GET_URL + f"/{id}"
        headers = common_utility.get_header()
        response = custom_call.call_api_custom("DELETE", url, headers=headers, status=204)
        assert response.status_code == 204
        print("API success")

def main():
    get()
    filter()
    delete()

if __name__ == "__main__":
    main()