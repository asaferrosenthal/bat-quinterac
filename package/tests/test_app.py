import pytest


def test_file1_method1(capsys):
    out, err = capsys.readouterr()
    assert out == "hello word!\n"
    x = 5
    y = 6
    assert x+1 == y, "test failed"
