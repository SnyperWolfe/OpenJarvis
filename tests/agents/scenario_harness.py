"""Shared harness dataclasses for agent lifecycle scenario tests."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from arize.agents.executor import AgentExecutor
from arize.agents.manager import AgentManager
from arize.agents.scheduler import AgentScheduler
from arize.core.events import EventBus
from tests.agents.fake_engine import FakeEngine


@dataclass(slots=True)
class FakeSystem:
    """Lightweight stand-in for ArizeSystem — just engine + model."""

    engine: FakeEngine
    model: str = "fake-model"
    memory_backend: Any = None
    channel_backend: Any = None
    tools: list = field(default_factory=list)
    config: Any = None
    session_store: Any = None


@dataclass(slots=True)
class ScenarioHarness:
    """All components needed for an agent lifecycle scenario test."""

    manager: AgentManager
    executor: AgentExecutor
    scheduler: AgentScheduler
    bus: EventBus
    engine: FakeEngine
    system: FakeSystem
    db_path: str
