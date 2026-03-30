# RuleWeaver (#3)

## Tagline
Dynamic, context-aware .cursorrules generation deployed on the fly.

## What It Does
RuleWeaver actively monitors the developer's IDE state, git diffs, and terminal errors. It instantly compiles and injects temporary, hyper-optimized rules into the agent's context window, ensuring the AI only receives instructions relevant to the exact line of code currently being edited.

## Inspired By
Cursor (.cursorrules), Continue.dev, LangChain + Context auto-pruning

## Viral Potential
Solves the massive, high-frequency pain point of AI context bloat in large repositories. Delivers a magic wow-factor during live video demos where rules rewrite themselves. Works invisibly in the background, requiring zero manual configuration.

## Unique Defensible Moat
A patented Abstract Syntax Tree (AST) routing algorithm maps complex code changes to optimal prompt injections with near-zero latency, creating a performance breakthrough highly resistant to reverse-engineering by generic wrapper startups.

## Repo Starter Structure
/watcher, /weaver-engine, GPLv3, VS Code/Cursor extension boilerplate

## Metadata
- **License**: GPL-3.0
- **Org**: avasis-ai
- **PyPI**: ruleweaver
- **Dependencies**: tree-sitter>=0.20, watchdog>=3.0, pyyaml>=6.0
