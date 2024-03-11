"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"ngbpm v{version('ngbpm')}")  # type: ignore[no-untyped-call]
