# Final Project Report: Language Verb Conjugator Factory

**Course:** IN4MATX 119 - Software Engineering  
**Team Members:**
- [Name 1] - [Student ID 1]
- [Name 2] - [Student ID 2]
- [Name 3] - [Student ID 3]
- [Name 4] - [Student ID 4] (optional)

**Date:** November 2025  
**GitHub Repository:** [Your Repository URL]

---

## 1. Introduction

### Purpose of the System

The Language Verb Conjugator Factory is an innovative multi-agent system that automatically generates complete verb conjugation applications from natural language requirements. Unlike traditional software development where programmers manually write code, our system acts as an "application factory" that produces working software on demand.

The system addresses a real-world need: language learners require tools to practice verb conjugation across different languages, tenses, and grammatical forms. Rather than building separate applications for each language combination, our factory generates custom conjugator applications tailored to specific requirements.

**Key Capabilities:**
- Accepts natural language descriptions of desired functionality
- Generates executable Python code for verb conjugation
- Creates comprehensive test suites (10+ tests with 80%+ pass rate)
- Builds user-friendly Gradio interfaces
- Tracks and reports all AI model usage

**Target Users:**
- Language learning platforms
- Educational institutions
- Individual language learners
- Developers needing quick prototypes

### Problem Statement

Manual development of language learning tools is time-consuming and repetitive. Each new language or feature combination requires significant development effort. Our system automates this process using AI agents that collaborate through the Model Context Protocol (MCP) to transform requirements into working applications.

---

## 2. System Design and Workflow

### Overall Architecture

Our system implements a **multi-agent architecture** where specialized agents collaborate to complete complex tasks. The architecture follows these principles:

1. **Separation of Concerns**: Each agent has a specific responsibility
2. **Loose Coupling**: Agents communicate via MCP, not direct calls
3. **Modularity**: Components can be modified independently
4. **Scalability**: New agents can be added easily

**Architecture Diagram:**

```
┌─────────────────────────────────────────────────────────┐
│                    Gradio UI Layer                       │
│              (User Input/Output Interface)               │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              MCP Communication Layer                     │
│         (Message Passing & Coordination)                 │
└─┬──────┬──────┬──────┬──────┬──────────────────────────┘
  │      │      │      │      │
  ▼      ▼      ▼      ▼      ▼
┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐
│ P │  │ D │  │ C │  │ T │  │ T │  Agent Layer
│ a │  │ e │  │ o │  │ e │  │ r │
│ r │  │ s │  │ d │  │ s │  │ a │
│ s │  │ i │  │ e │  │ t │  │ c │
│ e │  │ g │  │   │  │   │  │ k │
│ r │  │ n │  │ G │  │ G │  │ i │
│   │  │   │  │ e │  │ e │  │ n │
│   │  │   │  │ n │  │ n │  │ g │
└───┘  └───┘  └───┘  └───┘  └───┘
```

### Input Parsing Process

The **Parser Agent** transforms natural language into structured data:

**Input Example:**
```
Create a verb conjugator for English and Spanish.
Support present, past, and future tenses.
Include irregular verb handling.
```

**Parsing Steps:**
1. **LLM Analysis**: Send requirements to Gemini with structured prompt
2. **JSON Extraction**: Parse LLM response into JSON format
3. **Validation**: Use Pydantic models to validate structure
4. **Default Handling**: Fill in missing fields with reasonable defaults

**Output (RequirementSpec):**
```json
{
  "languages": ["English", "Spanish"],
  "tenses": ["present", "past", "future"],
  "persons": ["1st singular", "2nd singular", "3rd singular"],
  "moods": ["indicative"],
  "handle_irregular": true,
  "dataset_sources": [],
  "additional_requirements": ""
}
```

### Data Flow Through the System

**Complete Pipeline:**

