from pathlib import Path

from click.testing import CliRunner

from diffpdf.cli import cli

TEST_ASSETS_DIR = Path(__file__).parent / "assets"


def test_verbose_flag():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            str(TEST_ASSETS_DIR / "pass/identical-A.pdf"),
            str(TEST_ASSETS_DIR / "pass/identical-B.pdf"),
            "-v",
        ],
    )
    assert result.exit_code == 0
    assert "INFO" in result.output
    assert "DEBUG" not in result.output


def test_double_verbose_flag():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            str(TEST_ASSETS_DIR / "pass/identical-A.pdf"),
            str(TEST_ASSETS_DIR / "pass/identical-B.pdf"),
            "-vv",
        ],
    )
    assert result.exit_code == 0
    assert "DEBUG" in result.output
