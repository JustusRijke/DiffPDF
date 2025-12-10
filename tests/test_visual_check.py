from pathlib import Path

from DiffPDF.visual_check import compare_images, render_page_to_image


def test_render_page_to_image_returns_image():
    assets_dir = Path(__file__).parent / "assets" / "pass"
    pdf_path = assets_dir / "identical-A.pdf"

    img = render_page_to_image(pdf_path, 0, 96)

    assert img is not None
    assert img.width > 0
    assert img.height > 0


def test_compare_images_identical_returns_true(tmp_path):
    assets_dir = Path(__file__).parent / "assets" / "pass"
    pdf_path = assets_dir / "identical-A.pdf"

    img1 = render_page_to_image(pdf_path, 0, 96)
    img2 = render_page_to_image(pdf_path, 0, 96)

    output_path = tmp_path / "diff.png"
    result = compare_images(img1, img2, 0.1, output_path)

    assert result is True
    assert not output_path.exists()