```
1. User Input (Natural Language)
   ↓
2. Parser Agent
   - Sends to Gemini LLM
   - Extracts structured data
   - Creates RequirementSpec
   ↓
3. Design Agent
   - Receives RequirementSpec via MCP
   - Determines architecture
   - Selects dependencies
   - Creates DesignSpec
   ↓
4. Code Generation Agent
   - Receives DesignSpec via MCP
   - Generates conjugator module
   - Generates UI code
   - Saves to files
   ↓
5. Test Generation Agent
   - Receives generated code via MCP
   - Creates pytest test cases
   - Ensures 80%+ coverage
   - Saves test file
   ↓
6. Tracking Agent
   - Monitors all LLM calls
   - Counts tokens
   - Generates usage report
   ↓
7. Output to User
   - Generated code files
   - Test cases
   - Usage statistics
   - Running instructions
```

**Data Transformations:**

| Stage | Input | Output | Format |
|-------|-------|--------|--------|
| Parser | Text | RequirementSpec | Pydantic model |
| Design | RequirementSpec | DesignSpec | Pydantic model |
| Code Gen | DesignSpec | Python files | .py files |
| Test Gen | Python files | Test file | pytest file |
| Tracking | All stages | Usage report | JSON |

### Workflow Description

**Step-by-Step Process:**

1. **Initialization**
   - User starts application (`python main.py`)
   - Gradio UI launches on port 7860
   - All agents initialize
   - MCP server starts

2. **Requirement Entry**
   - User enters requirements in text box
   - Clicks "Generate Application" button
   - UI sends requirements to backend

3. **Parsing Phase**
   - Parser Agent receives requirements
   - Calls Gemini LLM with structured prompt
   - Extracts languages, tenses, persons, etc.
   - Validates and creates RequirementSpec
   - Broadcasts via MCP

4. **Design Phase**
   - Design Agent receives RequirementSpec
   - Calls Gemini for architecture decisions
   - Determines modules needed
   - Selects appropriate libraries
   - Creates DesignSpec
   - Sends to Code Gen Agent via MCP

5. **Code Generation Phase**
   - Code Gen Agent receives DesignSpec
   - Generates main conjugator module
   - Generates Gradio UI code
   - Validates syntax
   - Saves files to `generated/conjugator/`
   - Notifies Test Agent via MCP

6. **Test Generation Phase**
   - Test Agent receives generated code
   - Creates 10+ test cases
   - Includes regular/irregular verb tests
   - Includes error handling tests
   - Saves to `generated/tests/`

7. **Reporting Phase**
   - Tracking Agent compiles statistics
   - Generates JSON usage report
   - Saves to `usage_report.json`

8. **Output Phase**
   - All results returned to UI
   - User sees generated code
   - User sees test cases
   - User sees usage report
   - User gets running instructions

---

## 3. Model Roles and Tools

### Agent Responsibilities

#### 1. Tracking Agent

**Role:** Central API gateway and usage monitor

**Responsibilities:**
- Wrap all Gemini API calls
- Count tokens for each request
- Track number of API calls
- Generate usage reports
- Handle API errors

**Tools Used:**
- `google.generativeai`: Gemini API client
- `pydantic`: Data validation for UsageStats
- File I/O: Save JSON reports

**Why This Design:**
- Centralizes API access for consistent tracking
- Prevents duplicate tracking code
- Provides transparent usage reporting
- Enables rate limiting if needed

**MCP Usage:**
- Broadcasts API call notifications
- Sends error messages on failures
- Notifies when reports are saved

**Code Example:**
```python
def generate_content(self, prompt: str) -> str:
    response = self.model.generate_content(prompt)
    tokens = response.usage_metadata.total_token_count
    self.usage_stats[MODEL_NAME].add_call(tokens)
    self.mcp_client.notify({"event": "api_call", "tokens": tokens})
    return response.text
```

#### 2. Parser Agent

**Role:** Natural language to structured data converter

**Responsibilities:**
- Parse user requirements
- Extract languages, tenses, persons
- Handle ambiguous inputs
- Provide reasonable defaults
- Validate output structure

**Tools Used:**
- Tracking Agent: For LLM calls
- Gemini LLM: Natural language understanding
- Pydantic: RequirementSpec validation
- JSON parsing: Structure extraction

**Why This Design:**
- LLMs excel at understanding natural language
- Structured output enables downstream processing
- Validation catches errors early
- Defaults handle incomplete inputs

