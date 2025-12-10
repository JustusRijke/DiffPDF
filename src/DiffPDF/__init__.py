from importlib.metadata import version

from .cli import cli

__version__ = version("DiffPDF")


def main(args=None):  # pragma: no cover
    if args is None:
        cli()
    else:
        cli(args, standalone_mode=False)


__all__ = ["main", "__version__"]
