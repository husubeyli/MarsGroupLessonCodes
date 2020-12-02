import pytest

def test_inc(mock_a):
    assert mock_a.inc() == 2 # PASSED edir cunki, mock_a.inc() 2 return edir 

def test_inc2(mock_a):
    assert mock_a.inc() == 2 # FAIL edir çünki, mock_a.inc() 3 return edir
