src/ruleweaver/watcher.py
"""
Monitors IDE state, git diffs, and terminal errors
"""

import os
import yaml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CodeWatcher:
    """Watches code changes and triggers rule updates"""

    def __init__(self, watch_path: str):
        self.watch_path = watch_path
        self.observer = Observer()
        self.event_handler = self._create_event_handler()

    def _create_event_handler(self):
        """Create event handler with AST routing"""
        return ASTEventHandler()

    def start(self):
        """Start watching the directory"""
        self.observer.schedule(self.event_handler, self.watch_path, recursive=True)
        self.observer.start()

    def stop(self):
        """Stop the watcher"""
        self.observer.stop()
        self.observer.join()


class ASTEventHandler(FileSystemEventHandler):
    """Handles file system events with AST analysis"""

    def on_modified(self, event):
        """Handle file modifications"""
        if event.is_directory:
            return
        
        # AST routing logic here
        # Would analyze the changed file's AST
        # and trigger rule updates accordingly
        print(f"File modified: {event.src_path}")
