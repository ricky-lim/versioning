# Versioning

A demonstration project for Python versioning using bump-my-version.

## Project Structure

```
versioning/
├── .github/
│   └── workflows/         # GitHub Actions workflows
├── src/                   # Source code directory
│   └── demo/              # Main package directory
│       ├── __init__.py
│       └── cli.py         # CLI implementation
├── CHANGELOG.md           # Version history and changes
├── pyproject.toml         # Project configuration and dependencies
└── README.md              # Project documentation
```

## Requirements

- Python >= 3.12
- bump-my-version >= 0.32.2
- pre-commit >= 4.1.0 (for development)

## Version Management
This project uses bump-my-version for version management. Version configuration is maintained in pyproject.toml.

To bump version:

```bash
bump-my-version bump patch  # For patch version: 0.9.0 -> 0.9.1
bump-my-version bump minor  # For minor version: 0.9.0 -> 0.10.0
bump-my-version bump major  # For major version: 0.9.0 -> 1.0.0
```

## How to develop

- Create a new branch for your work

```
# Get the latest version including tags
git pull origin --tags

# Create a new branch for your work
# For features
git checkout -b feature/my-feature

# For bug fixes
git checkout -b bugfix/my-bugfix

# For releases
git checkout -b release/my-release

# Work and commit your changes
```

- Manual curation of CHANGELOG.md

Add your changes under the `## NEXT` section in CHANGELOG.md.
The GitHub Actions workflow automatically converts the "NEXT" section to the new version number and adds the release date when performing version bumps.
This ensures consistent versioning and release documentation.

Example structure:

```markdown
## NEXT

### Added
- New feature for user authentication
- Support for PostgreSQL database

### Changed
- Migrated version configuration from .bumpversion.toml to pyproject.toml
- Updated Python requirement to 3.12

### Fixed
- Database connection timeout issue
- Memory leak in background worker

### Removed
- Deprecated legacy API endpoints
- Old configuration format support
```

- Commit your changes
- Create a pull request to merge your changes into the main branch
- Wait for the pull request to be reviewed and merged
- The GitHub Actions workflow will automatically bump the version and create a new tag

## CHANGELOG

All notable changes to this project are documented in [CHANGELOG.md](CHANGELOG.md).

## Creating GitHub Token for Versioning Workflow

- Go to GitHub Settings > Developer Settings > Personal Access Tokens > Fine-grained tokens
- Click "Generate new token"
- Name your token: `VERSIONING_WORKFLOW_TOKEN`
- Set expiration as needed
- Select repository access: "Only select repositories" and choose your repository
- Select these permissions:

```
Repository permissions:
Contents: Read and write
Metadata: Read-only
Pull requests: Read and write
Workflows: Read and write
```

- Add token to repository:

  - Go to repository Settings > Secrets and variables > Actions
  - Click "New repository secret"
  - Name: VERSIONING_WORKFLOW_TOKEN
  - Value: Paste your generated token


## Add branch protection rules

```bash
gh api --method PUT /repos/ricky-lim/versioning/branches/main/protection --input branch-protection-rules.json
```
