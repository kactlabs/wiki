# PyPI Publishing Steps

Quick reference guide for publishing Python packages to PyPI.

## Prerequisites

1. **PyPI Account**: Create account at https://pypi.org/account/register/
2. **API Token**: Generate API token at https://pypi.org/manage/account/
3. **Build Tools**: `pip install build twine`

## Authentication Setup

Choose one method:

### Option 1: Environment Variables
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=your_pypi_token_here
```

### Option 2: .pypirc Configuration
Create `~/.pypirc`:
```ini
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = your_pypi_token_here
```

## Publishing Steps

### 1. Pre-Publishing Checklist
- [ ] All tests pass
- [ ] Code is formatted and linted
- [ ] Version number updated in `pyproject.toml`
- [ ] README is up to date
- [ ] All changes committed to git

### 2. Build Package
```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build
```

### 3. Validate Package
```bash
# Check package integrity
twine check dist/*

# Inspect package contents (optional)
tar -tzf dist/your-package-*.tar.gz
```

### 4. Upload to PyPI
```bash
# Upload to PyPI
twine upload dist/*

# Or with verbose output
twine upload --verbose dist/*
```

### 5. Verify Publication
1. Check package page: `https://pypi.org/project/your-package/`
2. Test installation: `pip install your-package`
3. Test functionality

## Version Management

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- Update version in `pyproject.toml` and package `__init__.py`

## Quick Commands

```bash
# Complete publishing workflow
python -m build && twine check dist/* && twine upload dist/*

# Test installation after publishing
pip install --upgrade your-package-name

# Check package info
pip show your-package-name
```

## Common Issues

1. **Authentication Error**: Check API token configuration
2. **Version Already Exists**: Increment version number and rebuild
3. **Missing Files**: Check `MANIFEST.in` or `pyproject.toml` includes
4. **Import Errors**: Verify package structure and dependencies

## Security Notes

- Never commit API tokens to version control
- Use environment variables or `.pypirc` for credentials
- Enable 2FA on PyPI account
- Consider project-specific tokens for better security

## Test PyPI (Optional)

For testing before production:
```bash
# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ your-package
