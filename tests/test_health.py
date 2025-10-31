from fastapi.testclient import TestClient

try:
    from main import app
except Exception:
    # if app is in package
    from ledger_service.main import app

client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
