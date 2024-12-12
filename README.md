# Vietnamese ID Card Information Extractor (Client)

This project focuses on extracting key information from the front side of Vietnamese ID cards, including ID number, name, and address. It provides a React-based client-side application that enables users to upload card images, view the processing steps in real-time, and manage extracted results efficiently.

Explore the full repository: [Vietnamese ID Card Information Extractor (Client)](https://github.com/bp82125/vietid-extractor-client)

## Technologies Used
- **YOLOv8, YOLOv8-Seg**: For object detection and segmentation of ID card regions.
- **CRAFT**: For detecting and extracting text from the card.
- **VietOCR Transformer**: For Vietnamese text recognition.
- **Flask**: Backend framework handling processing logic and API endpoints.
- **MongoDB**: For storing extracted results.
- **Python**: Core programming language used for backend processing.

## Getting Started

### Prerequisites
- Python version 3.12 or higher.
- (Optional) WSL2 with Ubuntu 22.04 for a Linux-based development environment.

## Installation

### Clone the Repository


```bash
git clone https://github.com/bp82125/vietid-extractor-client.git
cd vietid-extractor-client
```

### Install Miniconda
Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html) based on your operating system.

### Create and Activate the Conda Environment
1. Navigate to the project directory where the `environment.yaml` file is located.
2. Run the following commands to create and activate the Conda environment:

```bash
# Create the environment using the environment.yaml file
conda env create -f environment.yaml

# Activate the environment
conda activate vietid-extractor
```

### Configure the .env File
Before running the application, you need to configure environment variables. Follow these steps:

1. Locate the .env.example file in the project directory.
2. Create a new .env file by copying .env.example:
```bash
cp .env.example .env
```
3. Open the .env file and update the values as needed. Below are the default settings:
```
MONGO_URI=mongodb://localhost:27017/VietID
MONGO_COLLECTION_NAME=id
```
- MONGO_URI: The connection string for your MongoDB instance. Replace localhost with your MongoDB host if running on a remote server or a cloud database service.
- MONGO_COLLECTION_NAME: The name of the MongoDB collection where extracted data will be stored.

## Run the Project

Once the environment is set up and the `.env` file is configured, you can start the project:
```bash
python app.py
```
This will launch the application. You should see an output similar to the following:
```bash
 * ...
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```



