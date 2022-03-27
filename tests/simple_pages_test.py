"""This test the homepage"""

def test_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" aria-current="page" href="/docker" style="color: white;">Docker</a>' in response.data
    assert b'<a class="nav-link" aria-current="page" href="/python" style="color: white;">Python</a>' in response.data
    assert b'<a class="nav-link" aria-current="page" href="/html1" style="color: white;">CI/CD</a>' in response.data
    assert b'<a class="nav-link" aria-current="page" href="/git" style="color: white;">Git</a>' in response.data

def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home Page" in response.data


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
    assert b"Let's take a closer look to CI/CD" in response.data


def test_python_page(client):
    """This makes the ci/cd page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Let's take a closer look to Python" in response.data
