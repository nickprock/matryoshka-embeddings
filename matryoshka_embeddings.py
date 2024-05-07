from cat.mad_hatter.decorators import tool, hook, plugin
from cat.factory.embedder import EmbedderSettings

from pydantic import BaseModel, ConfigDict, Field
from typing import Type, Optional, List

from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings

class MatryoshkaOpenAIConfig(EmbedderSettings):
    openai_api_key: str
    model: str = 'text-embedding-3-small'
    dimensions: Optional[int] = 1536
    _pyclass: Type = OpenAIEmbeddings

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Matryoshka OpenAI Embedder",
            "description": "Configuration for OpenAI matryoshka embeddings",
            "link": "https://platform.openai.com/docs/models/overview",
        }
    )


# https://python.langchain.com/en/latest/_modules/langchain/embeddings/openai.html#OpenAIEmbeddings
class MatryoshkaAzureOpenAIConfig(EmbedderSettings):
    openai_api_key: str
    model: str
    azure_endpoint: str
    openai_api_type: str = "azure"
    openai_api_version: str
    deployment: str
    dimensions: Optional[int]

    _pyclass: Type = AzureOpenAIEmbeddings

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Matryoshka Azure OpenAI Embedder",
            "description": "Configuration for Azure OpenAI matryoshka embeddings",
            "link": "https://azure.microsoft.com/en-us/products/ai-services/openai-service",
        }
    )

@hook
def factory_allowed_embedders(allowed, cat) -> List:
    allowed.append(MatryoshkaOpenAIConfig)
    allowed.append(MatryoshkaAzureOpenAIConfig)
    return allowed