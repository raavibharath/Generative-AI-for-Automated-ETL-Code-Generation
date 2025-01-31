## Project Overview

This project provides a Flask web application that uses a pre-trained GPT-2 model to generate ETL (Extract, Transform, Load) code based on user descriptions.

## Features

- Generates Python ETL scripts from user-provided descriptions.
- Uses GPT-2 for natural language processing.
- Runs locally with minimal setup.

## Installation and Setup

### Step 1: Install Python
Ensure you have Python 3.8 or higher installed. You can download it from [python.org](https://python.org).

### Step 2: Clone the Repository
```bash
git clone https://github.com/yourusername/etl-code-generator.git
cd etl-code-generator
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

### Step 1: Start the Flask App
```bash
python app.py
```

### Step 2: Open in Browser
Visit `http://127.0.0.1:5000/` in your web browser.

### Step 3: Generate ETL Code
1. Enter an ETL description in the text box (e.g., "Extract data from a CSV and load into PostgreSQL").
2. Click "Generate Code."
3. The generated Python ETL script will be displayed.

## Project Files

1. **app.py** - Main Application File
   - Contains the Flask web application, loads the GPT-2 model, and handles user input.

2. **requirements.txt** - Dependencies File
   - Lists required libraries:
     - `flask`
     - `transformers`
     - `torch`

## Skills & Technologies

- **Flask** - Lightweight web framework for Python.
- **GPT-2 (via Hugging Face Transformers)** - Pre-trained language model for natural language processing.
- **Python** - Programming language used for ETL scripting and web application development.
- **PyTorch** - Deep learning framework used for running GPT-2.
  
## Contributions & Feedback

Feel free to fork this repository, submit pull requests, or raise issues. Your feedback is highly appreciated!
