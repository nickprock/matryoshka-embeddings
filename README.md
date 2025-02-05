# Matryoshka Embeddings

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=383938&style=for-the-badge&logo=cheshire_cat_ai)](https://)  


## Overview

The plugin enables the ability to use [matryoshka embeddings from OpenAI](https://openai.com/index/new-embedding-models-and-api-updates).

If you want to go deep in [matryoshka embeddings](https://arxiv.org/abs/2205.13147).


## Technology Stack

- **Language:** Python
- **Frameworks:** Langchain, Cheshire Cat
- **Libraries:** Pydantic
- **Tools:** OpenAI API, Azure OpenAI API

## Detailed Component Breakdown

### `MatryoshkaOpenAIConfig` Class

This class serves as a configuration container for OpenAI embeddings.  It inherits from an external `EmbedderSettings` class, likely defining common attributes for various embedding types.  Key attributes include:

*   `openai_api_key`: (str) The API key for accessing the OpenAI service.  This is a required field.
*   `model`: (str, default='text-embedding-3-small') Specifies the OpenAI embedding model to use.
*   `dimensions`: (Optional[int], default=1536)  The dimensionality of the generated embeddings.  This is optional, suggesting a default dimension is available.
*   `_pyclass`: (Type)  Specifies the Langchain class to be instantiated (`OpenAIEmbeddings`), linking the configuration to the appropriate embedding provider.


The `ConfigDict` metadata enhances user experience by providing a human-readable name, description, and a link to relevant OpenAI documentation.

### `MatryoshkaAzureOpenAIConfig` Class

This class mirrors the functionality of `MatryoshkaOpenAIConfig`, but for Azure OpenAI embeddings. It includes similar attributes (API key, model) along with additional fields specific to Azure's environment:

*   `azure_endpoint`: (str) The endpoint URL for the Azure OpenAI service.  This is required.
*   `openai_api_type`: (str, default='azure') Specifies the API type as 'azure'.
*   `openai_api_version`: (str) The API version for Azure OpenAI. This is required.
*   `deployment`: (str) The Azure OpenAI deployment name.  This is required.
*   `dimensions`: (Optional[int]) Similar to the OpenAI config, this specifies embedding dimensions and is optional.
*   `_pyclass`: (Type) Specifies `AzureOpenAIEmbeddings` for instantiation.

Like `MatryoshkaOpenAIConfig`, `ConfigDict` provides metadata for a better user experience.


### `factory_allowed_embedders` Function

This function, decorated with the `@hook` decorator (from the `cat` framework), acts as a plugin mechanism to register the OpenAI and Azure OpenAI embedding configurations.  It appends both `MatryoshkaOpenAIConfig` and `MatryoshkaAzureOpenAIConfig` to the provided `allowed` list, making them discoverable and usable within the `cat` framework.  The `cat` parameter likely represents the framework's context.

### `EmbedderSettings` Class (External)

This class (not shown in the code snippet) serves as the base class for the embedding configuration classes. It likely defines common attributes and methods shared by all embedding configurations, promoting code reusability and a consistent interface.


## Interactions and Data Flow

1.  The `factory_allowed_embedders` function registers `MatryoshkaOpenAIConfig` and `MatryoshkaAzureOpenAIConfig` within the `cat` framework.

2.  The `cat` framework (through an unknown mechanism) would then utilize these registered configurations to instantiate the appropriate Langchain embedding classes (`OpenAIEmbeddings` or `AzureOpenAIEmbeddings`).  This likely involves fetching the configuration settings (API keys, endpoints, model names, etc.) from the chosen config class.

3.  The instantiated Langchain embedding object would be used to generate embeddings based on the provided text.
