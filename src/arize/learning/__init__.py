"""Learning primitive -- router policies, reward functions, learning."""

from __future__ import annotations

from arize.learning._stubs import (
    QueryAnalyzer,
    RewardFunction,
    RouterPolicy,
    RoutingContext,
)
from arize.learning.agents.agent_evolver import AgentConfigEvolver
from arize.learning.learning_orchestrator import LearningOrchestrator
from arize.learning.optimize.llm_optimizer import LLMOptimizer
from arize.learning.optimize.optimizer import OptimizationEngine
from arize.learning.optimize.store import OptimizationStore
from arize.learning.routing.complexity import (
    ComplexityQueryAnalyzer,
    score_complexity,
)
from arize.learning.routing.heuristic_reward import HeuristicRewardFunction
from arize.learning.routing.router import (
    HeuristicRouter,
    build_routing_context,
)
from arize.learning.training.data import TrainingDataMiner
from arize.learning.training.lora import HAS_TORCH, LoRATrainer, LoRATrainingConfig


def ensure_registered() -> None:
    """Ensure all learning policies are registered in RouterPolicyRegistry."""
    from arize.learning.routing.heuristic_policy import (
        ensure_registered as _reg_heuristic,
    )

    _reg_heuristic()

    from arize.learning.routing.learned_router import (
        ensure_registered as _reg_learned,
    )

    _reg_learned()

    # Intelligence training (optional deps)
    try:
        import arize.learning.intelligence  # noqa: F401
    except ImportError:
        pass

    # Orchestrator-specific training (optional deps)
    try:
        import arize.learning.intelligence.orchestrator  # noqa: F401
    except ImportError:
        pass

    # Agent optimizers (optional deps)
    try:
        import arize.learning.agents.dspy_optimizer  # noqa: F401
    except ImportError:
        pass
    try:
        import arize.learning.agents.gepa_optimizer  # noqa: F401
    except ImportError:
        pass
    try:
        import arize.learning.agents.ace_optimizer  # noqa: F401
    except ImportError:
        pass


__all__ = [
    "AgentConfigEvolver",
    "ComplexityQueryAnalyzer",
    "HAS_TORCH",
    "HeuristicRewardFunction",
    "HeuristicRouter",
    "LLMOptimizer",
    "LearningOrchestrator",
    "LoRATrainer",
    "LoRATrainingConfig",
    "OptimizationEngine",
    "OptimizationStore",
    "QueryAnalyzer",
    "RewardFunction",
    "RouterPolicy",
    "RoutingContext",
    "TrainingDataMiner",
    "build_routing_context",
    "ensure_registered",
    "score_complexity",
]
