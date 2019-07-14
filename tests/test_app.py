import os
import tempfile
import pytest
import sys

curr_dir = os.getcwd()
sys.path.extend(['/Users/rsimari/DevOps/DevOps_App/Example_App'])

import my_app

@pytest.fixture
def client():
    my_app.app.config['TESTING'] = True
    client = my_app.app.test_client()

    yield client


def test_hello_world_success(client):
	rv = client.get('/')
	assert rv.data
	assert b'Hello, World' in rv.data

def test_hello_world_fail(client):
	pass