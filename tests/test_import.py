"""Test ngbpm."""

import ngbpm


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(ngbpm.__name__, str)
