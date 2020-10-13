from booker import mocks, message_service


def test_create_message():
    response = message_service.create_message(mocks.valid_message_request)
    assert response.ok
