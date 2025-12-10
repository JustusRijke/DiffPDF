from pathlib import Path

from DiffPDF.page_check import get_page_count


def test_get_page_count_returns_int():
    assets_dir = Path(__file__).parent / "assets" / "fail"
    pdf_path = assets_dir / "1-letter-diff-A.pdf"

    count = get_page_count(pdf_path)

    assert isinstance(count, int)
    assert count >= 1


def test_get_page_count_consistent():
    assets_dir = Path(__file__).parent / "assets" / "pass"
    pdf_path = assets_dir / "identical-A.pdf"

    count1 = get_page_count(pdf_path)
    count2 = get_page_count(pdf_path)

    assert count1 == count2
