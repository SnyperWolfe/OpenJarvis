"""External-framework subprocess backends (Hermes Agent, OpenClaw)."""

from arize.evals.backends.external.hermes_agent import HermesBackend
from arize.evals.backends.external.openclaw import OpenClawBackend

__all__ = ["HermesBackend", "OpenClawBackend"]
