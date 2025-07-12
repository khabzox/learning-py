"""
Basic tests for the Python learning repository.
"""
import os
import subprocess
import sys
from pathlib import Path


def test_main_py_exists():
    """Test that main.py exists in the 01-Intro directory."""
    main_file = Path("01-Intro/main.py")
    assert main_file.exists(), "main.py should exist in 01-Intro directory"


def test_main_py_runs():
    """Test that main.py can be executed without errors."""
    main_file = Path("01-Intro/main.py")
    if main_file.exists():
        result = subprocess.run(
            [sys.executable, str(main_file)],
            capture_output=True,
            text=True,
            timeout=30
        )
        assert result.returncode == 0, f"main.py failed with error: {result.stderr}"


def test_readme_files_exist():
    """Test that README files exist in each directory."""
    directories = [
        "01-Intro",
        "02-getting-started", 
        "03-syntax",
        "04-comments",
        "05-variables",
        "06-data-types",
        "07-numbers",
        "08-casting",
        "09-strings"
    ]
    
    for directory in directories:
        readme_path = Path(directory) / "README.md"
        if Path(directory).exists():
            assert readme_path.exists(), f"README.md should exist in {directory}"


def test_python_syntax():
    """Test that Python files have valid syntax."""
    python_files = list(Path(".").rglob("*.py"))
    
    for py_file in python_files:
        if "venv" not in str(py_file) and ".git" not in str(py_file):
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    compile(f.read(), py_file, 'exec')
            except SyntaxError as e:
                assert False, f"Syntax error in {py_file}: {e}"


def test_repository_structure():
    """Test that the repository has the expected structure."""
    required_files = [
        "README.md",
        "LICENSE", 
        ".gitattributes"
    ]
    
    for file_name in required_files:
        file_path = Path(file_name)
        assert file_path.exists(), f"{file_name} should exist in the repository root"


if __name__ == "__main__":
    # Run basic tests
    test_main_py_exists()
    test_main_py_runs()
    test_readme_files_exist()
    test_python_syntax()
    test_repository_structure()
    print("All tests passed!")
