"""Tests for speech configuration."""

from arize.core.config import ArizeConfig, SpeechConfig


def test_speech_config_defaults():
    cfg = SpeechConfig()
    assert cfg.backend == "auto"
    assert cfg.model == "base"
    assert cfg.language == ""
    assert cfg.device == "auto"
    assert cfg.compute_type == "float16"


def test_arize_config_has_speech():
    cfg = ArizeConfig()
    assert hasattr(cfg, "speech")
    assert isinstance(cfg.speech, SpeechConfig)
    assert cfg.speech.backend == "auto"


def test_arize_system_has_speech_backend():
    """ArizeSystem has a speech_backend attribute."""
    from arize.system import ArizeSystem

    assert "speech_backend" in ArizeSystem.__dataclass_fields__
