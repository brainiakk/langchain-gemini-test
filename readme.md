## Google Cloud Vertex AI Chatbot

This repository contains code and instructions on creating a simple chatbot using Langchain w/ Google Cloud's Vertex AI platform and the Gemini 1.5 Pro model.

### Prerequisites

* A Google Cloud Platform (GCP) account with billing enabled.
* Python 3.9 or later installed on your local machine.
* A text editor or IDE of your choice.

### Setup

1. **Create a Google Cloud Project:**
 * If you don't have an existing project, create one in the Google Cloud Console.
2. **Enable the Vertex AI API:**
 * Navigate to the Vertex AI section in the console and enable the API if it's not already enabled.
3. **Create a Service Account:**
 * Go to the IAM & Admin > Service Accounts section.
 * Create a new service account.
 * Grant the "Vertex AI User" role to the service account.
 * Download the JSON key file for the service account.
4. **Set Environment Variables:**
 * Create a `.env` file in the root directory of this repository.
 * Add the following line, replacing `path/to/your/keyfile.json` with the actual path to your downloaded key file:

 ```
 GOOGLE_APPLICATION_CREDENTIALS="path/to/your/keyfile.json"
 ```

### Installation

1. **Clone the Repository:**
 ```bash
 git clone https://github.com/brainiakk/langchain-gemini-test.git
 cd langchain-gemini-test
 ```
2. **Install Dependencies:**
 ```bash
 pip install -r requirements.txt
 ```

### Running the Chatbot

1. **Run the Python Script:**
 ```bash
 python -m main
 ```
2. **Interact with the Chatbot:**
 * The script will start a loop and prompt you for input.
 * Type your query and press Enter.
 * The chatbot will respond using the Gemini Pro model.

### Code Explanation

* **`load_dotenv()`:** This line loads environment variables from the `.env` file, including the path to your service account key file.
* **`llm = ChatVertexAI(...)`:** This line initializes the `ChatVertexAI` object from the `vertexai.preview.language_models` library. It specifies the Gemini Pro model and a temperature value for controlling the randomness of the responses.
* **`response = llm.invoke(text)`:** This line sends the user's input (`text`) to the Vertex AI API for processing by the Gemini Pro model.
* **`print(response.content)`:** This line prints the model's response to the console.

### Notes

* The code provided is a basic example and can be extended with additional features.
* Refer to the Vertex AI documentation for more advanced usage and customization options.
* Remember to replace `path/to/your/keyfile.json` with the actual path to your service account key file.

### Disclaimer

This code is provided for educational purposes only.