import os
import json
import pytest

base_dir = os.path.dirname(os.path.abspath(__file__))

# Load selectors and URLs globally
selectors_path = os.path.join(base_dir, 'web_selectors', 'google_selectors.json')
urls_path = os.path.join(base_dir, 'urls', 'urls.json')

try:
    with open(selectors_path) as f:
        selectors = json.load(f)

    with open(urls_path) as f:
        urls = json.load(f)

    pytest.selectors = selectors
    pytest.urls = urls
except FileNotFoundError as e:
    print(f"File not found: {e}")