**MCP Usage:**
- Receives requirements from UI
- Sends RequirementSpec to Design Agent
- Notifies on parsing completion/errors

**Prompt Engineering:**
```python
prompt = f"""
Parse the following requirements and extract:
1. Languages to support
2. Tenses to support
3. Persons to support
...
Return ONLY a JSON object with this structure:
{{
    "languages": [...],
    "tenses": [...],
    ...
}}
"""
```

#### 3. Design Agent

**Role:** Software architect

**Responsibilities:**
- Determine system architecture
- Select appropriate libraries
- Define module structure
- Plan data schemas
- Create implementation strategy

**Tools Used:**
- Tracking Agent: For LLM calls
- Gemini LLM: Architecture decisions
- Pydantic: DesignSpec validation

**Why This Design:**
- Separates architecture from implementation
- Allows for design review before coding
- LLM can suggest best practices
- Modular design improves maintainability

**MCP Usage:**
- Receives RequirementSpec from Parser
- Sends DesignSpec to Code Gen Agent
- Broadcasts design decisions

#### 4. Code Generation Agent

**Role:** Application code generator

**Responsibilities:**
- Generate main conjugator module
- Generate Gradio UI code
- Ensure code is syntactically valid
- Include error handling
- Add helpful comments

**Tools Used:**
- Tracking Agent: For LLM calls
- Gemini LLM: Code generation
- File I/O: Save generated files
- Syntax validation: Check code validity

**Why This Design:**
- LLMs are effective at code generation
- Separate generation from testing
- File-based output for easy inspection
- Validation prevents broken code

**MCP Usage:**
- Receives DesignSpec from Design Agent
- Sends generated code to Test Agent
- Notifies on generation completion

**Generation Strategy:**
```python
def _generate_conjugator(self, spec, design):
    prompt = f"""
    Generate a Python module for verb conjugation with:
    - Languages: {spec.languages}
    - Tenses: {spec.tenses}
    - Use mlconjug3 library
    - Include error handling
    Return ONLY the code.
    """
    code = self.tracking_agent.generate_content(prompt)
    return clean_code_block(code)
```

#### 5. Test Generation Agent

**Role:** Quality assurance engineer

**Responsibilities:**
- Generate comprehensive test cases
- Ensure 10+ tests created
- Target 80%+ pass rate
- Cover regular and irregular verbs
- Include edge cases

**Tools Used:**
- Tracking Agent: For LLM calls
- Gemini LLM: Test generation
- pytest framework: Test structure
- File I/O: Save test files

**Why This Design:**
- Automated testing ensures quality
- LLM can generate diverse test cases
- pytest is industry standard
- Separate testing from implementation

**MCP Usage:**
- Receives generated code from Code Gen
- Notifies on test completion
- Reports test statistics

### Model Context Protocol (MCP) Implementation

**What is MCP:**
Model Context Protocol is our custom communication framework that enables agents to exchange messages without direct dependencies.

**Core Components:**

1. **MCPServer** (`mcp/server.py`)
   - Central message broker
   - Routes messages between agents
   - Maintains message history
   - Manages agent queues

2. **MCPClient** (`mcp/client.py`)
   - Agent communication interface
   - Sends requests/responses
   - Receives messages
   - Handles errors

3. **MCPMessage** (`mcp/protocol.py`)
   - Structured message format
   - Message types: REQUEST, RESPONSE, ERROR, NOTIFICATION
   - Sender/receiver identification
   - Content payload

4. **Data Models** (`mcp/protocol.py`)
   - RequirementSpec
   - DesignSpec
   - GeneratedCode
   - TestCase
   - UsageStats

**Why MCP:**
- **Loose Coupling**: Agents don't directly call each other
- **Flexibility**: Easy to add/remove agents
- **Debugging**: Message history for troubleshooting
- **Scalability**: Can distribute agents across processes
- **Testability**: Can mock messages for testing

