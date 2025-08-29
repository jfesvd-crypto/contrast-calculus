All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-08-29

### Added
- Created `examples/quick_start.py` to demonstrate usage.
- Added full project description to `README.md`, which is now displayed on PyPI.

### Changed
- Updated version number to 1.0.1.

## [1.0.0] - 2025-08-28

### Added
- Initial public release of `contrast-calculus`.
- Core implementation of `Braid`, `FusionCategory`, and `cocycle` modules.
- Test suite with validation for the Yang-Baxter relation.
- Interactive visualization notebook for braid diagrams.
- CI workflow with GitHub Actions to run tests automatically.
- Project published to PyPI.
"""

with open('CHANGELOG.md', 'w') as f:
    f.write(changelog_content)

print("CHANGELOG.md has been created successfully.")