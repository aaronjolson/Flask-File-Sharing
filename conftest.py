import pytest


@pytest.fixture
def client():
    import main
    app = main.app
    app.testing = True
    with app.test_client() as client:
        yield client
