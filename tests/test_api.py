from pathlib import Path

from diffpdf import diffpdf

TEST_ASSETS_DIR = Path(__file__).parent / "assets"


def test_diffpdf():
    assert diffpdf(
        TEST_ASSETS_DIR / "pass/identical-A.pdf",
        TEST_ASSETS_DIR / "pass/identical-B.pdf",
    )
