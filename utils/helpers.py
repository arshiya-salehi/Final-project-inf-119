# Utility helper functions
# Author: [Your Name] - [Student ID]

import os
import json
from typing import Dict, Any

def ensure_directory(path: str) -> None:
    """
    Ensure a directory exists, create if it doesn't.
    
    Args:
        path: Directory path to create
    """
    os.makedirs(path, exist_ok=True)

def save_to_file(content: str, filepath: str) -> None:
    """
    Save content to a file.
    
    Args:
        content: Content to save
        filepath: Path to save the file
    """
    ensure_directory(os.path.dirname(filepath))
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def load_from_file(filepath: str) -> str:
    """
    Load content from a file.
    
    Args:
        filepath: Path to the file
        
    Returns:
        File content as string
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def save_json(data: Dict[str, Any], filepath: str) -> None:
    """
    Save data as JSON file.
    
    Args:
        data: Dictionary to save
        filepath: Path to save the JSON file
    """
    ensure_directory(os.path.dirname(filepath))
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def load_json(filepath: str) -> Dict[str, Any]:
    """
    Load JSON file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Dictionary from JSON
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_code_block(text: str) -> str:
    """
    Remove markdown code block markers from text.
    
    Args:
        text: Text potentially containing markdown code blocks
        
    Returns:
        Cleaned text
    """
    # Remove ```python and ``` markers
    if text.startswith("```python"):
        text = text.replace("```python", "", 1)
    if text.startswith("```"):
        text = text.replace("```", "", 1)
    if text.endswith("```"):
        text = text.rsplit("```", 1)[0]
    return text.strip()
