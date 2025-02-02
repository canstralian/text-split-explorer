import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter, Language
import code_snippets as code_snippets
import tiktoken
from typing import Callable, List
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Custom exception classes
class InvalidInputError(Exception):
    pass

class TextSplitterError(Exception):
    pass

# Streamlit UI
st.title("Text Splitter Playground")
st.info("""Split a text into chunks using a **Text Splitter**. Parameters include:

- `chunk_size`: Max size of the resulting chunks (in either characters or tokens, as selected)
- `chunk_overlap`: Overlap between the resulting chunks (in either characters or tokens, as selected)
- `length_function`: How to measure lengths of chunks, examples are included for either characters or tokens
- The type of the text splitter, this largely controls the separators used to split on
""")
col1, col2, col3, col4 = st.columns([1, 1, 1, 2])

with col1:
    chunk_size: int = st.number_input(min_value=1, label="Chunk Size", value=1000)

with col2:
    # Setting the max value of chunk_overlap based on chunk_size
    chunk_overlap: int = st.number_input(
        min_value=1,
        max_value=chunk_size - 1,
        label="Chunk Overlap",
        value=int(chunk_size * 0.2),
    )

    # Display a warning if chunk_overlap is not less than chunk_size
    if chunk_overlap >= chunk_size:
        st.warning("Chunk Overlap should be less than Chunk Length!")

with col3:
    length_function: str = st.selectbox(
        "Length Function", ["Characters", "Tokens"]
    )

splitter_choices: List[str] = ["RecursiveCharacter", "Character"] + [str(v) for v in Language]

with col4:
    splitter_choice: str = st.selectbox(
        "Select a Text Splitter", splitter_choices
    )

try:
    if length_function == "Characters":
        length_function: Callable[[str], int] = len
        length_function_str: str = code_snippets.CHARACTER_LENGTH
    elif length_function == "Tokens":
        enc = tiktoken.get_encoding("cl100k_base")


        def length_function(text: str) -> int:
            return len(enc.encode(text))


        length_function_str: str = code_snippets.TOKEN_LENGTH
    else:
        raise InvalidInputError("Invalid length function selected")

    if splitter_choice == "Character":
        import_text: str = code_snippets.CHARACTER.format(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=length_function_str
        )

    elif splitter_choice == "RecursiveCharacter":
        import_text: str = code_snippets.RECURSIVE_CHARACTER.format(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=length_function_str
        )

    elif "Language." in splitter_choice:
        import_text: str = code_snippets.LANGUAGE.format(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            language=splitter_choice,
            length_function=length_function_str
        )
    else:
        raise InvalidInputError("Invalid text splitter selected")

    st.info(import_text)

    # Box for pasting text
    doc: str = st.text_area("Paste your text here:")

    # Split text button
    if st.button("Split Text"):
        try:
            # Choose splitter
            if splitter_choice == "Character":
                splitter: CharacterTextSplitter = CharacterTextSplitter(separator = "\n\n",
                                             chunk_size=chunk_size, 
                                             chunk_overlap=chunk_overlap,
                                             length_function=length_function)
            elif splitter_choice == "RecursiveCharacter":
                splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, 
                                                      chunk_overlap=chunk_overlap,
                                             length_function=length_function)
            elif "Language." in splitter_choice:
                language: str = splitter_choice.split(".")[1].lower()
                splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter.from_language(language,
                                                                        chunk_size=chunk_size,
                                                                        chunk_overlap=chunk_overlap,
                                             length_function=length_function)
            else:
                raise InvalidInputError("Invalid text splitter selected")
            # Split the text
            splits: List[str] = splitter.split_text(doc)

            # Display the splits
            for idx, split in enumerate(splits, start=1):
                st.text_area(
                    f"Split {idx}", split, height=200
                )
        except Exception as e:
            logging.error("Error occurred while splitting text", exc_info=True)
            st.error(f"An error occurred while splitting the text: {str(e)}")

except InvalidInputError as e:
    st.error(f"Invalid input: {str(e)}")
except Exception as e:
    logging.error("Unexpected error occurred", exc_info=True)
    st.error(f"An unexpected error occurred: {str(e)}")
