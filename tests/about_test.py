"""This test the homepage"""


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert b"about" in response.data
