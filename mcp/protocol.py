# Model Context Protocol definitions
# Author: [Your Name] - [Student ID]

from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from enum import Enum

class MessageType(str, Enum):
    """Types of messages in MCP"""
    REQUEST = "request"
    RESPONSE = "response"
    ERROR = "error"
    NOTIFICATION = "notification"

class AgentRole(str, Enum):
    """Agent roles in the system"""
    PARSER = "parser"
    DESIGN = "design"
    CODE_GEN = "code_gen"
    TEST_GEN = "test_gen"
    UI_GEN = "ui_gen"
    TRACKING = "tracking"

class MCPMessage(BaseModel):
    """Base message structure for MCP"""
    message_type: MessageType
    sender: AgentRole
    receiver: Optional[AgentRole] = None
    content: Dict[str, Any]
    metadata: Dict[str, Any] = {}

class RequirementSpec(BaseModel):
    """Structured requirement specification"""
    languages: List[str]
    tenses: List[str]
    persons: List[str]
    moods: List[str] = ["indicative"]
    handle_irregular: bool = True
    dataset_sources: List[str] = []
    additional_requirements: str = ""

class DesignSpec(BaseModel):
    """Design specification for the application"""
    architecture: str
    modules: List[str]
    data_schema: Dict[str, Any]
    dependencies: List[str]
    implementation_notes: str

class GeneratedCode(BaseModel):
    """Generated code structure"""
    filename: str
    code: str
    description: str
    dependencies: List[str] = []

class TestCase(BaseModel):
    """Test case structure"""
    test_name: str
    test_code: str
    description: str
    expected_pass: bool = True

class UsageStats(BaseModel):
    """Model usage statistics"""
    model_name: str
    num_api_calls: int = 0
    total_tokens: int = 0
    
    def add_call(self, tokens: int):
        """Add an API call to statistics"""
        self.num_api_calls += 1
        self.total_tokens += tokens
