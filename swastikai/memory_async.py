import requests
from typing import Any, Dict, Optional
from pydantic import ValidationError, BaseModel
from .utils import retry
from .memory_models import createPersonalMemory
from .memory_models import retrievePersonalMemory

class personal_memory:
    def __init__(self, api_key: str):
        self.base_url = "https://api.swastikai.com/api/memory/v1/"
        self.api_key = api_key

    async def _build_headers(self) -> Dict[str, str]:
        """Builds headers for each request to include the API key."""
        return {"SWK_API_KEY": f"{self.api_key}", "Content-Type": "application/json"}

    @retry()
    async def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        url = f"{self.base_url}{endpoint}"
        headers = kwargs.pop("headers", {})
        headers.update(await self._build_headers())
        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()  # Raise for 4xx/5xx HTTP codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            raise
    
    async def create_memory(self, payload:createPersonalMemory):
        await self.validate_payload(payload, createPersonalMemory)
        return await self.post(endpoint="create-memory",json_payload=payload)

    async def retrieve_memory(self, payload:retrievePersonalMemory):
        await self.validate_payload(payload, retrievePersonalMemory)
        return await self.post(endpoint="retrieve-memory",json_payload=payload)

    async def get(self, endpoint: str, params: Optional[Dict] = None) -> Any:
        """GET request that supports query parameters."""
        return await self._request("GET", endpoint, params=params)

    async def post(self, endpoint: str, json_payload: Optional[Dict] = None) -> Any:
        """POST request that sends JSON payload."""
        return await self._request("POST", endpoint, json=json_payload)
    
    async def validate_payload(self, payload: Dict, model: BaseModel) -> Any:
        """Validates and sends a JSON payload using the ExampleRequestModel."""
        try:
            # Validate payload against ExampleRequestModel
            valid_payload = model(**payload).dict()
        except ValidationError as e:
            print("Validation error:", e)
            raise

