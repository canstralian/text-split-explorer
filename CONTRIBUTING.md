# Contribution Guide

We welcome contributions to the Text Split Explorer project! To contribute, please follow these steps:

## Setting Up the Development Environment

1. Fork the repository and clone it to your local machine.
2. Set up the development environment by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests, use the following command:

```shell
pytest
```

## Submitting Pull Requests

1. Create a new branch for your feature or bug fix:

   ```shell
   git checkout -b my-feature-branch
   ```

2. Make your changes and commit them with a descriptive commit message:

   ```shell
   git commit -m "Add feature: description of the feature"
   ```

3. Push your changes to your forked repository:

   ```shell
   git push origin my-feature-branch
   ```

4. Create a pull request from your branch to the main repository's `main` branch.

## Code Style

We use `flake8` for linting and `black` for code formatting. Please ensure that your code adheres to the following guidelines:

- Run `flake8` to check for linting issues:

  ```shell
  flake8 .
  ```

- Run `black` to format your code:

  ```shell
  black .
  ```

## Documentation

Please ensure that your code is well-documented with comments and docstrings. This helps other contributors understand the purpose and functionality of different parts of the code.

## Best Practices

- Follow the existing code style and structure.
- Write clear and concise commit messages.
- Keep your changes focused and avoid making unrelated changes in a single pull request.
- Test your changes thoroughly before submitting a pull request.

Thank you for contributing to the Text Split Explorer project!
