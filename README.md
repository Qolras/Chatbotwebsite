# Flask Chat Application

This project is a simple Flask application that interacts with OpenAI's API to create a chatbot. The application is set up to run in a local development environment using Visual Studio Code (VS Code) or Google Colab.

## Author

Sultan Fakhroo

[LinkedIn Profile](https://www.linkedin.com/in/sultan-fakhroo-01412630b)

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Setup Instructions for VS Code

1. **Clone the repository** (if you are using version control):
    ```sh
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - **Windows**:
        ```sh
        venv\Scripts\activate
        ```
    - **macOS and Linux**:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set your OpenAI API key**:
    - Create a `.env` file in the root directory of your project and add your OpenAI API key:
        ```env
        OPENAI_API_KEY=your_openai_api_key
        ```

6. **Run the Flask application**:
    ```sh
    python app.py
    ```

7. **Access the application**:
    - Open your browser and go to `http://127.0.0.1:5000/`

## Setup Instructions for Google Colab

For a more in-depth step-by-step process, you can follow the instructions in the Google Colab notebook:

[Google Colab Notebook](https://colab.research.google.com/drive/1vNR2B7mG2ezJUDwllHvMRGUMGFQIJUpN?usp=sharing)

## Project Structure

├── app.py
├── requirements.txt
├── README.md
└── templates
└── index.html

- `app.py`: The main Flask application script.
- `requirements.txt`: The list of required Python packages.
- `README.md`: This file with setup instructions.
- `templates/index.html`: The HTML file for the chat interface.

## Usage

- Open the application in your browser.
- Type a message in the input box and click "Send" to interact with the chatbot.

## License

This project is licensed under the MIT License.

**Additional Steps for VS Code**

## 1 Install VS Code Extensions:

Python (for Python support)
Python Environment Manager (optional, for easy virtual environment management)
Configure the Python Interpreter:

## 2 Open VS Code.
Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the command palette.
Type Python: Select Interpreter.
Choose the interpreter from the virtual environment you created (venv).

***This setup ensures that you have a clear, step-by-step guide for running your Flask application in VS Code. The README.md file provides all necessary instructions, including a link to the Google Colab notebook for a detailed setup, and the requirements.txt lists the dependencies required to run the project.***