# MCP Server implementation
# Author: [Your Name] - [Student ID]

from typing import Dict, List, Optional, Callable
from queue import Queue
import threading
from .protocol import MCPMessage, AgentRole, MessageType

class MCPServer:
    """
    Model Context Protocol Server
    Manages communication between agents
    """
    
    def __init__(self):
        """Initialize the MCP server"""
        # Message queues for each agent
        self.agent_queues: Dict[AgentRole, Queue] = {
            role: Queue() for role in AgentRole
        }
        
        # Registered agents and their handlers
        self.agent_handlers: Dict[AgentRole, Callable] = {}
        
        # Message history for debugging
        self.message_history: List[MCPMessage] = []
        
        # Server state
        self.running = False
        self.lock = threading.Lock()
    
    def register_agent(self, role: AgentRole, handler: Callable):
        """
        Register an agent with its message handler
        
        Args:
            role: Agent role
            handler: Function to handle messages for this agent
        """
        with self.lock:
            self.agent_handlers[role] = handler
    
    def send_message(self, message: MCPMessage):
        """
        Send a message to an agent
        
        Args:
            message: MCPMessage to send
        """
        with self.lock:
            # Store in history
            self.message_history.append(message)
            
            # Route to appropriate queue
            if message.receiver:
                self.agent_queues[message.receiver].put(message)
            else:
                # Broadcast to all agents
                for queue in self.agent_queues.values():
                    queue.put(message)
    
    def get_message(self, role: AgentRole, timeout: Optional[float] = None) -> Optional[MCPMessage]:
        """
        Get a message for a specific agent
        
        Args:
            role: Agent role
            timeout: Timeout in seconds
            
        Returns:
            MCPMessage or None if timeout
        """
        try:
            return self.agent_queues[role].get(timeout=timeout)
        except:
            return None
    
    def broadcast(self, sender: AgentRole, content: Dict, message_type: MessageType = MessageType.NOTIFICATION):
        """
        Broadcast a message to all agents
        
        Args:
            sender: Sending agent role
            content: Message content
            message_type: Type of message
        """
        message = MCPMessage(
            message_type=message_type,
            sender=sender,
            receiver=None,
            content=content
        )
        self.send_message(message)
    
    def get_history(self) -> List[MCPMessage]:
        """
        Get message history
        
        Returns:
            List of all messages
        """
        with self.lock:
            return self.message_history.copy()
    
    def clear_history(self):
        """Clear message history"""
        with self.lock:
            self.message_history.clear()
