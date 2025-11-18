# Tracking Agent - Monitors and reports model usage
# Author: [Your Name] - [Student ID]

import google.generativeai as genai
from typing import Dict, Optional
from mcp import MCPClient, AgentRole, UsageStats
from config.api_config import GOOGLE_API_KEY, MODEL_NAME, USAGE_REPORT_FILE
from utils.helpers import save_json

class TrackingAgent:
    """
    Agent responsible for tracking model API usage
    Wraps LLM calls and maintains usage statistics
    """
    
    def __init__(self, mcp_client: Optional[MCPClient] = None):
        """
        Initialize tracking agent
        
        Args:
            mcp_client: MCP client for communication
        """
        self.mcp_client = mcp_client
        
        # Configure Gemini API
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(model_name=MODEL_NAME)
        
        # Usage statistics per model
        self.usage_stats: Dict[str, UsageStats] = {}
        
        # Initialize stats for the model
        if MODEL_NAME not in self.usage_stats:
            self.usage_stats[MODEL_NAME] = UsageStats(model_name=MODEL_NAME)
    
    def generate_content(self, prompt: str, **kwargs) -> str:
        """
        Generate content using the LLM and track usage
        
        Args:
            prompt: Prompt for the model
            **kwargs: Additional arguments for generation
            
        Returns:
            Generated text
        """
        try:
            # Make API call
            response = self.model.generate_content(prompt, **kwargs)
            
            # Extract token usage from response metadata
            # Note: Gemini API provides usage metadata
            tokens_used = 0
            if hasattr(response, 'usage_metadata'):
                tokens_used = (
                    response.usage_metadata.prompt_token_count + 
                    response.usage_metadata.candidates_token_count
                )
            else:
                # Estimate tokens if not available (rough estimate: 1 token ≈ 4 chars)
                tokens_used = (len(prompt) + len(response.text)) // 4
            
            # Track the API call
            self.usage_stats[MODEL_NAME].add_call(tokens_used)
            
            # Notify via MCP if available
            if self.mcp_client:
                self.mcp_client.notify({
                    "event": "api_call",
                    "model": MODEL_NAME,
                    "tokens": tokens_used
                })
            
            return response.text
            
        except Exception as e:
            # Track failed calls too
            self.usage_stats[MODEL_NAME].num_api_calls += 1
            
            if self.mcp_client:
                self.mcp_client.send_error(
                    AgentRole.TRACKING,
                    f"API call failed: {str(e)}"
                )
            
            raise e
    
    def get_usage_report(self) -> Dict[str, Dict[str, int]]:
        """
        Get usage report in the required format
        
        Returns:
            Dictionary with model usage statistics
        """
        report = {}
        for model_name, stats in self.usage_stats.items():
            report[model_name] = {
                "numApiCalls": stats.num_api_calls,
                "totalTokens": stats.total_tokens
            }
        return report
    
    def save_usage_report(self, filepath: str = USAGE_REPORT_FILE):
        """
        Save usage report to JSON file
        
        Args:
            filepath: Path to save the report
        """
        report = self.get_usage_report()
        save_json(report, filepath)
        
        if self.mcp_client:
            self.mcp_client.notify({
                "event": "report_saved",
                "filepath": filepath,
                "report": report
            })
    
    def reset_stats(self):
        """Reset all usage statistics"""
        for stats in self.usage_stats.values():
            stats.num_api_calls = 0
            stats.total_tokens = 0
