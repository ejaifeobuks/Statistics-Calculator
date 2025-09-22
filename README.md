# Statistics Calculator

A comprehensive Python-based calculator application with advanced statistical analysis capabilities, built using Tkinter for the graphical user interface.

## About This Project

This is a personal project created to learn and demonstrate proficiency in several key Python concepts:

- **API Integration**: Working with external APIs (Wolfram Alpha) for enhanced functionality
- **GUI Development**: Building responsive user interfaces with Tkinter
- **Object-Oriented Programming**: Implementing classes and methods for clean, modular code structure
- **Statistical Computing**: Applying mathematical concepts through programming

The project serves as a practical learning exercise that combines theoretical knowledge with real-world application development.

## Features

### 🧮 Basic Calculator

- Standard arithmetic operations (+, -, \*, /)
- Parentheses support for complex expressions
- Number input via GUI buttons or keyboard
- Clear function and error handling

### 📊 Statistical Functions

- **Mean**: Calculate the average of a dataset
- **Median**: Find the middle value in a sorted dataset
- **Mode**: Identify the most frequently occurring value
- **Range**: Calculate the difference between max and min values
- **Standard Deviation**: Measure data spread from the mean
- **Variance**: Calculate the square of standard deviation
- **Coefficient of Variation**: Relative measure of variability
- **Linear Regression**: Analyze relationships between X and Y variables

### 🤖 AI Integration

- **Ask an AI**: Upload text files and get step-by-step solutions via Wolfram Alpha API
- Automatic image saving of mathematical solutions

### 🎨 User Interface

- Clean, intuitive GUI with multiple panels
- Responsive design that adapts to window resizing
- Keyboard input support
- Multiple calculation modes (Basic, Statistics, Scientific, Graphs)

## Installation

### Prerequisites

```bash
pip install tkinter pillow requests numpy
```

### Required Libraries

- `tkinter` - GUI framework (usually included with Python)
- `PIL` (Pillow) - Image processing
- `requests` - HTTP requests for API calls
- `numpy` - Numerical computations
- `statistics` - Built-in statistical functions

## Usage

### Running the Application

```bash
python "Calculator Program.py"
```

### Basic Operations

1. **Number Input**: Click number buttons or type directly
2. **Arithmetic**: Use +, -, \*, / for basic calculations
3. **Clear**: Press 'C' to clear the current expression
4. **Equals**: Press '=' or Enter to evaluate

### Statistical Analysis

1. **Switch to Statistics Mode**: Click the "Statistics" button
2. **Input Data**: Enter comma-separated values (e.g., "1,2,3,4,5")
3. **Calculate**: Click the desired statistical function button
4. **View Results**: Results appear in the display area

### Linear Regression

1. Switch to Statistics mode
2. Click "X-values" and input your X data points
3. Click "Y-values" and input your Y data points
4. Click "Regression" to get slope and intercept values

### AI Assistance

1. Click "Ask an AI" button
2. Select a text file containing your mathematical problem
3. The application will query Wolfram Alpha and save solution images

## File Structure

```
Statistics-Calculator/
├── Calculator Program.py    # Main application file
├── mathematical_functions.py # Statistical functions and calculations
├── README.md               # Project documentation
└── __pycache__/           # Python cache files
```

## Code Architecture

### StatTools Class

The core of the statistical functionality is the `StatTools` class in `mathematical_functions.py`:

- **Expression Management**: Handles user input and number extraction
- **Statistical Calculations**: Provides methods for all statistical functions
- **Error Handling**: Manages edge cases and invalid inputs

### GUI Components

- **Dynamic Button System**: Buttons change function based on selected mode
- **Responsive Layout**: Grid system that adapts to window resizing
- **Event Handling**: Keyboard and mouse input support

## Configuration

### Wolfram Alpha API

To use the AI features, you need to:

1. Get an API key from [Wolfram Alpha Developer Portal](https://developer.wolframalpha.com/)
2. Replace `YOUR_APP_ID` in the code with your actual API key

## Contributing

Feel free to contribute to this project by:

- Adding new statistical functions
- Improving the user interface
- Implementing the Scientific and Graphs panels
- Adding more visualization features

## License

This project is open source. Feel free to use and modify as needed.

## Author

Created by OgheneobukomeEjaife

---

**Note**: The Scientific and Graphs panels are placeholders for future development. The current implementation focuses on basic arithmetic and comprehensive statistical analysis.
