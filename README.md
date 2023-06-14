# YouTube Channel Statistics Dashboard


## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Keyword Search](#keyword-search)
- [Exporting Data](#exporting-data)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The YouTube Channel Statistics Dashboard is a Python tool that generates an interactive dashboard using the Plotly library. It allows users to visualize various statistics of YouTube channels based on keywords provided by the user. The dashboard provides a comprehensive overview of the channel's performance and allows users to save the results as an Excel spreadsheet.

## Installation



   ```bash
   git clone https://github.com/your-username/youtube-stats-dashboard.git
   cd youtube-stats-dashboard
   pip install -r requirements.txt
   
## Usage
Run the Python script:
```bash
    python run.py
 ```
    
Open your web browser and visit http://localhost:8000 to access the dashboard.

## Configuration
Before running the tool, make sure to configure the following settings in the config.json file:

API_KEY: Your YouTube Data API key. You can obtain one by following the instructions at https://developers.google.com/youtube/registering_an_application.

SEARCH_RESULTS: The maximum number of search results to retrieve for each keyword. Increase this value if you want to retrieve more results but note that it may take longer to process.

Keyword Search
To search for YouTube channels based on keywords, follow these steps:

Enter one or more keywords in the search bar provided.

Click the "Search" button to initiate the search.

The tool will retrieve the search results from YouTube and display them on the dashboard.

##Exporting Data
To export the displayed statistics as an Excel spreadsheet, follow these steps:

Click the "Export" button located at the top-right corner of the dashboard.

##Contributing
Contributions to the YouTube Channel Statistics Dashboard are welcome! If you find any bugs or have suggestions for improvements, please open an issue on the GitHub repository. If you would like to contribute code, feel free to submit a pull request.

Please ensure that your contributions adhere to the coding conventions and include appropriate tests and documentation.




 
