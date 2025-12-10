from pathlib import Path

from DiffPDF.text_check import extract_text, generate_diff


def test_extract_text_returns_string():
    assets_dir = Path(__file__).parent / "assets" / "pass"
    pdf_path = assets_dir / "identical-A.pdf"

    text = extract_text(pdf_path)

    assert isinstance(text, str)
    assert len(text) > 0


def test_extract_text_strips_whitespace():
    assets_dir = Path(__file__).parent / "assets" / "pass"
    pdf_path = assets_dir / "identical-A.pdf"

    text = extract_text(pdf_path)

    assert text == text.strip()


def test_generate_diff_shows_differences():
    ref_text = "Hello world"
    actual_text = "Hello wurld"

    diff = generate_diff(ref_text, actual_text)

    assert isinstance(diff, str)
    assert "world" in diff or "wurld" in diff
