# Learning Python 🐍

[![CI/CD](https://github.com/khabzox/learning-py/actions/workflows/ci.yml/badge.svg)](https://github.com/khabzox/learning-py/actions/workflows/ci.yml)
[![Learning Progress](https://github.com/khabzox/learning-py/actions/workflows/learning-progress.yml/badge.svg)](https://github.com/khabzox/learning-py/actions/workflows/learning-progress.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive Python learning journey covering fundamental concepts and practical examples. This repository contains structured lessons and exercises to help you master Python programming from the ground up.

## 📚 Course Structure

The course is organized into progressive modules, each building upon the previous one:

### 📖 Module Overview

- **[01-Intro](./01-Intro/)** - Introduction to Python programming
- **[02-getting-started](./02-getting-started/)** - Setting up your Python environment
- **[03-syntax](./03-syntax/)** - Python syntax fundamentals
- **[04-comments](./04-comments/)** - Writing effective comments
- **[05-variables](./05-variables/)** - Working with variables and data types
  - **[01-names](./05-variables/01-names/)** - Variable naming conventions
  - **[02-assign-multiple-values](./05-variables/02-assign-multiple-values/)** - Multiple variable assignment
  - **[03-output-variables](./05-variables/03-output-variables/)** - Displaying and outputting variables
  - **[04-global-variables](./05-variables/04-global-variables/)** - Understanding global vs local scope
- **[06-data-types](./06-data-types/)** - Python data types and their usage
- **[07-numbers](./07-numbers/)** - Working with numeric data types
- **[08-casting](./08-casting/)** - Type conversion and casting in Python
- **[09-strings](./09-strings/)** - String manipulation and methods
  - **[01-slicing-strings](./09-strings/01-slicing-strings/)** - String slicing techniques
  - **[02-modify-strings](./09-strings/02-modify-strings/)** - String modification and transformation

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Text editor or IDE (VS Code, PyCharm, etc.)
- Basic computer literacy

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/khabzox/learning-py.git
   cd learning-py
   ```

2. Verify Python installation:

   ```bash
   python --version
   ```

3. (Optional) Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate     # On Windows
   ```

4. Install development dependencies (optional):

   ```bash
   pip install -r requirements.txt
   ```

5. Start with the first module:

   ```bash
   cd 01-Intro
   python main.py
   ```

## �️ Development & Automation

This repository includes automated workflows and tools to ensure code quality and track learning progress:

### 🔄 GitHub Actions Workflows

- **CI/CD Pipeline**: Automatically tests Python code, runs linting, and validates markdown
- **Learning Progress Tracker**: Generates progress reports and completion statistics
- **Auto-formatting**: Keeps code formatted consistently using Black and isort
- **Release Automation**: Creates automatic releases when new modules are added

### 🧰 Development Tools

- **Black**: Code formatter for consistent Python styling
- **isort**: Import sorter for clean import organization  
- **pylint**: Static code analysis for Python
- **markdownlint**: Ensures consistent markdown formatting
- **pytest**: Testing framework for Python code validation

### 📊 Quality Assurance

All code is automatically:
- ✅ Formatted with Black
- ✅ Linted with pylint
- ✅ Import-sorted with isort
- ✅ Tested with pytest
- ✅ Markdown validated

## �📝 How to Use This Repository

1. **Sequential Learning**: Follow the modules in order (01, 02, 03, etc.)
2. **Hands-on Practice**: Each module contains practical examples and exercises
3. **Read the Documentation**: Each folder has its own README with specific instructions
4. **Experiment**: Modify the code examples to deepen your understanding
5. **Track Progress**: Use the automated progress tracking to monitor your learning journey
6. **Code Quality**: All examples follow Python best practices and are automatically tested

## 🎯 Learning Objectives

By completing this course, you will:

- ✅ Understand Python syntax and fundamentals
- ✅ Learn proper coding conventions and best practices
- ✅ Master variable declaration and manipulation
- ✅ Write clean, readable Python code
- ✅ Build a solid foundation for advanced Python topics

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome! Feel free to:

- Open an issue for questions or suggestions using our [issue templates](.github/ISSUE_TEMPLATE/)
- Submit a pull request for improvements
- Share your learning experience
- Suggest new learning modules or exercises

### 🐛 Found a Bug?

If you find any issues with the code examples or documentation:
1. Check existing issues first
2. Create a new issue with detailed information
3. Include steps to reproduce the problem
4. Mention your operating system and Python version

### 💡 Have a Learning Suggestion?

Use our learning suggestion template to propose:
- New topics to cover
- Improved explanations
- Additional exercises
- Better examples

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔧 Repository Features

### ⚡ Automated Workflows
- **Continuous Integration**: Every push triggers automated testing and validation
- **Progress Tracking**: Automatic generation of learning progress reports
- **Code Quality**: Automated formatting and linting ensure consistent code style
- **Release Management**: Automatic versioning and release notes

### 📋 Issue Templates
- Bug Report Template for reporting code issues
- Learning Suggestion Template for proposing improvements
- Feature Request Template for new functionality

### 🔍 Code Quality Tools
```bash
# Run all quality checks locally
pylint **/*.py          # Static code analysis
black **/*.py           # Code formatting
isort **/*.py           # Import sorting
pytest                  # Run tests
```

---

## Happy Learning! 🎉

_Remember: The best way to learn programming is by doing. Don't just read the code - run it, modify it, and experiment with it!_

### 📈 Learning Tips

1. **Practice Daily**: Consistency is key to mastering programming
2. **Understand, Don't Memorize**: Focus on understanding concepts rather than memorizing syntax
3. **Build Projects**: Apply what you learn by building small projects
4. **Debug Actively**: When you encounter errors, use them as learning opportunities
5. **Join Communities**: Engage with other Python learners and developers
6. **Read Code**: Study well-written Python code from open-source projects

### 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Weekly Newsletter](https://pythonweekly.com/)
- [Awesome Python](https://github.com/vinta/awesome-python) - Curated list of Python resources
