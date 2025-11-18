# Design Agent - Creates architecture and design specifications
# Author: [Your Name] - [Student ID]

import json
from typing import Optional
from mcp import MCPClient, AgentRole, RequirementSpec, DesignSpec
from agents.tracking_agent import TrackingAgent

class DesignAgent:
    """
    Agent responsible for creating system architecture and design
    based on parsed requirements
    """
    
    def __init__(self, tracking_agent: TrackingAgent, mcp_client: Optional[MCPClient] = None):
        """Initialize design agent"""
        self.tracking_agent = tracking_agent
        self.mcp_client = mcp_client
    
    def create_design(self, spec: RequirementSpec) -> DesignSpec:
        """
        Create design specification from requirements
        
        Args:
            spec: Requirement specification
            
        Returns:
            DesignSpec object
        """
        if self.mcp_client:
            self.mcp_client.notify({"event": "design_started"})
        
        prompt = f"""
You are a software architect designing a Language Verb Conjugator application.

Requirements:
- Languages: {', '.join(spec.languages)}
- Tenses: {', '.join(spec.tenses)}
- Persons: {', '.join(spec.persons)}
- Moods: {', '.join(spec.moods)}
- Handle Irregular Verbs: {spec.handle_irregular}
- Additional: {spec.additional_requirements}

Design a Python application with:
1. Clear module structure
2. Data schema for storing conjugations
3. Required dependencies
4. Implementation approach

Return ONLY a JSON object:
{{
    "architecture": "description of overall architecture",
    "modules": ["list", "of", "module", "names"],
    "data_schema": {{"description": "of data structure"}},
    "dependencies": ["list", "of", "python", "packages"],
    "implementation_notes": "key implementation details"
}}
"""
        
        try:
            response = self.tracking_agent.generate_content(prompt)
            response = response.strip()
            if response.startswith("```json"):
                response = response.replace("```json", "").replace("```", "").strip()
            elif response.startswith("```"):
                response = response.replace("```", "").strip()
            
            parsed_data = json.loads(response)
            design = DesignSpec(**parsed_data)
            
            if self.mcp_client:
                self.mcp_client.notify({"event": "design_completed", "design": design.model_dump()})
            
            return design
            
        except Exception as e:
            if self.mcp_client:
                self.mcp_client.send_error(AgentRole.DESIGN, f"Design failed: {str(e)}")
            
            # Return default design
            return DesignSpec(
                architecture="Simple verb conjugator with dictionary-based lookups",
                modules=["verb_conjugator", "data_loader", "ui"],
                data_schema={"verbs": "dict", "conjugations": "dict"},
                dependencies=["mlconjug3", "gradio"],
                implementation_notes="Use mlconjug3 library for conjugations"
            )
