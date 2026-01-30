from pathlib import Path

import pytest

from diffpdf import diffpdf

TEST_ASSETS_DIR = Path(__file__).parent / "assets"


@pytest.mark.parametrize(
    ("ref_pdf_rel", "actual_pdf_rel", "should_pass"),
    [
        # Pass cases
        ("pass/identical-A.pdf", "pass/identical-B.pdf", True),
        ("pass/hash-diff-A.pdf", "pass/hash-diff-B.pdf", True),
        ("pass/minor-color-diff-A.pdf", "pass/minor-color-diff-B.pdf", True),
        ("pass/multiplatform-diff-A.pdf", "pass/multiplatform-diff-B.pdf", True),
        # Fail cases
        ("fail/1-letter-diff-A.pdf", "fail/1-letter-diff-B.pdf", False),
        ("fail/major-color-diff-A.pdf", "fail/major-color-diff-B.pdf", False),
        ("fail/page-count-diff-A.pdf", "fail/page-count-diff-B.pdf", False),
        ("fail/unicode-A.pdf", "fail/unicode-B.pdf", False),
    ],
)
def test_api(ref_pdf_rel, actual_pdf_rel, should_pass):
    ref_pdf = TEST_ASSETS_DIR / ref_pdf_rel
    actual_pdf = TEST_ASSETS_DIR / actual_pdf_rel

    result = diffpdf(ref_pdf, actual_pdf)

    assert result == should_pass


def test_text_diff_output(tmp_path):
    ref_pdf = TEST_ASSETS_DIR / "fail/1-letter-diff-A.pdf"
    actual_pdf = TEST_ASSETS_DIR / "fail/1-letter-diff-B.pdf"

    result = diffpdf(ref_pdf, actual_pdf, output_dir=tmp_path)

    assert result is False
    diff_file = tmp_path / "1-letter-diff-A_vs_1-letter-diff-B_text_diff.txt"
    assert diff_file.exists()
    assert diff_file.read_text(encoding="utf-8")
