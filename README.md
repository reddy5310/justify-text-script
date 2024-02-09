# Justify Text Python Script

This project provides a Python script, `justify_text.py`, that justifies text to a specified width. The script breaks a paragraph into lines, ensuring that each line does not exceed the specified page width. It then justifies the text in each line both left and right, except for the last line, which is left-justified. Accompanying the script is a test suite `test_justify_text.py`, which validates the functionality of the text justification through various unit tests.

## Features

- Text justification to a specified width without breaking words.
- Left and right justification of lines for a clean and professional appearance.
- Unit tests to ensure reliability and correctness of the text justification logic.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Install Python on your machine:

```bash
Python 3.x
```

### Installing

A step by step process:

1. Clone the repository using HTTPS:
```bash
git clone https://github.com/yourusername/justify-text-script.git
```

2. Navigate to the cloned directory:
```bash
cd <cloned-directory>
```

3. Run the script with Python:
```bash
python justify_text.py
```

### Running the Tests

To run the automated tests for this system, execute:
```bash
python -m unittest test_justify_text.py
```

### Usage Example

To justify text using the justify_text.py script, run the script with Python and follow the prompts to input your paragraph and desired page width. Here's a command to start the script:

```python
python justify_text.py
```
Example Input:

```bash
Enter a paragraph: This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.
Enter page width: 20
```

Expected Output:

```bash
Array [1] = "This is a sample"
Array [2] = "text but a"
Array [3] = "complicated problem"
Array [4] = "to be solved, so we"
Array [5] = "are adding more text"
Array [6] = "to see that it"
Array [7] = "actually works."
```
---
