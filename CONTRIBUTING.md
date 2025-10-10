# Contributing to HackerBox

First off, thank you for considering contributing to HackerBox! It's people like you that make HackerBox such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs
- Ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/mynameissami/HackerBox/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/mynameissami/HackerBox/issues/new).
- Be sure to include a title and clear description, as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior.

### Suggesting Enhancements
- Open a new issue with a clear title and description.
- Explain why this enhancement would be useful.
- Include any relevant links, screenshots, or documentation.

### Pull Requests
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature/amazing-feature`.
3. Add your changes.
4. Commit your changes: `git commit -m 'Add some amazing feature'`.
5. Push to the branch: `git push origin feature/amazing-feature`.
6. Open a pull request.

## Development Setup

1. Fork and clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
4. Install development dependencies: `pip install -r requirements-dev.txt`
5. Make your changes.
6. Run tests: `pytest`
7. Format your code: `black .`
8. Submit a pull request.

## Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Use type hints for better code documentation.
- Write docstrings for all public functions and classes.

## License
By contributing, you agree that your contributions will be licensed under its GNU Affero General Public License v3.0.
