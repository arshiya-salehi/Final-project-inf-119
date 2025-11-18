# Quick Reference Guide

## Essential Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export GOOGLE_API_KEY="your-key"
# OR edit .env file

# Test installation
python test_structure.py
```

### Running
```bash
# Start the factory
python main.py

# Run generated app
bash run_generated_app.sh
# OR
cd generated/conjugator && python gradio_ui.py

# Run tests
cd generated/tests && pytest test_conjugator.py -v
```

## File Locations

| What | Where |
|------|-------|
| Main entry point | `main.py` |
| UI code | `ui/gradio_app.py` |
| Agents | `agents/*.py` |
| MCP implementation | `mcp/*.py` |
| Configuration | `config/api_config.py` |
| Generated code | `generated/conjugator/` |
| Generated tests | `generated/tests/` |
| Usage report | `usage_report.json` |

## Key Classes

### Agents
- `TrackingAgent`: Wraps LLM calls, tracks usage
- `ParserAgent`: Parses requirements → RequirementSpec
- `DesignAgent`: Creates design → DesignSpec
- `CodeGenAgent`: Generates code → GeneratedCode
- `TestAgent`: Generates tests → test files

### MCP
- `MCPServer`: Central message broker
- `MCPClient`: Agent communication interface
- `MCPMessage`: Message structure
- `AgentRole`: Enum of agent types

### Data Models
- `RequirementSpec`: Parsed requirements
- `DesignSpec`: Architecture design
- `GeneratedCode`: Code file structure
- `TestCase`: Test case structure
- `UsageStats`: API usage tracking

## Common Issues

| Problem | Solution |
|---------|----------|
| API key error | Set GOOGLE_API_KEY in .env |
| Import error | Run `pip install -r requirements.txt` |
| Port in use | Change port in config/api_config.py |
| Generated code fails | Normal - LLM may produce imperfect code |
| Tests don't pass | 80% pass rate is acceptable |

## Customization

### Change Model
Edit `config/api_config.py`:
```python
MODEL_NAME = "gemini-2.5-pro"  # More capable
# or
MODEL_NAME = "gemini-2.5-flash-lite"  # Faster, cheaper
```

### Change Port
Edit `config/api_config.py`:
```python
GRADIO_SERVER_PORT = 8080  # Your preferred port
```

### Modify Prompts
Edit the prompt strings in agent files:
- `agents/parser_agent.py` - requirement parsing
- `agents/design_agent.py` - architecture design
- `agents/code_gen_agent.py` - code generation
- `agents/test_agent.py` - test generation

## Example Requirements

### Simple
```
Create an English verb conjugator for present and past tense.
```

### Moderate
```
Build a verb conjugator for English and Spanish.
Support present, past, and future tenses.
Handle irregular verbs.
```

### Complex
```
Create a comprehensive verb conjugator supporting:
- Languages: English, Spanish, French
- Tenses: present, past, future, imperfect, conditional
- Persons: all six (1st/2nd/3rd singular and plural)
- Moods: indicative, subjunctive, imperative
- Handle both regular and irregular verbs
- Provide detailed conjugation tables
- Include pronunciation guides
```

## MCP Message Flow

```
User Input
    ↓
Parser Agent → RequirementSpec → MCP Server
    ↓
Design Agent → DesignSpec → MCP Server
    ↓
Code Gen Agent → GeneratedCode → MCP Server
    ↓
Test Agent → TestCode → MCP Server
    ↓
Tracking Agent → UsageReport
    ↓
Output to User
```

## Testing Checklist

Before submitting:
- [ ] All agents initialize without errors
- [ ] Can parse sample requirements
- [ ] Generates code files
- [ ] Generates test files
- [ ] Usage report is created
- [ ] Generated code is syntactically valid
- [ ] At least 10 test cases generated
- [ ] At least 80% of tests pass
- [ ] README is complete
- [ ] Comments in all code files
- [ ] GitHub repo shared with TA
- [ ] Demo video recorded
- [ ] Written report completed

## Git Commands

```bash
# Initialize repo
git init
git add .
git commit -m "Initial commit: Verb Conjugator Factory"

# Create GitHub repo, then:
git remote add origin <your-repo-url>
git push -u origin main

# Add TA as collaborator
# Go to Settings > Collaborators > Add: jacobk13@uci.edu
```

## Submission Checklist

- [ ] ZIP file of GitHub repository
- [ ] Demo video (.mp4 format)
- [ ] Written report (PDF, minimum 2 pages)
- [ ] Peer evaluation form
- [ ] TA added to GitHub repo
- [ ] All code files have author comments
- [ ] All functions have docstrings

## Contact

- **TA**: jacobk13@uci.edu
- **Course**: IN4MATX 119
- **Project**: Final Project - AI Coder
