# Installation Guide

This document provides detailed instructions on how to install and set up the Text Split Explorer project.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.10 or higher
- pip (Python package installer)
- pipenv (Python dependency manager)

## Installation Steps

1. **Clone the repository**

   Clone the repository to your local machine using the following command:

   ```shell
   git clone https://github.com/your-username/text-split-explorer.git
   cd text-split-explorer
   ```

2. **Set up the development environment**

   Use pipenv to set up the development environment and install the required dependencies:

   ```shell
   pipenv install --dev
   ```

3. **Activate the virtual environment**

   Activate the virtual environment created by pipenv:

   ```shell
   pipenv shell
   ```

4. **Run the Streamlit app**

   Start the Streamlit app using the following command:

   ```shell
   streamlit run splitter.py
   ```

## Additional Information

For more details on how to use the Text Split Explorer, refer to the [Usage Guide](usage.md).

If you encounter any issues during the installation process, please refer to the [FAQ](faq.md) or open an issue on the GitHub repository.
