"""Tools primitive — tool system with ABC interface and built-in tools."""

from __future__ import annotations

from arize.tools._stubs import BaseTool, ToolExecutor, ToolSpec

# Import built-in tools to trigger @ToolRegistry.register() decorators.
# Each is wrapped in try/except so the package loads even before the
# individual tool modules are created.
try:
    import arize.tools.calculator  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.think  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.retrieval  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.llm_tool  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.file_read  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.web_search  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.weather  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.fx_macro  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.code_interpreter  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.code_interpreter_docker  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.repl  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.storage_tools  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.mcp_adapter  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.channel_tools  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.http_request  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.docker_shell_exec  # noqa: F401
    import arize.tools.shell_exec  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.memory_manage  # noqa: F401
except ImportError:
    pass
try:
    import arize.tools.user_profile_manage  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.skill_manage  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.file_write  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.apply_patch  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.git_tool  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.db_query  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.pdf_tool  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.image_tool  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.audio_tool  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.knowledge_tools  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.text_to_speech  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.digest_collect  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.scan_chunks  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.knowledge_sql  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.knowledge_search  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.browser  # noqa: F401
    import arize.tools.browser_axtree  # noqa: F401
except ImportError:
    pass

try:
    import arize.tools.proactive_tools  # noqa: F401
except ImportError:
    pass

__all__ = ["BaseTool", "ToolExecutor", "ToolSpec"]
