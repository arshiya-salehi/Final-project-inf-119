# MCP Client implementation
# Author: [Your Name] - [Student ID]

from typing import Optional, Dict, Any
from .protocol import MCPMessage, AgentRole, MessageType
from .server import MCPServer

class MCPClient:
    """
    MCP Client for agents to communicate with the server
    """
    
    def __init__(self, server: MCPServer, role: AgentRole):
        """
        Initialize MCP client
        
        Args:
            server: MCP server instance
            role: This agent's role
        """
        self.server = server
        self.role = role
    
    def send_request(self, receiver: AgentRole, content: Dict[str, Any]) -> None:
        """
        Send a request to another agent
        
        Args:
            receiver: Target agent role
            content: Request content
        """
        message = MCPMessage(
            message_type=MessageType.REQUEST,
            sender=self.role,
            receiver=receiver,
            content=content
        )
        self.server.send_message(message)
    
    def send_response(self, receiver: AgentRole, content: Dict[str, Any]) -> None:
        """
        Send a response to another agent
        
        Args:
            receiver: Target agent role
            content: Response content
        """
        message = MCPMessage(
            message_type=MessageType.RESPONSE,
            sender=self.role,
            receiver=receiver,
            content=content
        )
        self.server.send_message(message)
    
    def send_error(self, receiver: AgentRole, error: str) -> None:
        """
        Send an error message
        
        Args:
            receiver: Target agent role
            error: Error description
        """
        message = MCPMessage(
            message_type=MessageType.ERROR,
            sender=self.role,
            receiver=receiver,
            content={"error": error}
        )
        self.server.send_message(message)
    
    def notify(self, content: Dict[str, Any], receiver: Optional[AgentRole] = None) -> None:
        """
        Send a notification
        
        Args:
            content: Notification content
            receiver: Optional specific receiver, None for broadcast
        """
        message = MCPMessage(
            message_type=MessageType.NOTIFICATION,
            sender=self.role,
            receiver=receiver,
            content=content
        )
        self.server.send_message(message)
    
    def receive_message(self, timeout: Optional[float] = None) -> Optional[MCPMessage]:
        """
        Receive a message for this agent
        
        Args:
            timeout: Timeout in seconds
            
        Returns:
            MCPMessage or None
        """
        return self.server.get_message(self.role, timeout)
