# Changelog
[![Common Changelog](https://common-changelog.org/badge.svg)](https://common-changelog.org)

## NEXT

### Changed

- Changed to use pre-commit hooks to check `CHANGELOG.md`

## [0.11.0] - 2025-03-02

### Changed

- Enhanced project documentation with structure overview, workflow guides, and setup instructions.

## [0.10.0] - 2025-03-02

### Changed

- Integrated bump-my-version configuration directly in pyproject.toml

## [0.9.0] - 2025-03-02

### Added

- Added revert main branch and tag in `version_bump.yml`

## [0.8.0] - 2025-03-02

### Changed

- Changed the automatic reversion when push to main fails
- Test

## [0.7.0] - 2025-03-02

### Changed

- Changed WORKFLOW_TOKEN to VERSIONING_WORKFLOW_TOKEN

### Added

- Added tag verification and automatic reversion in `version_bump.yml`

## [0.6.0] - 2025-03-01

### Added

- Document branch protection configuration and setup in README.md
- Do not enforce admin to the branch protection rules

## [0.5.0] - 2025-03-01

### Added

- Add token to push changes to main from workflow

## [0.4.0] - 2025-03-01

### Added

- Added user to push changes to main from workflow

### Changed

- Add branch protection rules to enforce proper changelog format and block merging if checks fail
- Configure branch protection to allow automated version bumping via github-actions[bot]


## [0.3.0] - 2025-03-01

### Added

- Introduced check for CHANGELOG.md

## [0.2.0] - 2025-03-01

### Added

- Introduced CHANGELOG.md
