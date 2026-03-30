# AGENTS.md - RuleWeaver Project

## Project Overview
RuleWeaver is a dynamic, context-aware rule generation system that enhances AI interactions by injecting optimized rules based on real-time code changes.

## Development Notes
- Use `tree-sitter` for AST analysis
- `watchdog` for file change monitoring
- `pyyaml` for configuration management

## Implementation Status
- [x] Core engine implementation
- [x] Watcher system
- [x] CLI interface
- [ ] Full AST routing algorithm
- [ ] Integration with VS Code/Cursor

## Testing
- pytest coverage: 75%
- Unit tests for core components
- Integration tests pending

## Next Steps
1. Implement full AST routing algorithm
2. Add VS Code/Cursor extension support
3. Optimize rule injection performance