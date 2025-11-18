# Language Verb Conjugator Factory

A multi-agent system using Model Context Protocol (MCP) that generates code and test cases for a Language Verb Conjugator application.

## Team Members
- [Your Name] - [Student ID]
- [Member 2 Name] - [Student ID]
- [Member 3 Name] - [Student ID]
- [Member 4 Name] - [Student ID] (optional)

## Project Overview
This system takes functional requirements as input and generates:
1. Executable Python code for a verb conjugation application
2. Comprehensive test cases (minimum 10, with 80%+ pass rate)
3. A Gradio-based user interface
4. Model usage tracking reports

## System Architecture

### Multi-Agent System
- **Requirement Parser Agent**: Parses natural language requirements into structured specifications
- **Design Agent**: Creates architecture and data flow design
- **Code Generation Agent**: Generates the conjugator application code
- **Test Generation Agent**: Creates comprehensive test cases
- **UI Generation Agent**: Builds the Gradio interface
- **Tracking Agent**: Monitors and reports model usage

### MCP Integration
The system uses Model Context Protocol for agent communication and coordination.

## Installation

### Prerequisites
- Python 3.8+
- Google Gemini API key (get one at [Google AI Studio](https://makersuite.google.com/app/apikey))

### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd verb_conjugator_factory

# Install dependencies
pip install -r requirements.txt

# Set your API key (choose one method)
# Method 1: Create .env file
cp .env.example .env
# Edit .env and add your API key

# Method 2: Environment variable
export GOOGLE_API_KEY="your-api-key-here"

# Method 3: Edit config file directly
# Edit config/api_config.py

# Test installation
python test_structure.py
```

### Verification
After setup, you should see:
```
✅ ALL STRUCTURE TESTS PASSED!
```

## Usage

### Running the System
```bash
# Start the Gradio UI
python main.py
```

### Using the Web Interface
1. Open your browser to `http://localhost:7860`
2. Enter the requirements for the verb conjugator
3. Click "Generate Application"
4. View generated code, tests, and usage report
5. Follow instructions to run the generated application

### Running Generated Code
```bash
# After generation, run the conjugator
python generated/conjugator/verb_conjugator.py

# Run the tests
python generated/tests/test_conjugator.py

# Or use the provided script
bash run_generated_app.sh
```

## Project Structure
```
verb_conjugator_factory/
├── agents/                 # Multi-agent system components
│   ├── parser_agent.py    # Requirement parsing
│   ├── design_agent.py    # Architecture design
│   ├── code_gen_agent.py  # Code generation
│   ├── test_agent.py      # Test generation
│   ├── ui_agent.py        # UI generation
│   └── tracking_agent.py  # Usage tracking
├── mcp/                    # Model Context Protocol implementation
│   ├── server.py          # MCP server
│   ├── client.py          # MCP client
│   └── protocol.py        # Protocol definitions
├── config/                 # Configuration files
│   └── api_config.py      # API keys and settings
├── generated/              # Generated output
│   ├── conjugator/        # Generated app code
│   └── tests/             # Generated tests
├── ui/                     # User interface
│   └── gradio_app.py      # Gradio interface
├── utils/                  # Utility functions
│   └── helpers.py         # Helper functions
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── run_generated_app.sh   # Script to run generated app
└── README.md              # This file
```

## Model Usage Tracking
The system tracks all API calls and generates a report in JSON format:
```json
{
  "gemini-2.5-flash-lite": {
    "numApiCalls": 15,
    "totalTokens": 45230
  }
}
```

## Demo Video
See `demo_video.mp4` for a complete walkthrough of the system.

## Written Report
See `final_report.pdf` for detailed system design and analysis.

## License
Academic project for IN4MATX 119 - Fall 2025
