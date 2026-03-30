tests/test_weaver_engine.py
import pytest
from ruleweaver.weaver_engine import RuleWeaverEngine

def test_rule_generation():
    engine = RuleWeaverEngine()
    context = {"current_file": "test.py", "line": 1}
    rules = engine.generate_rules(context)
    assert len(rules) > 0
    assert "id" in rules[0]
    assert "priority" in rules[0]
    assert "conditions" in rules[0]
    assert "actions" in rules[0]