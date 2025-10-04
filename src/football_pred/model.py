"""Example model utilities for football_pred.

This module contains a tiny example function used by tests and as a
starting point for model development.
"""
from typing import List


def average_score(scores: List[float]) -> float:
    """Return the arithmetic mean of scores. Returns 0.0 for empty list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def predict_winner(team_scores: List[float]) -> int:
    """Return the index of the team with the highest average score.

    team_scores is a list of average scores per team. If empty, raises ValueError.
    """
    if not team_scores:
        raise ValueError("team_scores must not be empty")
    return int(max(range(len(team_scores)), key=lambda i: team_scores[i]))
