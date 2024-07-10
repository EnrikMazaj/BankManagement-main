import os
import sys
from app import db
from app.models import Bank

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_index(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

def test_add_bank(test_client):
    response = test_client.post('/add_bank', data=dict(name='Test Bank', location='Test Location'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Bank' in response.data

def test_bank_detail(test_client):
    with test_client.application.app_context():
        bank = Bank(name='Detail Bank', location='Detail Location')
        db.session.add(bank)
        db.session.commit()
        bank_id = bank.id

    response = test_client.get(f'/bank/{bank_id}')
    assert response.status_code == 200
    assert b'Detail Bank' in response.data

def test_edit_bank(test_client):
    with test_client.application.app_context():
        bank = Bank(name='Edit Bank', location='Edit Location')
        db.session.add(bank)
        db.session.commit()
        bank_id = bank.id

    response = test_client.post(f'/edit_bank/{bank_id}', data=dict(name='Updated Bank', location='Updated Location'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Updated Bank' in response.data

def test_delete_bank(test_client):
    with test_client.application.app_context():
        bank = Bank(name='Delete Bank', location='Delete Location')
        db.session.add(bank)
        db.session.commit()
        bank_id = bank.id

    response = test_client.post(f'/delete_bank/{bank_id}', follow_redirects=True)
    assert response.status_code == 200
    with test_client.application.app_context():
        session = db.session()
        assert session.get(Bank, bank_id) is None
