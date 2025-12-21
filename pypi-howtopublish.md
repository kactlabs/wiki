/ [Home](index.md)

## PyPI - How To Publish - Updated


# PyPI Publishing Checklist

## Before Publishing

- [ ] Update version number in `setup.py` and `pyproject.toml`
- [ ] Update your name and email in `setup.py` and `pyproject.toml`
- [ ] Update GitHub URLs to your actual repository
- [ ] Test your package locally
- [ ] Ensure all dependencies are in `requirements.txt`

## Required Tools

Install the required publishing tools:

```bash
pip install build twine
```

## Publishing Steps

### 1. Clean Previous Builds
```bash
rm -rf dist/ build/ *.egg-info/
```

### 2. Build the Package
```bash
python -m build
```

### 3. Check the Package
```bash
twine check dist/*
```

### 4. Test Upload (Optional)
Upload to TestPyPI first to test:

```bash
twine upload --repository testpypi dist/*
```

Test install from TestPyPI:
```bash
pip install --index-url https://test.pypi.org/simple/ webtable2json
```

### 5. Upload to PyPI
```bash
twine upload dist/*
```

### 6. Verify Installation
```bash
pip install webtable2json
python -c "import webtable2json; print('Success!')"
```

## PyPI Account Setup

1. Create account at: https://pypi.org/account/register/
2. Enable 2FA
3. Generate API token at: https://pypi.org/manage/account/token/
4. Use `__token__` as username and your token as password when prompted

## Files Created for Publishing

- `setup.py` - Package configuration (legacy)
- `pyproject.toml` - Modern package configuration
- `MANIFEST.in` - Include additional files
- `LICENSE` - MIT license
- `README.md` - Updated with usage examples
- `publish.py` - Helper script for publishing

## Important Notes

- Package name `webtable2json` must be unique on PyPI
- Version numbers should follow semantic versioning (1.0.0, 1.0.1, etc.)
- Once uploaded, you cannot replace a version - you must increment the version number
- Test thoroughly before publishing to avoid issues