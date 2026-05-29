import pytest
@pytest.mark.xfail(reason = "bug #akjndsfkansdkfjn")
def test_xfail_with_bug():
    assert 1==2
@pytest.mark.xfail(reason = "bug #akjndsfkansdkfjn")
def test_xfail_without_bug():
    ...