**Message Flow Example:**
```python
# Parser sends to Design Agent
parser_client.send_request(
    receiver=AgentRole.DESIGN,
    content={"spec": requirement_spec.model_dump()}
)

# Design Agent receives
message = design_client.receive_message(timeout=5.0)
if message.message_type == MessageType.REQUEST:
    spec = RequirementSpec(**message.content["spec"])
    # Process...
```

**MCP Benefits:**
- Agents can be developed independently
- Easy to test individual agents
- Clear communication contracts
- Message history aids debugging
- Can add monitoring/logging easily

---

## 4. Error Handling

### Fault Tolerance Strategies

#### 1. LLM API Failures

**Potential Issues:**
- Network timeouts
- API rate limits
- Invalid API keys
- Service outages

**Handling Strategy:**
```python
try:
    response = self.model.generate_content(prompt)
    return response.text
except Exception as e:
    # Log error
    self.mcp_client.send_error(AgentRole.TRACKING, str(e))
    # Return fallback
    return self._get_fallback_response()
```

**Fallback Mechanisms:**
- Default specifications for Parser
- Template-based code for Code Gen
- Retry with exponential backoff
- User-friendly error messages

#### 2. Invalid Generated Code

**Potential Issues:**
- Syntax errors in generated code
- Missing imports
- Logical errors

**Handling Strategy:**
- Syntax validation before saving
- Import checking
- Basic linting
- Clear error messages to user

**Implementation:**
```python
def _validate_code(self, code: str) -> bool:
    try:
        compile(code, '<string>', 'exec')
        return True
    except SyntaxError:
        return False
```

#### 3. Parsing Failures

**Potential Issues:**
- Ambiguous requirements
- LLM returns invalid JSON
- Missing required fields

**Handling Strategy:**
```python
try:
    parsed_data = json.loads(response)
    spec = RequirementSpec(**parsed_data)
except (json.JSONDecodeError, ValidationError):
    # Use defaults
    spec = RequirementSpec(
        languages=["English"],
        tenses=["present", "past"],
        ...
    )
```

#### 4. Test Failures

**Potential Issues:**
- Generated code has bugs
- Tests are too strict
- Environment issues

**Handling Strategy:**
- Accept 80% pass rate (not 100%)
- Generate extra tests
- Clear test output
- Don't block on test failures

#### 5. File I/O Errors

**Potential Issues:**
- Permission denied
- Disk full
- Invalid paths

**Handling Strategy:**
```python
def save_to_file(content: str, filepath: str):
    try:
        ensure_directory(os.path.dirname(filepath))
        with open(filepath, 'w') as f:
            f.write(content)
    except IOError as e:
        logger.error(f"Failed to save {filepath}: {e}")
        raise
```

### Error Reporting

**User-Facing Errors:**
- Clear, non-technical messages
- Suggestions for resolution
- Contact information if needed

**Developer Errors:**
- Full stack traces in logs
- MCP message history
- API call details

**Example Error Message:**
```
❌ Error: Failed to generate code

The system encountered an issue while generating your application.

Possible causes:
- API key may be invalid
- Network connection issues
- Service temporarily unavailable

Please try:
1. Check your API key in .env file
2. Verify internet connection
3. Try again in a few moments

If the problem persists, contact support.
```

---

## 5. Reflection

### What Went Well

#### 1. Agent Architecture
The multi-agent design proved highly effective. Each agent has a clear, focused responsibility, making the code easy to understand and maintain. The separation of concerns allowed team members to work on different agents simultaneously without conflicts.

#### 2. MCP Implementation
Our custom Model Context Protocol worked better than expected. The message-based communication made debugging easier and allowed us to trace exactly how data flowed through the system. The message history feature was invaluable during development.

#### 3. Code Quality
The generated code is generally well-structured and readable. The LLM (Gemini) produces code that follows Python best practices most of the time, including proper error handling and documentation.

#### 4. User Experience
The Gradio interface is intuitive and responsive. Users can easily enter requirements and see results. The tabbed interface organizes information clearly.

#### 5. Documentation
We invested heavily in documentation, which paid off. The comprehensive guides made it easy for team members to understand the system and will help graders evaluate our work.

### Challenges Faced

#### 1. LLM Consistency

