# Dio Courses Downloader

## Preview
![Watch the demonstration](./Project_Demonstration.mp4)


## Overview

Dio Courses Downloader is a Python script designed to automate the process of downloading videos of the classes related to specific courses from the Dio platform. This tool is particularly useful for educators, students, or anyone looking to gather video resources for learning or teaching purposes. 

## Features

- Automates the process of downloading relevant videos from specified courses.
- Supports interaction with the Firefox browser for video retrieval.
- Organizes downloaded videos into structured folders based on course and institution.

## Requirements

Before running the script, ensure you have the following Python libraries installed:

```bash
pip install -r requirements.txt
```

Note: The script is currently optimized for use with Firefox and chrome. Support for other browsers may be limited or require additional configuration.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Ensure all dependencies are installed using pip.

## Usage

1. Open a terminal or command prompt.
2. Run the script using Python:

```bash
python main.py
```

3. Follow the prompts and enter the path where you want to save the videos
4. Follow the prompts to enter the name of the institution and course you wish to download videos from.
5. Once prompted, navigate to the course website and select the lesson you want to download videos from.
6. After completing the setup, press any key to start the download process.

### Important Notes

- The script requires manual navigation to the course website selection of the lesson. Ensure you have Firefox or chrome installed and set as your default browser.
- The script uses images stored in the `images` directory within the project folder. Ensure this directory contains the correct images for the browser you are using (currently supported: Firefox).
- Downloaded images will be saved in a structured directory format based on the institution and course name.

## Contributing

Contributions to improve functionality, add support for more browsers, or enhance the script's capabilities are welcome. Please submit pull requests or issues through the GitHub repository.