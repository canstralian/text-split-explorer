# Frequently Asked Questions (FAQs)

## How do I install the required dependencies?

To install the required dependencies, run the following command:

```shell
pip install -r requirements.txt
```

## How do I run the Streamlit app locally?

To run the Streamlit app locally, use the following command:

```shell
streamlit run splitter.py
```

## How do I contribute to the project?

Please refer to the [Contribution Guide](contributing.md) for detailed instructions on how to contribute to the project.

## What is the purpose of the Text Split Explorer?

The Text Split Explorer is designed to help explore different types of text splitting. It allows you to adjust different parameters and choose different types of splitters. By pasting a text file, you can apply the splitter to that text and see the resulting splits. You are also shown a code snippet that you can copy and use in your application.

## What are the different types of text splitters available?

The Text Split Explorer provides the following types of text splitters:

- `CharacterTextSplitter`: Splits text into chunks based on a specified separator, chunk size, and chunk overlap.
- `RecursiveCharacterTextSplitter`: Tries to split text on a list of separators in order until the chunks are small enough. This helps keep paragraphs, sentences, and words together as long as possible.
- `Language-based Text Splitter`: Splits text based on language-specific rules.

## How do I use a custom length function?

You can define a custom length function to measure the length of chunks. For example, to use token length instead of character length:

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

## Where can I find more examples and use cases?

For more examples and use cases, refer to the [README](../README.md) and the [Usage Guide](usage.md).

## What should I do if I encounter issues while using the Text Split Explorer?

If you encounter any issues while using the Text Split Explorer, please refer to this FAQ or open an issue on the GitHub repository.
