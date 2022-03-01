"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Lorem ipsum" in response.data


def test_request_about(client):
    response = client.get('/about')
    assert b"about" in response.data