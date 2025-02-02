import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter, Language
import code_snippets as code_snippets
import tiktoken

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

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
    chunk_size = st.number_input(min_value=1, label="Chunk Size", value=1000)

with col2:
    # Setting the max value of chunk_overlap based on chunk_size
    chunk_overlap = st.number_input(
        min_value=1,
        max_value=chunk_size - 1,
        label="Chunk Overlap",
        value=int(chunk_size * 0.2),
    )

    # Display a warning if chunk_overlap is not less than chunk_size
    if chunk_overlap >= chunk_size:
        st.warning("Chunk Overlap should be less than Chunk Length!")

with col3:
    length_function = st.selectbox(
        "Length Function", ["Characters", "Tokens"]
    )

splitter_choices = ["RecursiveCharacter", "Character"] + [str(v) for v in Language]

with col4:
    splitter_choice = st.selectbox(
        "Select a Text Splitter", splitter_choices
    )

if length_function == "Characters":
    length_function = len
    length_function_str = code_snippets.CHARACTER_LENGTH
elif length_function == "Tokens":
    enc = tiktoken.get_encoding("cl100k_base")


    def length_function(text: str) -> int:
        return len(enc.encode(text))


    length_function_str = code_snippets.TOKEN_LENGTH
else:
    raise ValueError

if splitter_choice == "Character":
    import_text = code_snippets.CHARACTER.format(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=length_function_str
    )

elif splitter_choice == "RecursiveCharacter":
    import_text = code_snippets.RECURSIVE_CHARACTER.format(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=length_function_str
    )

elif "Language." in splitter_choice:
    import_text = code_snippets.LANGUAGE.format(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        language=splitter_choice,
        length_function=length_function_str
    )
else:
    raise ValueError

st.info(import_text)

# Box for pasting text
doc = st.text_area("Paste your text here:")

# Dropdown for selecting sorting algorithm
sort_algorithm = st.selectbox(
    "Select a Sorting Algorithm",
    ["None", "Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
)

# Split text button
if st.button("Split Text"):
    # Choose splitter
    if splitter_choice == "Character":
        splitter = CharacterTextSplitter(separator = "\n\n",
                                         chunk_size=chunk_size, 
                                         chunk_overlap=chunk_overlap,
                                         length_function=length_function)
    elif splitter_choice == "RecursiveCharacter":
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, 
                                                  chunk_overlap=chunk_overlap,
                                         length_function=length_function)
    elif "Language." in splitter_choice:
        language = splitter_choice.split(".")[1].lower()
        splitter = RecursiveCharacterTextSplitter.from_language(language,
                                                                chunk_size=chunk_size,
                                                                chunk_overlap=chunk_overlap,
                                         length_function=length_function)
    else:
        raise ValueError
    # Split the text
    splits = splitter.split_text(doc)

    # Sort the splits if a sorting algorithm is selected
    if sort_algorithm == "Bubble Sort":
        splits = bubble_sort(splits)
    elif sort_algorithm == "Selection Sort":
        splits = selection_sort(splits)
    elif sort_algorithm == "Insertion Sort":
        splits = insertion_sort(splits)
    elif sort_algorithm == "Merge Sort":
        splits = merge_sort(splits)
    elif sort_algorithm == "Quick Sort":
        splits = quick_sort(splits)

    # Display the splits
    for idx, split in enumerate(splits, start=1):
        st.text_area(
            f"Split {idx}", split, height=200
        )