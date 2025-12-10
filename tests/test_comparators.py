from pathlib import Path

import pytest

from DiffPDF.comparators import compare_pdfs


def test_compare_pdfs_identical_exits_0(tmp_path):
    assets_dir = Path(__file__).parent / "assets" / "pass"
    ref_path = assets_dir / "identical-A.pdf"
    actual_path = assets_dir / "identical-B.pdf"

    import logging
    logger = logging.getLogger()

    with pytest.raises(SystemExit) as exc_info:
        compare_pdfs(ref_path, actual_path, 0.1, 96, tmp_path, logger)

    assert exc_info.value.code == 0


def test_compare_pdfs_hash_diff_all_checks_pass(tmp_path):
    assets_dir = Path(__file__).parent / "assets" / "pass"
    ref_path = assets_dir / "hash-diff-A.pdf"
    actual_path = assets_dir / "hash-diff-B.pdf"

    import logging
    logger = logging.getLogger()

    with pytest.raises(SystemExit) as exc_info:
        compare_pdfs(ref_path, actual_path, 0.1, 96, tmp_path, logger)

    assert exc_info.value.code == 0


def test_compare_pdfs_page_count_diff_exits_1(tmp_path):
    assets_dir = Path(__file__).parent / "assets" / "fail"
    ref_path = assets_dir / "page-count-diff-A.pdf"
    actual_path = assets_dir / "page-count-diff-B.pdf"

    import logging
    logger = logging.getLogger()

    with pytest.raises(SystemExit) as exc_info:
        compare_pdfs(ref_path, actual_path, 0.1, 96, tmp_path, logger)

    assert exc_info.value.code == 1


def test_compare_pdfs_text_diff_exits_1(tmp_path):
    assets_dir = Path(__file__).parent / "assets" / "fail"
    ref_path = assets_dir / "1-letter-diff-A.pdf"
    actual_path = assets_dir / "1-letter-diff-B.pdf"

    import logging
    logger = logging.getLogger()

    with pytest.raises(SystemExit) as exc_info:
        compare_pdfs(ref_path, actual_path, 0.1, 96, tmp_path, logger)

    assert exc_info.value.code == 1


def test_compare_pdfs_visual_diff_and_saves_diff_images(tmp_path):
    assets_dir = Path(__file__).parent / "assets" / "fail"
    ref_path = assets_dir / "major-color-diff-A.pdf"
    actual_path = assets_dir / "major-color-diff-B.pdf"

    import logging
    logger = logging.getLogger()

    with pytest.raises(SystemExit) as exc_info:
        compare_pdfs(ref_path, actual_path, 0.1, 96, tmp_path, logger)

    assert exc_info.value.code == 1

    diff_files = list(tmp_path.glob("*_diff.png"))
    assert len(diff_files) > 0
    assert "major-color-diff-A_vs_major-color-diff-B" in diff_files[0].name