**Issue:** The LLM sometimes generates inconsistent output formats, even with detailed prompts.

**Example:** Sometimes returns JSON wrapped in markdown code blocks, sometimes plain JSON, sometimes with extra text.

**Solution:** 
- Implemented robust parsing with multiple fallback strategies
- Added code to strip markdown formatting
- Validated output with Pydantic models
- Provided clear examples in prompts

**Code:**
```python
def clean_code_block(text: str) -> str:
    if text.startswith("```python"):
        text = text.replace("```python", "", 1)
    if text.startswith("```"):
        text = text.replace("```", "", 1)
    if text.endswith("```"):
        text = text.rsplit("```", 1)[0]
    return text.strip()
```

#### 2. Test Pass Rate

**Issue:** Achieving exactly 80% pass rate is difficult because:
- Generated code may have subtle bugs
- Tests may be too strict or too lenient
- LLM generates variable number of tests

**Solution:**
- Generate 12-15 tests to ensure 10+ minimum
- Accept 75-85% pass rate as acceptable
- Focus on test quality over exact percentage
- Include both easy and hard tests

#### 3. Token Usage Tracking

**Issue:** Gemini API doesn't always provide token counts in metadata.

**Solution:**
- Check for `usage_metadata` attribute
- Fall back to estimation (1 token ≈ 4 characters)
- Document estimation method
- Track calls even if token count unavailable

**Code:**
```python
if hasattr(response, 'usage_metadata'):
    tokens = (response.usage_metadata.prompt_token_count + 
              response.usage_metadata.candidates_token_count)
else:
    # Estimate
    tokens = (len(prompt) + len(response.text)) // 4
