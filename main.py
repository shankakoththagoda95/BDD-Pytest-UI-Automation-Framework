import pytest
import os

# Ensure the working directory is correct
print("Current working directory:", os.getcwd())

# Run pytest programmatically
if __name__ == "__main__":
    pytest.main(["--tb=short", "Automation/"])