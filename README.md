<div align="center">

<img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/License-GPL--3.0-4CC61E?style=flat-square&logo=osi&logoColor=white" alt="License">
<img src="https://img.shields.io/badge/Version-0.1.0-3B82F6?style=flat-square" alt="Version">
<img src="https://img.shields.io/badge/PRs_Welcome-3B82F6?style=flat-square" alt="PRs Welcome">

<br/>
<br/>

<h3>Dynamic, context-aware .cursorrules generation deployed on the fly.</h3>

<i>RuleWeaver actively monitors the developer's IDE state, git diffs, and terminal errors. It instantly compiles and injects temporary, hyper-optimized rules into the agent's context window, ensuring the AI only receives instructions relevant to the exact line of code currently being edited.</i>

<br/>
<br/>

<a href="#installation"><b>Install</b></a>
&ensp;·&ensp;
<a href="#quick-start"><b>Quick Start</b></a>
&ensp;·&ensp;
<a href="#features"><b>Features</b></a>
&ensp;·&ensp;
<a href="#architecture"><b>Architecture</b></a>
&ensp;·&ensp;
<a href="#demo"><b>Demo</b></a>

</div>

---
## Installation

```bash
pip install ruleweaver
```

## Quick Start

```bash
ruleweaver --help
```

## Architecture

```
ruleweaver/
├── pyproject.toml
├── README.md
├── src/
│   └── ruleweaver/
│       ├── __init__.py
│       └── cli.py
├── tests/
│   └── test_ruleweaver.py
└── AGENTS.md
```

## Demo

<!-- Add screenshot or GIF here -->

> Coming soon

## Development

```bash
git clone https://github.com/avasis-ai/ruleweaver
cd ruleweaver
pip install -e .
pytest tests/ -v
```

## Links

- **Repository**: https://github.com/avasis-ai/ruleweaver
- **PyPI**: https://pypi.org/project/ruleweaver
- **Issues**: https://github.com/avasis-ai/ruleweaver/issues

---

<div align="center">
<i>Part of the <a href="https://github.com/avasis-ai">AVASIS AI</a> open-source ecosystem</i>
</div>
