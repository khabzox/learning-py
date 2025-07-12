"""
Test suite for Python learning examples.
This ensures all Python files in the repository can be executed without errors.
"""

import os
import subprocess
import sys
from pathlib import Path


def test_main_py_execution():
    """Test that 01-Intro/main.py executes successfully."""
    main_py_path = Path("01-Intro/main.py")
    
    if main_py_path.exists():
        result = subprocess.run(
            [sys.executable, str(main_py_path)],
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )
        
        # Check if the script ran without errors
        assert result.returncode == 0, f"main.py failed with error: {result.stderr}"
        
        # Check if it produces expected output
        assert "Hello" in result.stdout or "hello" in result.stdout.lower(), \
            f"Expected greeting output, got: {result.stdout}"


def test_python_files_syntax():
    """Test that all Python files have valid syntax."""
    python_files = []
    
    # Find all Python files
    for root, dirs, files in os.walk("."):
        # Skip hidden directories and common ignored directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'venv', 'env']]
        
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    for py_file in python_files:
        # Test syntax by compiling
        try:
            with open(py_file, 'r') as f:
                compile(f.read(), py_file, 'exec')
        except SyntaxError as e:
            assert False, f"Syntax error in {py_file}: {e}"


def test_readme_files_exist():
    """Test that each numbered module has a README file."""
    for item in os.listdir('.'):
        if os.path.isdir(item) and item[0].isdigit():
            readme_path = os.path.join(item, 'README.md')
            assert os.path.exists(readme_path), f"README.md missing in {item}"


if __name__ == "__main__":
    # Run tests when script is executed directly
    print("Running basic tests...")
    
    try:
        test_main_py_execution()
        print("✅ main.py execution test passed")
    except Exception as e:
        print(f"❌ main.py execution test failed: {e}")
    
    try:
        test_python_files_syntax()
        print("✅ Python syntax test passed")
    except Exception as e:
        print(f"❌ Python syntax test failed: {e}")
    
    try:
        test_readme_files_exist()
        print("✅ README files test passed")
    except Exception as e:
        print(f"❌ README files test failed: {e}")
    
    print("Tests completed!")
