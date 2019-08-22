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
