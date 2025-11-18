# Configuration for API keys and model settings
# Author: [Your Name] - [Student ID]

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')

# Validate API key
if not GOOGLE_API_KEY or GOOGLE_API_KEY == 'your-api-key-here':
    print("⚠️  WARNING: GOOGLE_API_KEY not set!")
    print("Please set your API key in one of these ways:")
    print("1. Create a .env file with: GOOGLE_API_KEY=your-key")
    print("2. Set environment variable: export GOOGLE_API_KEY=your-key")
    print("3. Edit config/api_config.py directly")

# Model Configuration
MODEL_NAME = "gemini-2.5-flash-lite"
MODEL_TEMPERATURE = 0.7
MODEL_MAX_TOKENS = 8192

# MCP Configuration
MCP_SERVER_HOST = "localhost"
MCP_SERVER_PORT = 8000

# Generation Configuration
OUTPUT_DIR = "generated"
CONJUGATOR_DIR = f"{OUTPUT_DIR}/conjugator"
TESTS_DIR = f"{OUTPUT_DIR}/tests"
USAGE_REPORT_FILE = "usage_report.json"

# UI Configuration
GRADIO_SERVER_NAME = "0.0.0.0"
GRADIO_SERVER_PORT = 7860
GRADIO_SHARE = False
