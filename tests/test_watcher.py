tests/test_watcher.py
import pytest
from ruleweaver.watcher import CodeWatcher, ASTEventHandler

@pytest.fixture
def test_dir(tmpdir):
    return str(tmpdir.mkdir("test_project"))

def test_watcher_initialization(test_dir):
    watcher = CodeWatcher(test_dir)
    assert watcher.watch_path == test_dir
    assert isinstance(watcher.event_handler, ASTEventHandler)

def test_event_handler(test_dir):
    event_handler = ASTEventHandler()
    # Test event handling logic here
    # Would create temporary files and trigger events
    pass