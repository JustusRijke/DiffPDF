import sys
from pathlib import Path

import fitz
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch


def render_page_to_image(pdf_path: Path, page_num: int, dpi: int) -> Image.Image:
    doc = fitz.open(pdf_path)
    page = doc[page_num]
    pix = page.get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    doc.close()
    return img


def compare_images(
    ref_img: Image.Image, actual_img: Image.Image, threshold: float, output_path: Path
) -> bool:
    diff_img = Image.new("RGB", ref_img.size)
    mismatch_count = pixelmatch(ref_img, actual_img, diff_img, threshold=threshold)

    if mismatch_count > 0:
        diff_img.save(output_path)
        return False

    return True


def check_visual_content(
    ref: Path, actual: Path, threshold: float, dpi: int, output_dir: Path, logger
) -> None:
    logger.info("[4/4] Checking visual content...")

    output_dir.mkdir(parents=True, exist_ok=True)

    ref_doc = fitz.open(ref)
    page_count = len(ref_doc)
    ref_doc.close()

    failing_pages = []

    for page_num in range(page_count):
        ref_img = render_page_to_image(ref, page_num, dpi)
        actual_img = render_page_to_image(actual, page_num, dpi)

        ref_name = ref.stem
        actual_name = actual.stem
        output_path = (
            output_dir / f"{ref_name}_vs_{actual_name}_page{page_num + 1}_diff.png"
        )

        passed = compare_images(ref_img, actual_img, threshold, output_path)

        if not passed:
            failing_pages.append(page_num + 1)

    if failing_pages:
        logger.error(f"Visual mismatch on pages: {', '.join(map(str, failing_pages))}")
        sys.exit(1)

    logger.info("Visual content matches")
