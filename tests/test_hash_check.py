from pathlib import Path

from DiffPDF.hash_check import compute_file_hash


def test_compute_file_hash_returns_sha256():
    assets_dir = Path(__file__).parent / "assets" / "pass"
    pdf_path = assets_dir / "identical-A.pdf"

    hash_result = compute_file_hash(pdf_path)

    assert isinstance(hash_result, str)
    assert len(hash_result) == 64


def test_compute_file_hash_consistent():
    assets_dir = Path(__file__).parent / "assets" / "pass"
    pdf_path = assets_dir / "identical-A.pdf"

    hash1 = compute_file_hash(pdf_path)
    hash2 = compute_file_hash(pdf_path)

    assert hash1 == hash2


def test_compute_file_hash_different_files():
    assets_dir = Path(__file__).parent / "assets"
    pdf1 = assets_dir / "pass" / "identical-A.pdf"
    pdf2 = assets_dir / "fail" / "1-letter-diff-A.pdf"

    hash1 = compute_file_hash(pdf1)
    hash2 = compute_file_hash(pdf2)

    assert hash1 != hash2
