#!/usr/bin/env python

"""Tests for `sc2replaystats_uploader` package."""


import unittest
from click.testing import CliRunner

from sc2replaystats_uploader import sc2replaystats_uploader
from sc2replaystats_uploader import cli


class TestSc2replaystats_uploader(unittest.TestCase):
    """Tests for `sc2replaystats_uploader` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'sc2replaystats_uploader.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
