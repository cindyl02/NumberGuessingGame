from main import EASY_LEVEL_TRIES, HARD_LEVEL_TRIES, start_game


def test_start_game_easy_correct_answer(capfd, monkeypatch):
    inputs = ["100", "90", "50", "40", "20", "16", "11", "5", "9", "10"]
    answer = 10

    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    start_game(EASY_LEVEL_TRIES, answer)
    out, err = capfd.readouterr()

    for i in range(1, 11):
        assert f"You have {i} attempts remaining to guess the number.\n" in out

    assert f"You got it! The answer was {answer}.\n" in out
    assert out.count("Too high.\n") == 7
    assert out.count("Too low.\n") == 2
    assert out.count("Guess again.\n") == 9


def test_start_game_hard_correct_answer(capfd, monkeypatch):
    inputs = ["100", "90", "11", "9", "10"]
    answer = 10

    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    start_game(HARD_LEVEL_TRIES, answer)
    out, err = capfd.readouterr()

    for i in range(1, 6):
        assert f"You have {i} attempts remaining to guess the number.\n" in out

    assert f"You got it! The answer was {answer}.\n" in out
    assert out.count("Too high.\n") == 3
    assert out.count("Too low.\n") == 1
    assert out.count("Guess again.\n") == 4


def test_start_game_easy_wrong_answer(capfd, monkeypatch):
    inputs = ["100", "90", "50", "40", "20", "16", "11", "5", "9", "7"]
    answer = 8

    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    start_game(EASY_LEVEL_TRIES, answer)
    out, err = capfd.readouterr()

    for i in range(1, 11):
        assert f"You have {i} attempts remaining to guess the number.\n" in out

    assert f"You got it! The answer was {answer}.\n" not in out
    assert out.count("Too high.\n") == 8
    assert out.count("Too low.\n") == 2
    assert out.count("Guess again.\n") == 9
    assert "You've run out of guesses, you lose." in out


def test_start_game_hard_wrong_answer(capfd, monkeypatch):
    inputs = ["100", "90", "4", "3", "6"]
    answer = 5

    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    start_game(HARD_LEVEL_TRIES, answer)
    out, err = capfd.readouterr()

    for i in range(1, 6):
        assert f"You have {i} attempts remaining to guess the number.\n" in out

    assert f"You got it! The answer was {answer}.\n" not in out
    assert out.count("Too high.\n") == 3
    assert out.count("Too low.\n") == 2
    assert out.count("Guess again.\n") == 4
    assert "You've run out of guesses, you lose." in out
