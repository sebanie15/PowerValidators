

from .pwd_validator import PwdValidator


def test_pwd_length_ok():
    validator = PwdValidator()
    password = 'test1234'
    assert validator.length_is_valid(password) == True

def test_pwd_length_to_short():
    validator = PwdValidator()
    password = 'test123'
    assert validator.length_is_valid(password) == False

def test_num_digits_ok():
    validator = PwdValidator()
    password = 'test12'
    assert validator.num_digits_is_valid(password) == True

def test_num_digits_not_enough():
    validator = PwdValidator()
    password = 'test1'
    assert validator.num_digits_is_valid(password) == False


def test_num_lowercase_ok():
    validator = PwdValidator()
    password = 'te1234'
    assert validator.num_lowercase_is_valid(password) == True

def test_num_lowercase_not_enough():
    validator = PwdValidator()
    password = 'tEST123!'
    assert validator.num_lowercase_is_valid(password) == False

def test_num_uppercase_ok():
    validator = PwdValidator()
    password = 'TEst1234'
    assert validator.num_uppercase_is_valid(password) == True

def test_num_uppercase_not_enough():
    validator = PwdValidator()
    password = 'Test1234'
    assert validator.num_uppercase_is_valid(password) == False

def test_num_special_char_ok():
    validator = PwdValidator()
    password = 'TEst12!@'
    assert validator.num_special_char_is_valid(password) == True

def test_num_special_char_not_enough():
    validator = PwdValidator()
    password = 'TEst123!'
    assert validator.num_special_char_is_valid(password) == False

def test_is_valid_ok():
    validator = PwdValidator()
    password = 'TEst12!@'
    assert validator.is_valid(password) == True

def test_is_valid_():
    validator = PwdValidator()
    password = 'Test12!@'
    assert validator.is_valid(password) == False
