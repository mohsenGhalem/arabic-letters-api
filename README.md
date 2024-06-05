# Arabic Letter Recognition FastAPI Application

This project is a FastAPI application that performs Arabic letter recognition using a TensorFlow Keras model. The model has an accuracy of 98% and is trained to recognize Arabic letters on a purple background color with the letter itself in yellow color for best accuracy.
## Repository

The code for data training and processing can be found in the [arabic-handwritten-letters-recognition.ipynb](./arabic-handwritten-letters-recognition.ipynb) file.

## Prerequisites

Before running the application, make sure you have the following installed:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Python virtual environment (venv): [Installation Guide](https://docs.python.org/3/library/venv.html)

## Getting Started

1. Clone the repository:

    ```shell
    git clone https://github.com/your-username/arabic-letters-api.git
    ```

2. Navigate to the project directory:

    ```shell
    cd arabic-letters-api
    ```
## Installation

To run this application, you have two options: using Docker or Python virtual environment (venv).

### Docker

1. Install Docker on your machine.
2. Build the Docker image using the provided Dockerfile:
    ```bash
    docker build -t arabic-letter-recognition .
3. Run the Docker container:

    ```bash
    docker run -p 8000:8000 arabic-letters-api
    ```
### Python venv

3. Create a Python virtual environment:

    ```shell
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

      ```shell
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```shell
      source venv/bin/activate
      ```

5. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

6. Run the application :

    ```shell
    uvicorn main:app --host 0.0.0.0 --port 80
    ```

## API Usage

Once the application is running, you can send POST requests to the following endpoint to recognize Arabic letters:

API endpoint to process an uploaded file containing an Arabic letter image.

    Endpoint: /letter

    Parameters:
    - file: UploadFile object representing the uploaded file.

    Returns:
    - The result of processing the image.

    Example:
    - Request:
        POST /letter
        Body: Form data with key 'file' and value as the uploaded file.

    - Response:
        {
            "has_error": bool,
            "data": {
                "letter": "label in english",
                "letter-ar": "label in arabic",
                "letter-index": "index of the predictied letter"
            },
            "error": "error message",
            "confidence": double
        }
