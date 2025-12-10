from click.testing import CliRunner

from DiffPDF.cli import cli


def test_cli_with_missing_file_exits_2():
    runner = CliRunner()
    result = runner.invoke(cli, ["nonexistent.pdf", "another.pdf"])

    assert result.exit_code == 2
