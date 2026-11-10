"""Command-line interface for ARIZE (Click-based)."""

from __future__ import annotations

import sys

import click

import arize
from arize.cli.scan_cmd import scan


def _invoked_command(argv: list[str]) -> str:
    """Return the first positional CLI token after global flags."""
    for arg in argv:
        if arg.startswith("-"):
            continue
        return arg
    return ""


# A data-boundary scan must be able to diagnose an invalid ARIZE_HOME.
# Importing the rest of the CLI eagerly would import core.config and resolve that
# path before the scan can turn the failure into a finding.
_DATA_BOUNDARY_BOOTSTRAP = (
    _invoked_command(sys.argv[1:]) == "scan" and "--data-boundaries" in sys.argv[1:]
)


def _should_skip_update_check(ctx: click.Context, argv: list[str]) -> bool:
    """Return true for commands whose diagnostics should remain local-only."""
    if "--research" in argv:
        return True
    return ctx.invoked_subcommand == "scan" and "--data-boundaries" in argv


@click.group(
    help="ARIZE — modular AI assistant backend",
    invoke_without_command=True,
)
@click.version_option(version=arize.__version__, prog_name="arize")
@click.option("--verbose", is_flag=True, default=False, help="Enable debug logging")
@click.option("--quiet", is_flag=True, default=False, help="Suppress non-error output")
@click.option(
    "--pick-model",
    "pick_model_bare",
    is_flag=True,
    default=False,
    help=(
        "Bare ``arize``: force interactive model list "
        "(overrides ARIZE_SKIP_MODEL_PICK)."
    ),
)
@click.pass_context
def cli(ctx: click.Context, verbose: bool, quiet: bool, pick_model_bare: bool) -> None:
    """Top-level CLI group."""
    from arize.cli.log_config import setup_logging

    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
    ctx.obj["quiet"] = quiet
    ctx.obj["pick_model_bare"] = pick_model_bare
    setup_logging(verbose=verbose, quiet=quiet)

    # Check for updates on interactive commands. The banner is noise in
    # demo recordings of ``arize ask --research``, so skip it whenever
    # the research flag is in argv (cheap argv sniff — Click hasn't
    # parsed the subcommand's args yet at this point). Also skip
    # ``arize scan --data-boundaries`` because it is intended to be a
    # local application-data diagnostic with no outbound calls.
    import sys

    skip_update_check = _should_skip_update_check(ctx, sys.argv[1:])
    if not quiet and ctx.invoked_subcommand and not skip_update_check:
        import threading

        from arize.cli._version_check import check_for_updates

        # Run the PyPI version poll off the hot path: on a cache miss it does
        # a blocking urlopen (up to 3s) that otherwise delays every command,
        # notably `arize serve` startup (#263). It's best-effort and never
        # raises, and the nudge prints to stderr, so a daemon thread is safe —
        # for long-lived commands (serve) it finishes; for short commands that
        # exit first, the check is simply skipped this run (same as a miss).
        threading.Thread(
            target=check_for_updates,
            args=(ctx.invoked_subcommand,),
            daemon=True,
        ).start()

    # First-run guard — routes bare `arize` to chat or init.
    if ctx.invoked_subcommand is None:
        from arize.cli._first_run import check_and_route

        check_and_route(ctx)


