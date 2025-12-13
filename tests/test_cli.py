from pathlib import Path

import pytest
from click.testing import CliRunner

from DiffPDF.cli import cli


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
def test_cli(ref_pdf_rel, actual_pdf_rel, expected_exit_code):
    """Parametric integration test: CLI should exit with correct code for various PDF pairs."""
    runner = CliRunner()
    test_assets_dir = Path(__file__).parent / "assets"

    ref_pdf = str(test_assets_dir / ref_pdf_rel)
    actual_pdf = str(test_assets_dir / actual_pdf_rel)

    result = runner.invoke(cli, [ref_pdf, actual_pdf])

    assert result.exit_code == expected_exit_code
