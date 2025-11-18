# Demo Video Instructions

## What to Show in Your Demo Video

### 1. Introduction (30 seconds)
- Show the project structure in your file explorer
- Briefly explain: "This is a multi-agent system that generates verb conjugator applications"
- Show the README.md file

### 2. Starting the Application (30 seconds)
- Open terminal
- Run: `python main.py`
- Show the Gradio interface loading
- Navigate to `http://localhost:7860` in browser

### 3. Entering Requirements (1 minute)
Show the Gradio interface and enter requirements like:

```
Create a Language Verb Conjugator application that supports English and Spanish.

Requirements:
- Support present tense, past tense, and future tense
- Handle both regular and irregular verbs
- Support first person singular, second person singular, and third person singular
- Provide a user-friendly interface where users can input a verb and see all conjugations
- Include comprehensive error handling for invalid inputs
```

Click the "Generate Application" button.

### 4. Generation Process (2-3 minutes)
- Show the status updates as each agent works:
  - "📝 Parsing requirements..."
  - "🎨 Creating design..."
  - "💻 Generating code..."
  - "🧪 Generating tests..."
  - "📊 Saving usage report..."
  - "✅ Generation complete!"

### 5. Review Generated Code (1 minute)
- Click on the "Generated Code" tab
- Scroll through the code briefly
- Point out key components:
  - VerbConjugator class
  - conjugate() method
  - Gradio UI code

### 6. Review Test Cases (1 minute)
- Click on the "Test Cases" tab
- Show that there are 10+ test cases
- Point out different test types:
  - Regular verb tests
  - Irregular verb tests
  - Error handling tests

### 7. Review Usage Report (30 seconds)
- Click on the "Usage Report" tab
- Show the JSON with:
  - Model name
  - Number of API calls
  - Total tokens used
- Example:
```json
{
  "gemini-2.5-flash-lite": {
    "numApiCalls": 5,
    "totalTokens": 12450
  }
}
```

### 8. Review Instructions (30 seconds)
- Click on the "Instructions" tab
- Show the installation and running instructions

### 9. Running the Generated Application (2 minutes)
Open a new terminal and run:

```bash
cd generated/conjugator
pip install mlconjug3 gradio
python gradio_ui.py
```

Show the generated application running:
- Enter a verb (e.g., "speak")
- Select language (English)
- Select tense (present)
- Show the conjugation results

### 10. Running Tests (1 minute)
Open another terminal:

```bash
cd generated/tests
pytest test_conjugator.py -v
```

Show the test results:
- Total tests run (should be 10+)
- Tests passed (should be 8+, ~80%)
- Tests failed (2-3 is acceptable)

### 11. Showing the Code Structure (1 minute)
- Open your code editor
- Show the multi-agent structure:
  - `agents/` folder with all agents
  - `mcp/` folder with MCP implementation
  - Point out key files
- Show comments in one agent file

### 12. Conclusion (30 seconds)
- Summarize what was demonstrated
- Mention the GitHub repository
- Thank the viewer

## Tips for Recording

1. **Screen Resolution**: Use 1920x1080 for clarity
2. **Font Size**: Increase terminal and editor font size
3. **Clean Desktop**: Close unnecessary applications
4. **Rehearse**: Do a practice run first
5. **Narration**: Explain what you're doing as you go
6. **Pace**: Don't rush - give viewers time to see what's happening
7. **Highlight**: Use cursor or highlighting to draw attention to important parts

## If API Calls Fail During Demo

If you encounter API issues during recording:

1. **Pre-generate**: Run the generation before recording and show the results
2. **Edit**: Cut out long waiting times
3. **Explain**: Mention that you're showing pre-generated results due to time constraints
4. **Focus**: Spend more time on the code structure and MCP implementation

## Video Format

- **Format**: .mp4
- **Length**: 8-12 minutes (no strict requirement, but be comprehensive)
- **Quality**: At least 720p, preferably 1080p
- **Audio**: Clear narration (use a decent microphone)
- **Editing**: Basic cuts are fine, no need for fancy effects

## What Graders Look For

1. ✅ Complete end-to-end demonstration
2. ✅ Requirements input through GUI
3. ✅ Code generation process
4. ✅ Test case generation
5. ✅ Generated code runs properly
6. ✅ At least 10 test cases with 8+ passing
7. ✅ Usage tracking report displayed
8. ✅ Clear explanation of the system

## Recording Tools

- **macOS**: QuickTime Player (built-in) or OBS Studio
- **Windows**: OBS Studio or Xbox Game Bar
- **Linux**: OBS Studio or SimpleScreenRecorder
- **Online**: Loom (easy to use)

Good luck with your demo! 🎬
