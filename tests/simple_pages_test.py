"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a href="/html1" class="nav-link">HTML</a>' in response.data
    assert b'<a href="/git" class="nav-link">Git</a>' in response.data
    assert b'<a href="/docker" class="nav-link">Docker</a> ' in response.data
    assert b'<a href="/python" class="nav-link">Python/Flask</a>' in response.data


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Home Page" in response.data


def test_git_page(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data


def test_docker_page(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_html_page(client):
    """This makes the flask page"""
    response = client.get("/html1")
    assert response.status_code == 200
    assert b"HTML" in response.data


def test_python_page(client):
    """This makes the ci/cd page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Pyhton" in response.data
