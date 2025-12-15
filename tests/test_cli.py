from pathlib import Path

import pytest
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


@pytest.mark.parametrize(
    "ref_pdf_rel,actual_pdf_rel,expected_exit_code",
    [
        # Pass cases (exit code 0)
        ("pass/identical-A.pdf", "pass/identical-B.pdf", 0),
        ("pass/hash-diff-A.pdf", "pass/hash-diff-B.pdf", 0),
        ("pass/minor-color-diff-A.pdf", "pass/minor-color-diff-B.pdf", 0),
        ("pass/multiplatform-diff-A.pdf", "pass/multiplatform-diff-B.pdf", 0),
        # Fail cases (exit code 1)
        ("fail/1-letter-diff-A.pdf", "fail/1-letter-diff-B.pdf", 1),
        ("fail/major-color-diff-A.pdf", "fail/major-color-diff-B.pdf", 1),
        ("fail/page-count-diff-A.pdf", "fail/page-count-diff-B.pdf", 1),
        # Critical error cases (exit code 2)
        ("nonexistent.pdf", "another.pdf", 2),
    ],
)
def test_comparators(ref_pdf_rel, actual_pdf_rel, expected_exit_code):
    """Parametric integration test: CLI should exit with correct code for various PDF pairs."""
    runner = CliRunner()

    ref_pdf = str(TEST_ASSETS_DIR / ref_pdf_rel)
    actual_pdf = str(TEST_ASSETS_DIR / actual_pdf_rel)

    result = runner.invoke(cli, [ref_pdf, actual_pdf])

    assert result.exit_code == expected_exit_code
