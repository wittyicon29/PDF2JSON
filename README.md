# PDF2JSON

## Overview

Resume Extractor is a tool designed to analyze and extract key information from resumes in PDF format. Leveraging the power of language models, this tool parses resumes to output clean, structured data in JSON format. It focuses on extracting essential sections such as the person's name, education, experience, and skills while excluding irrelevant details.

## Features

- **PDF Loading**: Seamlessly loads and processes PDF resumes.
- **Information Extraction**: Extracts title, education, experience, and skills from resumes.
- **Data Cleaning**: Removes irrelevant details and special characters.
- **Structured Output**: Outputs data in a clean, well-formatted JSON structure.
- **Error Handling**: Manages missing sections by leaving them empty in the JSON output.

## Getting Started

### Prerequisites

- Python 3.7+
- Required Python packages: `langchain_community`, `langchain_core`, `langchain_groq`, `pydantic_v1`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/wittyicon29/PDF2JSON.git
    cd PDF2JSON
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Place the resume PDF in the project directory and name it `resume.pdf`.

2. Add your GROQ Cloud API Key at the `GROQ_API_KEY`.

3. Run the script:
    ```bash
    python extract_resume.py
    ```

4. The extracted information will be saved as `output.json`.

![image](https://github.com/user-attachments/assets/abedea4f-aa8a-4fc8-b305-36843e13b195)


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
