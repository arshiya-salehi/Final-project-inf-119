# Gradio UI for the Verb Conjugator Factory
# Author: [Your Name] - [Student ID]

import gradio as gr
import os
from typing import Tuple
from mcp import MCPServer, MCPClient, AgentRole
from agents import TrackingAgent, ParserAgent, DesignAgent, CodeGenAgent, TestAgent
from config.api_config import GRADIO_SERVER_NAME, GRADIO_SERVER_PORT, USAGE_REPORT_FILE
from utils.helpers import load_from_file, ensure_directory

class VerbConjugatorFactoryUI:
    """
    Gradio UI for the multi-agent verb conjugator factory
    """
    
    def __init__(self):
        """Initialize the UI and agents"""
        # Initialize MCP server
        self.mcp_server = MCPServer()
        
        # Initialize agents
        self.tracking_agent = TrackingAgent()
        self.parser_agent = ParserAgent(self.tracking_agent)
        self.design_agent = DesignAgent(self.tracking_agent)
        self.code_gen_agent = CodeGenAgent(self.tracking_agent)
        self.test_agent = TestAgent(self.tracking_agent)
        
        # Ensure output directories exist
        ensure_directory("generated/conjugator")
        ensure_directory("generated/tests")
    
    def generate_application(self, requirements: str) -> Tuple[str, str, str, str, str]:
        """
        Main pipeline to generate the verb conjugator application
        
        Args:
            requirements: User requirements as text
            
        Returns:
            Tuple of (status, generated_code, test_code, usage_report, instructions)
        """
        try:
            # Step 1: Parse requirements
            status = "📝 Parsing requirements..."
            spec = self.parser_agent.parse_requirements(requirements)
            
            # Step 2: Create design
            status += "\n🎨 Creating design..."
            design = self.design_agent.create_design(spec)
            
            # Step 3: Generate code
            status += "\n💻 Generating code..."
            generated_code = self.code_gen_agent.generate_code(spec, design)
            
            # Step 4: Generate tests
            status += "\n🧪 Generating tests..."
            test_code = self.test_agent.generate_tests(spec, generated_code)
            
            # Step 5: Save usage report
            status += "\n📊 Saving usage report..."
            self.tracking_agent.save_usage_report()
            
            # Load generated files
            conjugator_code = load_from_file("generated/conjugator/verb_conjugator.py")
            ui_code = load_from_file("generated/conjugator/gradio_ui.py")
            
            # Combine code for display
            full_code = f"# verb_conjugator.py\n{conjugator_code}\n\n# gradio_ui.py\n{ui_code}"
            
            # Load usage report
            usage_report = load_from_file(USAGE_REPORT_FILE)
            
            # Create instructions
            instructions = self._create_instructions(spec)
            
            status += "\n\n✅ Generation complete!"
            
            return status, full_code, test_code, usage_report, instructions
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            return error_msg, "", "", "", ""
    
    def _create_instructions(self, spec) -> str:
        """Create instructions for running the generated application"""
        return f"""
# How to Run the Generated Application

## 1. Install Dependencies
```bash
pip install mlconjug3 gradio pytest
```

## 2. Run the Conjugator UI
```bash
cd generated/conjugator
python gradio_ui.py
```

## 3. Run the Tests
```bash
cd generated/tests
pytest test_conjugator.py -v
```

## Application Features
- Supported Languages: {', '.join(spec.languages)}
- Supported Tenses: {', '.join(spec.tenses)}
- Handles Irregular Verbs: {spec.handle_irregular}

## Usage
1. Open the Gradio interface in your browser
2. Enter a verb to conjugate
3. Select language and tense
4. View the conjugation results
"""
    
    def create_interface(self) -> gr.Blocks:
        """Create the Gradio interface"""
        
        with gr.Blocks(title="Verb Conjugator Factory", theme=gr.themes.Soft()) as interface:
            gr.Markdown("# 🏭 Language Verb Conjugator Factory")
            gr.Markdown("Multi-agent system that generates verb conjugator applications using MCP")
            
            with gr.Row():
                with gr.Column():
                    requirements_input = gr.Textbox(
                        label="Application Requirements",
                        placeholder="Enter requirements for the verb conjugator...\n\nExample:\nCreate a verb conjugator that supports English and Spanish.\nIt should handle present, past, and future tenses.\nInclude support for irregular verbs.",
                        lines=10
                    )
                    
                    generate_btn = gr.Button("🚀 Generate Application", variant="primary", size="lg")
                
                with gr.Column():
                    status_output = gr.Textbox(label="Generation Status", lines=10)
            
            with gr.Tabs():
                with gr.Tab("📄 Generated Code"):
                    code_output = gr.Code(label="Application Code", language="python", lines=20)
                
                with gr.Tab("🧪 Test Cases"):
                    test_output = gr.Code(label="Test Code", language="python", lines=20)
                
                with gr.Tab("📊 Usage Report"):
                    usage_output = gr.Code(label="Model Usage Report", language="json", lines=10)
                
                with gr.Tab("📖 Instructions"):
                    instructions_output = gr.Markdown()
            
            # Connect the button
            generate_btn.click(
                fn=self.generate_application,
                inputs=[requirements_input],
                outputs=[status_output, code_output, test_output, usage_output, instructions_output]
            )
            
            # Add examples
            gr.Examples(
                examples=[
                    ["Create a verb conjugator for English and Spanish that supports present, past, and future tenses. Include irregular verb handling."],
                    ["Build a French verb conjugator with present, imperfect, and future tenses. Support both regular and irregular verbs."],
                    ["Make a simple English verb conjugator for present and past tense only."]
                ],
                inputs=[requirements_input]
            )
        
        return interface
    
    def launch(self):
        """Launch the Gradio interface"""
        interface = self.create_interface()
        interface.launch(
            server_name=GRADIO_SERVER_NAME,
            server_port=GRADIO_SERVER_PORT,
            share=False
        )
