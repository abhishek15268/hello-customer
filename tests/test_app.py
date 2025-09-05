import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, add

def test_add():
    assert add(2, 3) == 5

def test_home_route():
    # Use Flask's built-in test client
    with app.test_client() as client:
        resp = client.get("/")
        assert resp.status_code == 200
        assert b"I am back!" in resp.data

def test_healthz():
    with app.test_client() as client:
        resp = client.get("/healthz")
        assert resp.status_code == 200
        assert resp.get_json()["status"] == "ok"
