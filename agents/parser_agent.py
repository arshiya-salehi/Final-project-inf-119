# Parser Agent - Parses requirements into structured specifications
# Author: [Your Name] - [Student ID]

import json
from typing import Optional
from mcp import MCPClient, AgentRole, RequirementSpec
from agents.tracking_agent import TrackingAgent

class ParserAgent:
    """
    Agent responsible for parsing natural language requirements
    into structured specifications
    """
    
    def __init__(self, tracking_agent: TrackingAgent, mcp_client: Optional[MCPClient] = None):
        """
        Initialize parser agent
        
        Args:
            tracking_agent: Tracking agent for LLM calls
            mcp_client: MCP client for communication
        """
        self.tracking_agent = tracking_agent
        self.mcp_client = mcp_client
    
    def parse_requirements(self, user_input: str) -> RequirementSpec:
        """
        Parse user requirements into structured specification
        
        Args:
            user_input: Natural language requirements
            
        Returns:
            RequirementSpec object
        """
        # Notify start of parsing
        if self.mcp_client:
            self.mcp_client.notify({
                "event": "parsing_started",
                "input_length": len(user_input)
            })
        
        # Create prompt for LLM
        prompt = f"""
You are a requirements parser for a Language Verb Conjugator application.

Parse the following requirements and extract:
1. Languages to support (e.g., English, Spanish, French)
2. Tenses to support (e.g., present, past, future, imperfect)
3. Persons to support (e.g., first person singular, second person plural)
4. Moods to support (e.g., indicative, subjunctive, imperative)
5. Whether to handle irregular verbs
6. Any dataset sources mentioned
7. Additional requirements

User Requirements:
{user_input}

Return ONLY a JSON object with this exact structure:
{{
    "languages": ["list", "of", "languages"],
    "tenses": ["list", "of", "tenses"],
    "persons": ["list", "of", "persons"],
    "moods": ["list", "of", "moods"],
    "handle_irregular": true/false,
    "dataset_sources": ["list", "of", "sources"],
    "additional_requirements": "any other requirements as text"
}}

If something is not specified, make reasonable defaults for a verb conjugator.
"""
        
        try:
            # Get response from LLM via tracking agent
            response = self.tracking_agent.generate_content(prompt)
            
            # Clean and parse JSON
            response = response.strip()
            if response.startswith("```json"):
                response = response.replace("```json", "").replace("```", "").strip()
            elif response.startswith("```"):
                response = response.replace("```", "").strip()
            
            # Parse JSON
            parsed_data = json.loads(response)
            
            # Create RequirementSpec
            spec = RequirementSpec(**parsed_data)
            
            # Notify success
            if self.mcp_client:
                self.mcp_client.notify({
                    "event": "parsing_completed",
                    "spec": spec.model_dump()
                })
            
            return spec
            
        except Exception as e:
            error_msg = f"Failed to parse requirements: {str(e)}"
            
            if self.mcp_client:
                self.mcp_client.send_error(AgentRole.PARSER, error_msg)
            
            # Return default spec on error
            return RequirementSpec(
                languages=["English"],
                tenses=["present", "past", "future"],
                persons=["first person singular", "second person singular", "third person singular"],
                moods=["indicative"],
                handle_irregular=True,
                dataset_sources=[],
                additional_requirements=user_input
            )
