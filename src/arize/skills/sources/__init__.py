"""Skill source resolvers — Hermes, OpenClaw, generic GitHub."""

from arize.skills.sources.base import ResolvedSkill, SourceResolver
from arize.skills.sources.github import GitHubResolver
from arize.skills.sources.hermes import HERMES_REPO_URL, HermesResolver
from arize.skills.sources.openclaw import OPENCLAW_REPO_URL, OpenClawResolver

__all__ = [
    "GitHubResolver",
    "HERMES_REPO_URL",
    "HermesResolver",
    "OPENCLAW_REPO_URL",
    "OpenClawResolver",
    "ResolvedSkill",
    "SourceResolver",
]
