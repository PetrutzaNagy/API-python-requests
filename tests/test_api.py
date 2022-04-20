import requests

def test_response_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200, "status code is not ok"

def test_response_404():
    response = requests.get("http://api.zippopotam.us/us/902104645756756756")
    assert response.status_code == 404, "status code is not ok"

def test_content_type():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers["Content-Type"] == "application/json"

def test_body():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == "United States"
    assert response_body["post code"] == "90210"
    assert response_body["places"][0]["place name"] == "Beverly Hills"