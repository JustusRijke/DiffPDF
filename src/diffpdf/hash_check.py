import hashlib
from pathlib import Path


def compute_file_hash(filepath: Path) -> str:
    sha256 = hashlib.sha256()
    with Path(filepath).open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def check_hash(ref: Path, actual: Path) -> bool:
    ref_hash = compute_file_hash(ref)
    actual_hash = compute_file_hash(actual)

    return ref_hash == actual_hash
