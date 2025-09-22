from reservation_notifier.checker import check_reservation
import requests_mock


def test_check_reservation_detects_keyword():
    with requests_mock.Mocker() as m:
        m.get("http://fake.com", text="<button>Jetzt reservieren</button>")
        assert check_reservation("http://fake.com") is True


def test_check_reservation_no_keyword():
    with requests_mock.Mocker() as m:
        m.get("http://fake.com", text="<p>Keine Plätze frei</p>")
        assert check_reservation("http://fake.com") is False
