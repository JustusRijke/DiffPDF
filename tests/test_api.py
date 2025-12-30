from pathlib import Path

import pytest

from diffpdf import diffpdf

TEST_ASSETS_DIR = Path(__file__).parent / "assets"


def test_diffpdf_function():
    with pytest.raises(SystemExit) as exc_info:
        diffpdf(
            TEST_ASSETS_DIR / "pass/identical-A.pdf",
            TEST_ASSETS_DIR / "pass/identical-B.pdf",
            output_dir=Path("./"),
        )
    assert exc_info.value.code == 0
