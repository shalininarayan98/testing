import pytest
from python_exercises import anti_vowel

def test_anti_vowel():
    assert anti_vowel.anti_vowel("hello") == "hll"