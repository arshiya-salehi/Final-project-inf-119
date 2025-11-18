# Setup Guide for Verb Conjugator Factory

## Quick Start

### 1. Get Your Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

### 2. Install Dependencies

```bash
cd verb_conjugator_factory
pip install -r requirements.txt
```

### 3. Configure API Key

**Option A: Using .env file (Recommended)**
```bash
cp .env.example .env
# Edit .env and replace 'your-api-key-here' with your actual API key
```

**Option B: Environment Variable**
```bash
export GOOGLE_API_KEY="your-actual-api-key"
```

**Option C: Direct Edit**
Edit `config/api_config.py` and replace the API key directly.

### 4. Run the Application

```bash
python main.py
```

The Gradio interface will open at `http://localhost:7860`

## Testing the Installation

Run the structure test to verify everything is set up correctly:

```bash
python test_structure.py
```

You should see all tests pass with ✅ marks.

## Using the Application

1. **Enter Requirements**: In the text box, describe what you want:
   ```
   Create a verb conjugator for English and Spanish.
   Support present, past, and future tenses.
   Include irregular verb handling.
   ```

2. **Generate**: Click the "🚀 Generate Application" button

3. **Wait**: The system will:
   - Parse your requirements
   - Design the architecture
   - Generate code
   - Create tests
   - Save usage report

4. **Review Output**: Check the tabs for:
   - Generated code
   - Test cases
   - Usage statistics
   - Running instructions

5. **Run Generated App**: Follow the instructions in the "Instructions" tab

## Running Generated Applications

After generation, you can run the created app:

```bash
# Option 1: Use the provided script
bash run_generated_app.sh

# Option 2: Manual steps
cd generated/conjugator
python gradio_ui.py
```

## Running Tests

```bash
cd generated/tests
pytest test_conjugator.py -v
```

## Troubleshooting

### API Key Issues
**Error**: "API Key not found"
**Solution**: Make sure your API key is set correctly in .env file

### Import Errors
**Error**: "ModuleNotFoundError"
**Solution**: Install all dependencies: `pip install -r requirements.txt`

### Port Already in Use
**Error**: "Address already in use"
**Solution**: Change the port in `config/api_config.py` or kill the process using port 7860

### Generated Code Doesn't Run
**Error**: Various errors in generated code
**Solution**: This is expected - the LLM may generate imperfect code. You can:
- Regenerate with more specific requirements
- Manually fix the generated code
- Adjust the prompts in the agent files

## Project Structure

```
verb_conjugator_factory/
├── agents/              # Multi-agent system
│   ├── parser_agent.py
│   ├── design_agent.py
│   ├── code_gen_agent.py
│   ├── test_agent.py
│   └── tracking_agent.py
├── mcp/                 # Model Context Protocol
│   ├── server.py
│   ├── client.py
│   └── protocol.py
├── config/              # Configuration
│   └── api_config.py
├── ui/                  # User interface
│   └── gradio_app.py
├── utils/               # Utilities
│   └── helpers.py
├── generated/           # Output directory (created on first run)
├── main.py             # Entry point
└── requirements.txt    # Dependencies
```

## Development

### Adding New Agents

1. Create a new agent file in `agents/`
2. Inherit from base patterns in existing agents
3. Register with MCP server if needed
4. Update `agents/__init__.py`

### Modifying Prompts

Edit the prompt strings in each agent's generation methods to customize output.

### Changing Models

Edit `config/api_config.py` to use different Gemini models:
- `gemini-2.5-flash-lite` (fast, cheaper)
- `gemini-2.5-pro` (more capable, expensive)

## Support

For issues or questions:
1. Check this guide
2. Review the code comments
3. Check the REPORT_TEMPLATE.md for detailed explanations
4. Contact your TA: jacobk13@uci.edu

## License

Academic project for IN4MATX 119 - Fall 2025
