"""Structural protocols for substituting fakes in place of ArizeSystem."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional, Protocol

if TYPE_CHECKING:
    from arize.core.config import ArizeConfig
    from arize.core.events import EventBus
    from arize.engine._stubs import InferenceEngine
    from arize.security.capabilities import CapabilityPolicy
    from arize.sessions.session import SessionStore
    from arize.tools._stubs import BaseTool
    from arize.tools.storage._stubs import MemoryBackend
    from arize.traces.collector import TraceCollector
    from arize.traces.store import TraceStore


class OrchestratorDeps(Protocol):
    """Minimum surface of ArizeSystem that QueryOrchestrator depends on.

    Tests can satisfy this with a lightweight class — no need to construct
    the full ArizeSystem dataclass or materialize every subsystem.
    """

    config: ArizeConfig
    bus: EventBus
    engine: InferenceEngine
    engine_key: str
    model: str
    agent_name: str
    tools: List[BaseTool]
    memory_backend: Optional[MemoryBackend]
    capability_policy: Optional[CapabilityPolicy]
    rate_limiter: Optional[Any]
    session_store: Optional[SessionStore]
    trace_store: Optional[TraceStore]
    trace_collector: Optional[TraceCollector]  # written by _run_agent

    # Optional attribute (getattr with default) — declared for type clarity.
    _skill_few_shot_examples: Any
