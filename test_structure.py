#!/usr/bin/env python3
# Test script to verify code structure without API calls
import sys
sys.path.insert(0, '.')

print("Testing project structure...\n")

# Test 1: Import all modules
print("1. Testing imports...")
try:
    from mcp import MCPServer, MCPClient, AgentRole, MessageType
    from agents import TrackingAgent, ParserAgent, DesignAgent, CodeGenAgent, TestAgent
    from config import api_config
    from utils import helpers
    print("   ✅ All imports successful")
except Exception as e:
    print(f"   ❌ Import error: {e}")
    sys.exit(1)

# Test 2: MCP Server initialization
print("\n2. Testing MCP Server...")
try:
    server = MCPServer()
    client = MCPClient(server, AgentRole.PARSER)
    print("   ✅ MCP Server and Client initialized")
except Exception as e:
    print(f"   ❌ MCP error: {e}")
    sys.exit(1)

# Test 3: Agent initialization (without API calls)
print("\n3. Testing Agent initialization...")
try:
    # Note: This will show API key warning, which is expected
    tracker = TrackingAgent()
    parser = ParserAgent(tracker)
    design = DesignAgent(tracker)
    codegen = CodeGenAgent(tracker)
    testgen = TestAgent(tracker)
    print("   ✅ All agents initialized")
except Exception as e:
    print(f"   ❌ Agent error: {e}")
    sys.exit(1)

# Test 4: Helper functions
print("\n4. Testing helper functions...")
try:
    from utils.helpers import ensure_directory, clean_code_block
    ensure_directory("test_output")
    cleaned = clean_code_block("```python\nprint('test')\n```")
    assert cleaned == "print('test')"
    print("   ✅ Helper functions work")
except Exception as e:
    print(f"   ❌ Helper error: {e}")
    sys.exit(1)

# Test 5: Pydantic models
print("\n5. Testing data models...")
try:
    from mcp import RequirementSpec, DesignSpec, GeneratedCode, TestCase
    
    spec = RequirementSpec(
        languages=["English"],
        tenses=["present"],
        persons=["first person"],
        moods=["indicative"],
        handle_irregular=True
    )
    print(f"   ✅ RequirementSpec created: {spec.languages}")
    
    design = DesignSpec(
        architecture="test",
        modules=["test"],
        data_schema={},
        dependencies=["test"],
        implementation_notes="test"
    )
    print(f"   ✅ DesignSpec created")
    
except Exception as e:
    print(f"   ❌ Model error: {e}")
    sys.exit(1)

# Test 6: UI initialization (without launching)
print("\n6. Testing UI initialization...")
try:
    from ui.gradio_app import VerbConjugatorFactoryUI
    app = VerbConjugatorFactoryUI()
    print("   ✅ UI initialized")
except Exception as e:
    print(f"   ❌ UI error: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("✅ ALL STRUCTURE TESTS PASSED!")
print("="*50)
print("\nTo run the full application:")
print("1. Set your GOOGLE_API_KEY in .env file")
print("2. Run: python main.py")
print("\nThe application will start on http://localhost:7860")
