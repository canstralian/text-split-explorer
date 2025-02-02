# Usage Guide

This document provides step-by-step instructions on how to use the different text splitters and their parameters in the Text Split Explorer project.

## Table of Contents

- [CharacterTextSplitter](#charactertextsplitter)
- [RecursiveCharacterTextSplitter](#recursivecharactertextsplitter)
- [Language-based Text Splitter](#language-based-text-splitter)

## CharacterTextSplitter

The `CharacterTextSplitter` splits text into chunks based on a specified separator, chunk size, and chunk overlap. Here's an example of how to use it:

```python
from langchain.text_splitter import CharacterTextSplitter

length_function = len

splitter = CharacterTextSplitter(
    separator = "\n\n",  # Split character (default \n\n)
    chunk_size=1000,
    chunk_overlap=200,
    length_function=length_function,
)
text = "foo bar"
splits = splitter.split_text(text)
```

## RecursiveCharacterTextSplitter

The `RecursiveCharacterTextSplitter` tries to split text on a list of separators in order until the chunks are small enough. This helps keep paragraphs, sentences, and words together as long as possible. Here's an example:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

length_function = len

# The default list of split characters is [\n\n, \n, " ", ""]
# Tries to split on them in order until the chunks are small enough
splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=1000, 
    chunk_overlap=200,
    length_function=length_function,
)
text = "foo bar"
splits = splitter.split_text(text)
```

## Language-based Text Splitter

The `RecursiveCharacterTextSplitter` can also be used to split text based on language-specific rules. Here's an example of how to use it for English:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

length_function = len

splitter = RecursiveCharacterTextSplitter.from_language(
    Language.ENGLISH,
    chunk_size=1000, 
    chunk_overlap=200,
    length_function=length_function,
)
text = "foo bar"
splits = splitter.split_text(text)
```

## Custom Length Function

You can also define a custom length function to measure the length of chunks. For example, to use token length instead of character length:

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
    
def length_function(text: str) -> int:
    return len(enc.encode(text))

from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator = "\n\n",  # Split character (default \n\n)
    chunk_size=1000,
    chunk_overlap=200,
    length_function=length_function,
)
text = "foo bar"
splits = splitter.split_text(text)
```

For more details on how to use the Text Split Explorer, refer to the [README](../README.md).

If you encounter any issues while using the text splitters, please refer to the [FAQ](faq.md) or open an issue on the GitHub repository.