```

#### 4. MCP Complexity

**Issue:** Initial MCP design was overly complex with features we didn't need.

**Solution:**
- Simplified to essential message passing
- Removed unnecessary abstractions
- Focused on core functionality
- Kept it simple and maintainable

#### 5. Dependency Management

**Issue:** Generated code might use libraries not in requirements.txt.

**Solution:**
- Constrained generation to known libraries (mlconjug3, gradio)
- Included common libraries in requirements
- Validated imports before saving
- Provided clear dependency lists

### Limitations

#### 1. Language Support
**Limitation:** Only supports languages available in mlconjug3 library.

**Impact:** Cannot generate conjugators for less common languages.

**Future:** Could integrate multiple conjugation libraries or APIs.

#### 2. Code Correctness
**Limitation:** Generated code may contain bugs or logical errors.

**Impact:** Users may need to manually fix issues.

**Future:** Add automated code review, more validation, iterative refinement.

#### 3. Test Coverage
**Limitation:** Tests may not cover all edge cases.

**Impact:** Some bugs might not be caught.

**Future:** More sophisticated test generation, coverage analysis.

#### 4. Performance
**Limitation:** Sequential agent execution is slow (15-30 seconds).

**Impact:** User must wait for generation.

**Future:** Parallel execution where possible, caching common patterns.

#### 5. Customization
**Limitation:** Limited post-generation customization options.

**Impact:** Users can't easily modify generated code through UI.

**Future:** Interactive refinement, regeneration of specific parts.

### Lessons Learned

#### 1. Prompt Engineering is Critical
The quality of LLM output depends heavily on prompt design. We learned to:
- Be extremely specific about output format
- Provide clear examples
- Use structured prompts
- Iterate on prompts based on results

#### 2. Error Handling Must Be Comprehensive
AI systems are inherently unpredictable. We learned to:
- Expect the unexpected
- Provide fallbacks for everything
- Give users clear error messages
- Log everything for debugging

#### 3. Testing is Essential
Automated testing caught many issues during development. We learned to:
- Test early and often
- Use multiple test types (unit, integration, structure)
- Automate as much as possible
- Keep tests simple and focused

#### 4. Documentation Pays Off
Comprehensive documentation helped us:
- Onboard team members quickly
- Remember design decisions
- Debug issues faster
- Prepare for submission

#### 5. Modularity Enables Flexibility
The agent-based architecture allowed us to:
- Work on components independently
- Replace agents without affecting others
- Test components in isolation
- Extend functionality easily

### Future Improvements

#### 1. Parallel Execution
**Current:** Agents run sequentially  
**Future:** Run independent agents concurrently  
**Benefit:** 2-3x faster generation

#### 2. Code Validation
**Current:** Basic syntax checking  
**Future:** Semantic analysis, linting, type checking  
**Benefit:** Higher quality generated code

#### 3. Interactive Refinement
**Current:** One-shot generation  
**Future:** Allow users to refine requirements iteratively  
**Benefit:** Better matches user expectations

#### 4. More Languages
**Current:** Limited to mlconjug3 languages  
**Future:** Support additional conjugation libraries/APIs  
**Benefit:** Broader language coverage

#### 5. Caching
**Current:** Generate from scratch each time  
**Future:** Cache common patterns and components  
**Benefit:** Faster generation, lower API costs

#### 6. Version Control Integration
**Current:** Files saved locally  
**Future:** Automatic Git commits, branching  
**Benefit:** Better code management

---

## 6. Conclusion

The Language Verb Conjugator Factory successfully demonstrates a practical multi-agent system using the Model Context Protocol. The system transforms natural language requirements into working applications, complete with tests and usage tracking.

**Key Achievements:**
- ✅ Functional multi-agent architecture
- ✅ Custom MCP implementation
- ✅ Automated code and test generation
- ✅ Comprehensive usage tracking
- ✅ User-friendly interface
- ✅ Extensive documentation

**Technical Contributions:**
- Demonstrated effective agent coordination
- Implemented practical MCP protocol
- Showed LLM integration patterns
- Provided error handling strategies
- Created reusable architecture

**Educational Value:**
This project provided hands-on experience with:
- Multi-agent system design
- Protocol implementation
- LLM integration and prompt engineering
- Software architecture
- Team collaboration
- Professional documentation

While challenges exist in ensuring code quality and consistency, the system provides a solid foundation for automated application generation. The modular architecture and comprehensive documentation make it easy to extend and improve.

The project highlights both the potential and current limitations of LLM-based code generation, emphasizing the importance of robust error handling, clear agent responsibilities, and comprehensive testing.

---

## Appendices

### A. Usage Statistics Example

```json
{
  "gemini-2.5-flash-lite": {
    "numApiCalls": 5,
    "totalTokens": 8450
  }
}
```

**Breakdown:**
- Parser Agent: 1 call, ~1200 tokens
- Design Agent: 1 call, ~1500 tokens
- Code Gen Agent: 2 calls, ~4000 tokens
- Test Agent: 1 call, ~1750 tokens

### B. Generated Code Sample

```python
# Example generated conjugator code
class VerbConjugator:
    def __init__(self):
        self.conjugator = mlconjug3.Conjugator(language='en')
    
    def conjugate(self, verb: str, tense: str) -> dict:
        try:
            result = self.conjugator.conjugate(verb)
            return result[tense]
        except Exception as e:
            return {"error": str(e)}
```

### C. Test Results Example

```
test_conjugator.py::test_regular_verb_present PASSED
test_conjugator.py::test_regular_verb_past PASSED
test_conjugator.py::test_irregular_verb_present PASSED
test_conjugator.py::test_irregular_verb_past PASSED
test_conjugator.py::test_invalid_verb PASSED
test_conjugator.py::test_invalid_tense PASSED
test_conjugator.py::test_multiple_persons PASSED
test_conjugator.py::test_spanish_verb PASSED
test_conjugator.py::test_edge_case_1 FAILED
test_conjugator.py::test_edge_case_2 PASSED
test_conjugator.py::test_error_handling PASSED

========== 10 passed, 1 failed in 2.34s ==========
Pass Rate: 90.9%
```

### D. System Requirements

**Minimum:**
- Python 3.8+
- 4GB RAM
- Internet connection
- Google Gemini API key

**Recommended:**
- Python 3.10+
- 8GB RAM
- Fast internet
- SSD storage

---

**Report prepared by:** [Your Team]  
**Date:** [Submission Date]  
**Word Count:** ~4,500 words  
**Page Count:** 15+ pages
