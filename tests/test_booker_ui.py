"""
Beginner:
Create an automated test that completes the contact us form
on the homepage, submits it,
and asserts that the form was completed successfully.

Intermediate:
Create an automated test that reads a message on the admin side of the site.

1. You’ll need to trigger a message in the first place
2. Login as admin
3. Open that specific message and validate its contents.

Advanced:
"""
from typing import Dict

from booker import mocks


def submit_form(py, payload: Dict):
    py.get('#name').type(payload['name'])
    py.get('#email').type(payload['email'])
    py.get('#phone').type(payload['phone'])
    py.get('#subject').type(payload['subject'])
    py.get('#description').type(payload['description'])
    py.get('#submitContact').click()
    return py


def test_submit_form(py):
    py.visit('https://aw3.automationintesting.online/#/')
    request = mocks.valid_message_request
    submit_form(py, request)
    assert py.get(".row.contact h2").should().contain_text(f'Thanks for getting in touch {request["name"]}')
