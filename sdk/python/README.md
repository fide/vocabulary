# Fide Vocabulary — Python SDK

Work in progress. The typed vocabulary surface will be generated from `spec/v0/vocabulary.json` (same source of truth as the JavaScript SDK).

## Development

```bash
cd sdk/python
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

Regenerate `src/chris_test_vocabulary/spec.py` from `spec/v0/vocabulary.json` (run from repo `packages/fide-vocabulary`):

```bash
python scripts/generate-sdk/spec_module.py
```

Build a wheel:

```bash
python -m build
```
