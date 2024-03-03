from app.hangman import hangman
import pytest

def choice():
    return 'python'


def test_win(mocker, capsys):
    mocker.patch('app.hangman.get_random_word', choice)
    mocker.patch('builtins.input', side_effect=["p", "y", "t", "h", "o", "n", "n"])
    hangman()
    captured = capsys.readouterr()
    assert "You win!" in captured.out


def test_loose(mocker, capsys):
    mocker.patch('app.hangman.get_random_word', choice)
    mocker.patch('builtins.input', side_effect=["a", "b", "c", "d", "e", "f", "g", "n"])
    hangman()
    captured = capsys.readouterr()
    assert "You lose!" in captured.out


def test_play_again(mocker, capsys):
    mocker.patch('app.hangman.get_random_word', choice)
    #Здесь я сначала угадал python, потом нажал y для начала новой игры, снова угадал python, и не стал играть дальше
    mocker.patch('builtins.input', side_effect=["p", "y", "t", "h", "o", "n", "y", "p", "y", "t", "h", "o", "n", "n"])
    hangman()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out


def test_invalid(mocker, capsys):
    mocker.patch('app.hangman.get_random_word', choice)
    #Invalid guess - число 1
    mocker.patch('builtins.input', side_effect=["1", "p", "y", "t", "h", "o", "n", "n"])
    hangman()
    captured = capsys.readouterr()
    assert "Invalid guess. Please enter a single letter." in captured.out


def test_already_guessedd(mocker, capsys):
    mocker.patch('app.hangman.get_random_word', choice)
    #alreday guessed - y
    mocker.patch('builtins.input', side_effect=["p", "y", "y", "t", "h", "o", "n", "n"])
    hangman()
    captured = capsys.readouterr()
    assert "You have already guessed that letter." in captured.out


def test_keyboard_interupt(mocker, capsys):
    mocker.patch('app.hangman.get_random_word', choice)
    mocker.patch('builtins.input', side_effect=KeyboardInterrupt)
    with pytest.raises(SystemExit):
        hangman()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out