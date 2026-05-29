import pytest
SYSTEM_VERSION = "1.0.0"

@pytest.mark.skipif(
    SYSTEM_VERSION == "1.0.0", reason=f"Need to be implemented in 1.3.0, current version is {SYSTEM_VERSION}"
)
def test_system_version_valid():
    pass

@pytest.mark.skipif(
    SYSTEM_VERSION == "1.3.0", reason=f"Need to be implemented in 1.4.0, current version is {SYSTEM_VERSION}"
)
def test_system_version_invalid():
    pass
