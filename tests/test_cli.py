from pathlib import Path

from click.testing import CliRunner

from diffpdf.cli import cli

TEST_ASSETS_DIR = Path(__file__).parent / "assets"


def test_cli_with_output_dir():
    runner = CliRunner()

    with runner.isolated_filesystem():
        ref_pdf = str(TEST_ASSETS_DIR / "fail/major-color-diff-A.pdf")
        actual_pdf = str(TEST_ASSETS_DIR / "fail/major-color-diff-B.pdf")

        result = runner.invoke(cli, [ref_pdf, actual_pdf, "--output-dir", "./diff"])

        assert result.exit_code == 1
        assert Path("./diff").exists()


def test_verbose_flag():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            str(TEST_ASSETS_DIR / "pass/identical-A.pdf"),
            str(TEST_ASSETS_DIR / "pass/identical-B.pdf"),
            "-v",
        ],
    )
    assert result.exit_code == 0
    assert "INFO" in result.output
