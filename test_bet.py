from project import Player
import pytest

def test_bet():
    temp = Player(5000, 'George', 4)
    temp.bet(1000)
    assert 4000 == temp.balance