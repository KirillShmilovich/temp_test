"""
Unit and regression test for the temp_test package.
"""

# Import package, test suite, and other packages as needed
import temp_test
import pytest
import sys

def test_temp_test_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "temp_test" in sys.modules

def test_convert_c():
    true_val = 100.0
    T = temp_test.Temp(temp_f=212)
    val = T.convert_to_c()
    assert true_val==val