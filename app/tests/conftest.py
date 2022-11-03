import pytest
from app import create_app
from app import db
from flask.signals import request_finished


@pytest.fixture
def app():
    # flags create_app to go into the testing environment
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    # creates an empty database for us to test on
    with app.app_context():
        db.create_all()
        yield app # tells our app to create an instance and sends it to the test to do its 
                    # thing and comes back here

    # once other tests are complete, it returns and clears out any context that was added
    with app.app_context():
        db.drop_all()

# creates a 'dummy" client that will act for us to call any requests to test our routes
@pytest.fixture
def client(app):
    return app.test_client()
