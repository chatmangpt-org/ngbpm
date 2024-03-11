"""ngbpm CLI."""
import sys
from pathlib import Path

import typer
import dspy

from dspygen.utils.file_tools import find_project_root

app = typer.Typer()


@app.command()
def say(message: str = "") -> None:
    """Say a message."""
    typer.echo()


@app.command()
def call() -> None:
    """Call a module."""
    typer.echo(__file__)


def main():
    from pathlib import Path
    print(find_project_root())
    # print(find_project_root(__file__))
    # from dspygen.utils.dspy_tools import init_dspy
    # init_dspy()
    #
    # from dspygen.modules.mermaid_js_module import mermaid_js_call
    # print(mermaid_js_call("Hello World System"))


if __name__ == '__main__':
    main()