cli.add_command(scan, "scan")
if not _DATA_BOUNDARY_BOOTSTRAP:
    from arize.cli._bootstrap import bootstrap_cmd
    from arize.cli.add_cmd import add
    from arize.cli.agent_cmd import agent
    from arize.cli.ask import ask
    from arize.cli.bench_cmd import bench
    from arize.cli.channel_cmd import channel
    from arize.cli.channels_cmd import channels
    from arize.cli.chat_cmd import chat
    from arize.cli.compose_cmd import compose
    from arize.cli.config_cmd import config
    from arize.cli.connect_cmd import connect
    from arize.cli.daemon_cmd import restart, start, status, stop
    from arize.cli.digest_cmd import digest
    from arize.cli.doctor_cmd import doctor
    from arize.cli.eval_cmd import eval_group
    from arize.cli.feedback_cmd import feedback_group
    from arize.cli.gateway_cmd import gateway
    from arize.cli.gui_cmd import gui
    from arize.cli.host_cmd import host
    from arize.cli.init_cmd import init
    from arize.cli.memory_cmd import memory
    from arize.cli.mine_cmd import mine
    from arize.cli.model import model
    from arize.cli.operators_cmd import operators
    from arize.cli.optimize_cmd import optimize_group
    from arize.cli.pearl_cmd import pearl
    from arize.cli.quickstart_cmd import quickstart
    from arize.cli.registry_cmd import registry
    from arize.cli.scheduler_cmd import scheduler
    from arize.cli.self_update_cmd import self_update
    from arize.cli.serve import serve
    from arize.cli.skill_cmd import skill
    from arize.cli.telemetry_cmd import telemetry
    from arize.cli.tool_cmd import tool
    from arize.cli.vault_cmd import vault
    from arize.cli.workflow_cmd import workflow

    cli.add_command(init, "init")
    cli.add_command(ask, "ask")
    cli.add_command(chat, "chat")
    cli.add_command(serve, "serve")
    cli.add_command(model, "model")
    cli.add_command(memory, "memory")
    cli.add_command(mine, "mine")
    cli.add_command(pearl, "pearl")
    cli.add_command(telemetry, "telemetry")
    cli.add_command(bench, "bench")
    cli.add_command(channel, "channel")
    cli.add_command(channels, "channels")
    cli.add_command(scheduler, "scheduler")
    cli.add_command(doctor, "doctor")
    cli.add_command(agent, "agents")
    cli.add_command(workflow, "workflow")
    cli.add_command(skill, "skill")
    cli.add_command(start, "start")
    cli.add_command(stop, "stop")
    cli.add_command(restart, "restart")
    cli.add_command(status, "status")
    cli.add_command(vault, "vault")
    cli.add_command(add, "add")
    cli.add_command(operators, "operators")
    cli.add_command(eval_group, "eval")
    cli.add_command(host, "host")
    cli.add_command(quickstart, "quickstart")
    cli.add_command(optimize_group, "optimize")
    cli.add_command(feedback_group, "feedback")
    cli.add_command(compose, "compose")
    cli.add_command(gateway, "gateway")
    cli.add_command(gui, "gui")
    cli.add_command(tool, "tool")
    cli.add_command(registry, "registry")
    cli.add_command(config, "config")
    cli.add_command(connect, "connect")
    cli.add_command(digest, "digest")

    # Deep Research setup pulls the ingestion pipeline (embeddings/numpy). Guard
    # it so an import-time dependency failure cannot take down the whole CLI.
    try:
        from arize.cli.deep_research_setup_cmd import deep_research_setup

        cli.add_command(deep_research_setup, "deep-research-setup")
        cli.add_command(deep_research_setup, "research")
    except Exception as _dr_exc:
        import logging as _logging

        _logging.getLogger(__name__).debug(
            "deep-research command unavailable: %s", _dr_exc
        )
    cli.add_command(self_update, "self-update")
    cli.add_command(bootstrap_cmd, "_bootstrap")

    # Gateway CLI commands (lazy import to avoid pulling starlette)
    try:
        from arize.cli.auth_cmd import auth

        cli.add_command(auth, "auth")
    except ImportError:
        pass

    try:
        from arize.cli.tunnel_cmd import tunnel

        cli.add_command(tunnel, "tunnel")
    except ImportError:
        pass


def main() -> None:
    """Entry point registered as ``arize`` console script."""
    import sys

    if sys.platform == "win32":
        for _stream in (sys.stdout, sys.stderr):
            if hasattr(_stream, "reconfigure"):
                try:
                    _stream.reconfigure(encoding="utf-8", errors="replace")
                except (AttributeError, OSError):
                    pass
    cli()


__all__ = ["cli", "main"]
