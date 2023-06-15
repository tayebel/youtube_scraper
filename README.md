# YouTube Channels Statistics Dashboard
![Table](image1.png)
![Figures](image2.png)

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Keyword Search](#keyword-search)
- [Exporting Data](#exporting-data)
- [Contributing](#contributing)


## Introduction

The YouTube Channel Statistics Dashboard is a simple Python tool that generates an interactive dashboard using the Plotly library. It allows users to visualize various (Views, Total videos and Number subscribers) statistics of YouTube channels based on keywords provided by the user. The dashboard provides a comprehensive overview of the channel's performance and allows users to save the results as an Excel spreadsheet.

## Installation



   ```bash
   git clone https://github.com/tayebel/yt.git
   cd yt
   pip install  -r requirements.txt  -t ./
   ```
   
## Usage
Run the Python script:
```bash
 python run.py
 ```
    
Open your web browser and visit http://localhost:8052 to access the dashboard.

## Configuration
Before running the tool, make sure to configure the following :

API_KEY: Your YouTube Data API key. You can obtain one by following the instructions at https://developers.google.com/youtube/registering_an_application.


## Keyword Search
To search for YouTube channels based on keywords, follow these steps:

Enter one or more keywords in the search bar provided.

Click the "update inputs" button to initiate the search.

The tool will retrieve the search results from YouTube and display them on the dashboard.

You can also increase the number of results using maximumResults.

## Exporting Data
To export the displayed statistics as an Excel spreadsheet, follow these steps click the "Save Excel Sheet" button located at the top-left corner of the dashboard.

## Contributing
Contributions to the YouTube Channel Statistics Dashboard are welcome! If you find any bugs or have suggestions for improvements, please open an issue on the GitHub repository. If you would like to contribute code, feel free to submit a pull request.

Please ensure that your contributions adhere to the coding conventions and include appropriate tests and documentation.




 
