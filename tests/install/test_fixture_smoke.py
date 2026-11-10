"""Smoke test that the tmp_arize_home fixture works."""

from __future__ import annotations

from pathlib import Path

from arize.core import config as config_mod


def test_fixture_redirects_default_config_dir(tmp_arize_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_DIR == tmp_arize_home
    assert tmp_arize_home.exists()
    assert (tmp_arize_home / ".state").exists()
    assert (tmp_arize_home / ".state" / "models").exists()


def test_fixture_redirects_config_path(tmp_arize_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_PATH == tmp_arize_home / "config.toml"
