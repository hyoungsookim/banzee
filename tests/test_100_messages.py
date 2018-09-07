import pytest
from server.messages import get_message


def test_get_message_200():
    assert get_message(200) == 'The request was completed successfully.'

def test_get_message_501():
    assert get_message(501) == 'Unknown code'

