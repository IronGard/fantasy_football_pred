import pytest

from football_pred import model


def test_average_score_empty():
    assert model.average_score([]) == 0.0


def test_average_score():
    assert model.average_score([10, 20, 30]) == 20


def test_predict_winner():
    assert model.predict_winner([5, 10, 7]) == 1


def test_predict_winner_empty():
    with pytest.raises(ValueError):
        model.predict_winner([])
