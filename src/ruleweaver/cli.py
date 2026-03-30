src/ruleweaver/cli.py
"""
Command-line interface for RuleWeaver
"""

import click
from .watcher import CodeWatcher
from .weaver_engine import RuleWeaverEngine

@click.command()
@click.argument("watch-path", type=click.Path(exists=True))
def main(watch_path: str):
    """
    Start RuleWeaver watching the specified directory

    Args:
        watch_path: Directory to watch for code changes
    """
    print(f"Starting RuleWeaver in {watch_path}")

    # Initialize components
    watcher = CodeWatcher(watch_path)
    engine = RuleWeaverEngine()

    # Start watching
    try:
        watcher.start()
        print("Watching for code changes... (press Ctrl+C to exit)")
        while True:
            pass
    except KeyboardInterrupt:
        print("\nStopping RuleWeaver...")
        watcher.stop()