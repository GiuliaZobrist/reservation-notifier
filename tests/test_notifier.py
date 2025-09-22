import os
from unittest.mock import patch, MagicMock
from reservation_notifier.notifier import send_telegram

# Dummy env for testing
os.environ["TELEGRAM_TOKEN"] = "dummy_token"
os.environ["TELEGRAM_CHAT_ID"] = "12345678"

@patch("reservation_notifier.notifier.requests.post")
def test_send_telegram_success(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response

    send_telegram("Test message")
    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert "bot" in args[0]
    assert kwargs["data"]["text"] == "Test message"

@patch("reservation_notifier.notifier.requests.post")
def test_send_telegram_missing_credentials(mock_post):
    os.environ["TELEGRAM_TOKEN"] = ""
    os.environ["TELEGRAM_CHAT_ID"] = ""
    send_telegram("Test")
    mock_post.assert_not_called()
