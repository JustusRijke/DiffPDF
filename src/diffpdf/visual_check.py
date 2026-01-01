import logging
from pathlib import Path

import fitz
from PIL import Image
from pixelmatch import pixelmatch


def render_page_to_image(pdf_path: Path, page_num: int, dpi: int) -> Image.Image:
    doc = fitz.open(pdf_path)
    page = doc[page_num]
    pix = page.get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    doc.close()
    return img


def compare_images(
    ref_img: Image.Image,
    actual_img: Image.Image,
    threshold: float,
    output_path: Path | None,
) -> bool:
    mismatch_count = pixelmatch(
        ref_img, actual_img, output=output_path, threshold=threshold
    )

    if mismatch_count > 0:
        return False

    return True


def check_visual_content(
    ref: Path,
    actual: Path,
    threshold: float,
    dpi: int,
    output_dir: Path | None,
) -> bool:
    logger = logging.getLogger()
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)

    ref_doc = fitz.open(ref)
    page_count = len(ref_doc)
    ref_doc.close()

    failing_pages = []

    for page_num in range(page_count):
        ref_img = render_page_to_image(ref, page_num, dpi)
        actual_img = render_page_to_image(actual, page_num, dpi)

        output_path = None
        if output_dir is not None:
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
        return False

    logger.info("Visual content matches")
    return True
