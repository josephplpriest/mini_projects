from ..app import start_game, check_answer, get_input, validate_input

def test_start_game():
    assert(start_game() == None)

def test_get_input():
    assert(get_input() == None)

def test_validate_input():
    assert(validate_input() == None)

def test_check_answer():
    assert(check_answer() == None)
