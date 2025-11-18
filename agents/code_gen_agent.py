# Code Generation Agent - Generates the conjugator application code
# Author: [Your Name] - [Student ID]

from typing import Optional, List
from mcp import MCPClient, AgentRole, RequirementSpec, DesignSpec, GeneratedCode
from agents.tracking_agent import TrackingAgent
from utils.helpers import clean_code_block, save_to_file
from config.api_config import CONJUGATOR_DIR

class CodeGenAgent:
    """
    Agent responsible for generating the verb conjugator application code
    """
    
    def __init__(self, tracking_agent: TrackingAgent, mcp_client: Optional[MCPClient] = None):
        """Initialize code generation agent"""
        self.tracking_agent = tracking_agent
        self.mcp_client = mcp_client
    
    def generate_code(self, spec: RequirementSpec, design: DesignSpec) -> List[GeneratedCode]:
        """
        Generate application code based on requirements and design
        
        Args:
            spec: Requirement specification
            design: Design specification
            
        Returns:
            List of GeneratedCode objects
        """
        if self.mcp_client:
            self.mcp_client.notify({"event": "code_generation_started"})
        
        generated_files = []
        
        # Generate main conjugator module
        conjugator_code = self._generate_conjugator(spec, design)
        generated_files.append(conjugator_code)
        
        # Generate Gradio UI
        ui_code = self._generate_ui(spec)
        generated_files.append(ui_code)
        
        # Save generated files
        for gen_code in generated_files:
            filepath = f"{CONJUGATOR_DIR}/{gen_code.filename}"
            save_to_file(gen_code.code, filepath)
        
        if self.mcp_client:
            self.mcp_client.notify({
                "event": "code_generation_completed",
                "files": [gc.filename for gc in generated_files]
            })
        
        return generated_files
    
    def _generate_conjugator(self, spec: RequirementSpec, design: DesignSpec) -> GeneratedCode:
        """Generate the main conjugator module"""
        
        prompt = f"""
Generate a complete Python module for a verb conjugator with these requirements:

Languages: {', '.join(spec.languages)}
Tenses: {', '.join(spec.tenses)}
Persons: {', '.join(spec.persons)}
Handle Irregular: {spec.handle_irregular}

The code should:
1. Use mlconjug3 library for conjugations
2. Have a VerbConjugator class with a conjugate() method
3. Handle multiple languages and tenses
4. Return conjugations in a clear format
5. Include error handling
6. Be well-commented

Return ONLY the Python code, no explanations.
"""
        
        code = self.tracking_agent.generate_content(prompt)
        code = clean_code_block(code)
        
        return GeneratedCode(
            filename="verb_conjugator.py",
            code=code,
            description="Main verb conjugator module",
            dependencies=["mlconjug3"]
        )
    
    def _generate_ui(self, spec: RequirementSpec) -> GeneratedCode:
        """Generate Gradio UI code"""
        
        prompt = f"""
Generate a Gradio UI for a verb conjugator that:
1. Imports from verb_conjugator module
2. Has input fields for: verb, language, tense
3. Displays conjugation results in a clear format
4. Handles errors gracefully
5. Is user-friendly

Languages to support: {', '.join(spec.languages)}
Tenses to support: {', '.join(spec.tenses)}

Return ONLY the Python code for the Gradio interface.
"""
        
        code = self.tracking_agent.generate_content(prompt)
        code = clean_code_block(code)
        
        return GeneratedCode(
            filename="gradio_ui.py",
            code=code,
            description="Gradio user interface",
            dependencies=["gradio", "verb_conjugator"]
        )
