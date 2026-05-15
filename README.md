# AI Study Assistant

## Description
AI Study Assistant is a Python-based command-line application that uses a simple tool-based architecture to assist users with study-related tasks. The assistant can perform mathematical calculations and read text files through modular tools.

---

## Features
- Perform mathematical calculations
- Read content from text files
- Tool-based modular architecture
- Automated testing using pytest
- Simple command-line interaction

---

## Project Structure

```bash
ai-study-assistant/
│
├── main.py
├── README.md
├── requirements.txt
├── journal_step3.docx
│
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   └── file_reader.py
│
├── tests/
│   ├── __init__.py
│   └── test_tools.py
```

---

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the program using:

```bash
python main.py
```

Example commands:

```bash
calculate 2+3*4
read file notes.txt
```

Type:

```bash
exit
```

to close the assistant.

---

## Running Tests

Run all tests using pytest:

```bash
pytest tests
```

Expected result:

```bash
3 passed
```

---

## Technologies Used
- Python 3
- Pytest
- VS Code
- Git & GitHub

---

## Current Progress
- Step 1 – Project Setup Completed
- Step 2 – Initial Implementation Completed
- Step 3 – Testing and Documentation Completed