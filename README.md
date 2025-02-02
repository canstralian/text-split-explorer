# Text Split Explorer

![ui.png](ui.png)

Many of the most important LLM applications involve connecting LLMs to external sources of data.
A prerequisite to doing this is to ingest data into a format where LLMs can easily connect to them.
Most of the time, that means ingesting data into a vectorstore.
A prerequisite to doing this is to split the original text into smaller chunks.

While this may seem trivial, it is a nuanced and overlooked step.
When splitting text, you want to ensure that each chunk has cohesive information - e.g. you don't just want to split in the middle of sentence.
What "cohesive information" means can differ depending on the text type as well.
For example, with Markdown you have section delimiters (`##`) so you may want to keep those together, while for splitting Python code you may want to keep all classes and methods together (if possible).

This repo (and associated Streamlit app) are designed to help explore different types of text splitting.
You can adjust different parameters and choose different types of splitters.
By pasting a text file, you can apply the splitter to that text and see the resulting splits.
You are also shown a code snippet that you can copy and use in your application

## Hosted App

To use the hosted app, head to [https://langchain-text-splitter.streamlit.app/](https://langchain-text-splitter.streamlit.app/)

## Running locally

To run locally, first set up the environment by cloning the repo and running:

```shell
pip install -r requirements
```

Then, run the Streamlit app with:

```shell
streamlit run splitter.py
```

## Examples and Use Cases

### Example 1: Splitting a Markdown File

Suppose you have a Markdown file with the following content:

```markdown
# Introduction

This is the introduction section.

## Section 1

This is the first section.

## Section 2

This is the second section.
```

You can use the `CharacterTextSplitter` to split the Markdown file into chunks based on the section delimiters (`##`). The resulting chunks will be:

1. `# Introduction\n\nThis is the introduction section.`
2. `## Section 1\n\nThis is the first section.`
3. `## Section 2\n\nThis is the second section.`

### Example 2: Splitting a Python Code File

Suppose you have a Python code file with the following content:

```python
class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass
```

You can use the `RecursiveCharacterTextSplitter` to split the Python code file into chunks based on the class and method definitions. The resulting chunks will be:

1. `class MyClass:\n    def method1(self):\n        pass`
2. `def method2(self):\n        pass`

## Frequently Asked Questions (FAQs)

### How do I install the required dependencies?

To install the required dependencies, run the following command:

```shell
pip install -r requirements.txt
```

### How do I run the Streamlit app locally?

To run the Streamlit app locally, use the following command:

```shell
streamlit run splitter.py
```

### How do I contribute to the project?

Please refer to the [Contribution Guide](#contribution-guide) for detailed instructions on how to contribute to the project.

## Contribution Guide

We welcome contributions to the Text Split Explorer project! To contribute, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Set up the development environment by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

3. Create a new branch for your feature or bug fix:

   ```shell
   git checkout -b my-feature-branch
   ```

4. Make your changes and commit them with a descriptive commit message:

   ```shell
   git commit -m "Add feature: description of the feature"
   ```

5. Push your changes to your forked repository:

   ```shell
   git push origin my-feature-branch
   ```

6. Create a pull request from your branch to the main repository's `main` branch.

### Running Tests

To run the tests, use the following command:

```shell
pytest
```

### Code Style

We use `flake8` for linting and `black` for code formatting. Please ensure that your code adheres to the following guidelines:

- Run `flake8` to check for linting issues:

  ```shell
  flake8 .
  ```

- Run `black` to format your code:

  ```shell
  black .
  ```

### Documentation

Please ensure that your code is well-documented with comments and docstrings. This helps other contributors understand the purpose and functionality of different parts of the code.

### Submitting Pull Requests

When submitting a pull request, please provide a clear and concise description of the changes you have made. Include any relevant issue numbers and provide context for the changes.

Thank you for contributing to the Text Split Explorer project!
