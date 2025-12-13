import hashlib
import sys
from pathlib import Path


def compute_file_hash(filepath: Path) -> str:
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def check_hash(ref: Path, actual: Path, logger) -> None:
    logger.info("[1/4] Checking file hashes...")

    ref_hash = compute_file_hash(ref)
    actual_hash = compute_file_hash(actual)

    if ref_hash == actual_hash:
        logger.info("Files are identical (hash match)")
        sys.exit(0)

    logger.info("Hashes differ, continuing checks")
