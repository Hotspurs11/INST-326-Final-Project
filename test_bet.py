"""Tests blackjack project code"""
from project import Game
from project import Player
from project import player_game
import pytest
def test_bet():
    temp = Player(5000, 'George', 4)
    temp.bet(1000)
    assert 4000 == temp.balance
    temp.bet(1000)
    assert 3000 == temp.balance
def test_fold():
    temp = Player(5000, 'George', 4)
    temp.foldround = False
    assert False == temp.fold()
    temp.foldround = True
    assert True == temp.fold()
def test_double_down():
    temp = Player(5000, 'George', 4)
    temp.double_down(1000)
    assert 3000 == temp.balance
    temp.double_down(1000)
    assert 1000 == temp.balance
def test_check_blackjack():
    p_g = player_game()
    v_d = p_g.value_display()
    if p_g.player_hand() == 21:
        assert check_blackjack() == True, False
    if p_g.player_hand() == 21:
        assert check_blackjack() == False, True
