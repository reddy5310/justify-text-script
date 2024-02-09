# Justify Text Python Script

This Python script takes a paragraph of text and a page width (as an integer) and returns an array of strings that are both left and right justified according to the specified page width.

## Features

- Accepts any paragraph string as input.
- Accepts page width as input to adjust the justification.
- Ensures no words are broken in the process.
- Provides an array of strings as output, each string being a line justified according to the given page width.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

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

To use the script in your Python code:
```python
from justify_text import justify_text

paragraph = "Enter the paragraph here."
page_width = 20
print(justify_text(paragraph, page_width))
```

---
