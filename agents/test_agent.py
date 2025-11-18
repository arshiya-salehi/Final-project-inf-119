# Test Generation Agent - Generates test cases for the application
# Author: [Your Name] - [Student ID]

from typing import Optional, List
from mcp import MCPClient, AgentRole, RequirementSpec, GeneratedCode, TestCase
from agents.tracking_agent import TrackingAgent
from utils.helpers import clean_code_block, save_to_file
from config.api_config import TESTS_DIR

class TestAgent:
    """
    Agent responsible for generating comprehensive test cases
    """
    
    def __init__(self, tracking_agent: TrackingAgent, mcp_client: Optional[MCPClient] = None):
        """Initialize test generation agent"""
        self.tracking_agent = tracking_agent
        self.mcp_client = mcp_client
    
    def generate_tests(self, spec: RequirementSpec, generated_code: List[GeneratedCode]) -> str:
        """
        Generate test cases for the application
        
        Args:
            spec: Requirement specification
            generated_code: List of generated code files
            
        Returns:
            Test file content as string
        """
        if self.mcp_client:
            self.mcp_client.notify({"event": "test_generation_started"})
        
        # Get the main conjugator code
        conjugator_code = next((gc for gc in generated_code if "conjugator" in gc.filename), None)
        
        prompt = f"""
Generate comprehensive pytest test cases for a verb conjugator application.

Requirements:
- Languages: {', '.join(spec.languages)}
- Tenses: {', '.join(spec.tenses)}
- Test irregular verbs: {spec.handle_irregular}

Generate at least 12 test cases that:
1. Test regular verb conjugations
2. Test irregular verb conjugations (if applicable)
3. Test multiple languages
4. Test multiple tenses
5. Test error handling (invalid inputs)
6. Test edge cases

The tests should:
- Use pytest framework
- Import from verb_conjugator module
- Be well-documented
- Have clear assertions
- At least 80% should pass

Return ONLY the Python test code.
"""
        
        test_code = self.tracking_agent.generate_content(prompt)
        test_code = clean_code_block(test_code)
        
        # Ensure proper imports
        if "import pytest" not in test_code:
            test_code = "import pytest\n" + test_code
        
        # Save test file
        test_filepath = f"{TESTS_DIR}/test_conjugator.py"
        save_to_file(test_code, test_filepath)
        
        if self.mcp_client:
            self.mcp_client.notify({
                "event": "test_generation_completed",
                "test_file": test_filepath
            })
        
        return test_code
