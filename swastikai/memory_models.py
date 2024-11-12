from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any

class AgentDetails_PersonalMemory(BaseModel):
    company_id: Optional[str] = Field(default=None, description="The company ID/Name. This can be used to differentiate how a memory is stored and this field (if provided) sits on the top most hierarchy." + """\n
    'CogencyAI'""")
    department_id: Optional[str] = Field(default=None, description="The Department ID/Name. This can be used to differentiate how a memory is stored and this field (if provided) sits just below Company ID in hierarchy." + """\n
    'Reasearch and Development'""")
    team_id: Optional[str] = Field(default=None, description="The Team ID/Name. This can be used to differentiate how a memory is stored and this field (if provided) sits just below Department ID in hierarchy." + """\n
    'Development'""")
    agent_id: str = Field(..., description="The Agent ID/Name. This is a mandatory field. This is used to differentiate how a memory is stored and this field sits just below Team ID in hierarchy." + """\n
    'Conversation Personal Agent'""")
    user_id: str = Field(..., description="The User ID/Name. This is a mandatory field. This is used to differentiate how a memory is stored and this field sits just below Agent ID in hierarchy." + """\n
    'John Smith'""")
    agent_type: str = Field(default="iA", description="The type of the agent. This is an OPTIONAL field. The only value allowed is 'iA'" + """\n
    'iA' is the only allowed value""")
    agent_description: str = Field(..., description="This is the description of your AI agent. Be concise but properly describe what it is and what it does. This information is very crucial for the memory system as it deduces memory based upon what the agent does and thereby what it needs to remember." + """\n
    This is a Personal Assistant agent. The main role of the agent is to assist the user with writing and editing e-mails and messages.""")

class createPersonalMemory(BaseModel):
    agent_details: AgentDetails_PersonalMemory
    memories: Optional[str] = Field(default=None, description="A string of memories as received in earlier retrieve memory api calls. These are the existing memories that the system already has. This really helps in cutting down the cost and increases efficiency in case available and when the available memories are relevant to the context.Example memories to send:" + """\n
    'User loves apples',
    'User loves to dance',
    'User always prefers a polite conversation'
    """)
    last_user_prompt: str = Field(..., description="The latest prompt that the end user used. In a chat scenario this basically represents the user message that the system will provide to the LLM for a reply. Example:" + """\n
    'What should I wear today?'
    """)
    memory_category: str = Field(default="personal_memory", description="The type of memory category that needs to be used. Currently only Personal memories are supported." + """\n
    'personal_memory' is the only allowed value""")

class retrievePersonalMemory(BaseModel):
    agent_details: AgentDetails_PersonalMemory
    chat_history: Optional[List[Dict[str,Any]]] = Field(default=None,
    description="""A list of dictionaries containg the chat history. This is the format in which the chat history should be provided:
    \n```[
        {"sender": "User", "message": "Hello!"},
        {"sender": "AI Agent", "message": "Hi, how can I help you?"},
        {"sender": "User", "message": "I have a question about my order."},
        {"sender": "AI Agent", "message": "Sure, can you provide the order ID?"}
    ]```
    \n**Note**
    \n1. The chat history should be in ascending order i.e. latest conversation at the last in the list.
    \n2. The only valid value for sender is ***'User'*** and ***'AI Agent'*** only and case sensitive."""
    )
    last_user_prompt: str = Field(..., description="The latest prompt that the end user used. In a chat scenario this basically represents the user message that the system will provide to the LLM for a reply. Example:" + """\n
    'What should I wear today?'
    """)
    memory_category: str = Field(default="personal_memory", description="The type of memory category that needs to be used. Currently only Personal memories are supported." + """\n
    'personal_memory' is the only allowed value""")