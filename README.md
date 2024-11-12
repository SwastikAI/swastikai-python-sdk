# SwastikAI

This is the `official` Python SDK of SwastikAI. It allows you to easily create and/or retrieve memories for your AI agents. Whether you've one agent, a multi-agent system or an agent based on LLM or SLM - SwastikAI works seamlessly across platforms and irrespective of your choice of AI model as long as the memory requirement is in natural language. Visit https://swastikai.com. to get your API_KEY and grab some generous free usage credits.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
  - [Memory Creation](#memory-creation)
  - [Memory Retrieval](#memory-retrieval)
  - [Async Requests](#async-requests)
- [API Documentation](#api-documentation)

---

# Installation

Easily install using `pip`:

```bash
pip install swastikai
```

# Quick Start
Quick example code showing how to initialize the memory client and start using it in just few lines of code.

---

## Memory Creation

### Making a Request
```python
from swastikai.memory import personal_memory
memory_client = personal_memory(api_key="SWK_API_KEY") #Get your API KEY from www.swastikai.com
paylod = {
    "agent_details": {
    "agent_id": "Sample_Agent",
    "user_id": "John",
    "agent_description": "This is a very helpful personal assisstant.",
    },
    "memories": "",
    "last_user_prompt": "I love mangoes",
    "last_ai_response": "",
    "chat_history": [],
    "memory_category": "personal_memory"
    }

response = memory_client.create_memory(paylod)
print(response)
```

### Memory Creation Payload
```bash
agent_details = {
  "agent_details": {
    "company_id": "string",
    "department_id": "string",
    "team_id": "string",
    "agent_id": "string",
    "user_id": "string",
    "agent_type": "iA",
    "agent_description": "string"
  },
  "memories": "string",
  "last_user_prompt": "string",
  "memory_category": "personal_memory"
}
```
**Agent Details**
- *company_id* (`string`) (`Optional`): The company ID/Name. This can be used to differentiate how a memory is stored.This field sits at the top-most hierarchy.<br>
Example:
  ```bash
  SwastikAI
  ```
- *department_id* (`string`) (`Optional`): The Department ID/Name. This can be used to differentiate how a memory is stored. This field (if provided) sits just below Company ID in hierarchy.<br> Example:
  ```bash
  Reasearch and Development
  ```
- *team_id* (`string`) (`Optional`): The Team ID/Name. This can be used to differentiate how a memory is stored. This field (if provided) sits just below Department ID in hierarchy.<br>Example:
  ```bash
  Development Team
  ```
- *agent_id* (`string`): The Agent ID/Name. This is a `mandatory` field. This is used to differentiate how a memory is stored. This field sits just below Team ID in hierarchy.<br>Example:
  ```bash
  Conversation Personal Agent
  ```
- *user_id* (`string`): The User ID/Name. This is a `mandatory` field. This is used to differentiate how a memory is stored. This field sits just below Agent ID in hierarchy.<br>Example:
  ```bash
  John Smith
  ```
- *agent_type* (`string`) (`Optional`): The type of the agent. This is an `OPTIONAL` field. The `Default` value and the only value allowed is
  ```bash
  iA
  ```
- *agent_description* (`string`): This is the description of your AI agent, a `very important` and `mandatory` field. Be concise but properly describe what it is and what it does. This information is very crucial for the memory system as it deduces memory based upon what the agent does and thereby what it needs to remember.<br>Example:
  ```bash
  This is a Personal Assistant agent. The main role of the agent is to assist the user with writing and editing e-mails and messages.
  ```
**Other Parameters**
- *memories* (`string`) (`Optional`): A string of memories as received in earlier retrieve memory api calls. These are the existing memories that the system already has. This really helps in cutting down the cost and increases efficiency in case available and when the available memories are relevant to the context. This also helps in eradicating duplicate memory creation, if available with you but not provided, chances of duplicate memory creation increases multifold<br>Example memories to send:
  ```bash
  "User loves apples"
  "User loves to dance"
  "User always prefers a polite conversation"
  ```
- *last_user_prompt* (`string`): The latest prompt that the end user used. In a chat scenario this basically represents the user message that the system will provide to the LLM for a reply.<br>Example:
  ```bash
  What should I wear today?
  ```
- *memory_category* (`string`) (`Optional`): The type of memory category that needs to be used. Currently only Personal memories are supported.
  ```bash
  personal_memory
  ```

---

## Memory Retrieval
All remains same just change the calling function to `retrieve_memory`
```python
response = memory_client.retrieve_memory(paylod)
print(response)
```

### Memory Retrieval Payload
Same as memory creation payload with one addition of `chat_history` parameter.
```bash
{
  "agent_details": {
    "company_id": "string",
    "department_id": "string",
    "team_id": "string",
    "agent_id": "string",
    "user_id": "string",
    "agent_type": "iA",
    "agent_description": "string"
  },
  "chat_history": [
    {}
  ],
  "last_user_prompt": "string",
  "memory_category": "personal_memory"
}
```
- *chat_history* (`list[dict]`) (`Optional`): A list of dictionaries containg the chat history.
  1. The chat history should be in ascending order i.e. latest conversation at the last in the list.\n"
  2. The only valid value for sender is `User` and `AI Agent` only and case sensitive.
  ```json
    [
      {"sender": "User", "message": "Hello!"},
      {"sender": "AI Agent", "message": "Hi, how can I help you?"},
      {"sender": "User", "message": "I have a question about my order."},
      {"sender": "AI Agent", "message": "Sure, can you provide the order ID?"}
    ]
  ```

---

## Async Requests
```python
from swastikai.memory_async import personal_memory
```

---

# API Documentation
Please find the API documentation in at https://api.swastikai.com/.