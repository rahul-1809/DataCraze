# Twitter Analytics Dashboard

## Overview

DataCraze is an interactive web-based Twitter analytics dashboard developed using **Streamlit** and **Plotly**. It helps users analyze tweet engagement metrics including retweets, likes, views, and user statistics. The dashboard supports filtering by language and date range to allow focused insights.

This project was built using a dataset of over **150,000 preprocessed tweets** sourced from a larger dataset of more than **300,000 tweets**.

**Live App:** [https://twitter-analytics.streamlit.app](https://twitter-analytics.streamlit.app/)

## Features

* **Language and Date Filters**: Narrow down analysis based on selected languages and date ranges.
* **Key Metrics**: View total tweets, likes, retweets, followers, and average engagement statistics.
* **Interactive Graphs**:

  * Daily trends of retweets, likes, and views.
  * Language distribution pie chart.
  * Engagement by author verification status.
  * Scatter plot of retweets vs. likes.
  * Histogram of author follower counts.
  * Correlation matrix of engagement features.
  * Average retweets per day.

## Tech Stack

* **Streamlit**: For building the dashboard interface.
* **Pandas**: For data manipulation.
* **Plotly**: For generating interactive visualizations.
* **Python**: Backend scripting and logic.

## Dataset

The dataset used in this project contains tweets and metadata such as:

* `retweetCount`, `likeCount`, `viewCount`
* `author_followers`, `author_following`
* `lang`, `date`, `author_isVerified`

The data was preprocessed to handle missing values, convert datatypes, and ensure consistency for visualization.

## Getting Started

### Installation

1. Clone the repository:

```bash
git clone https://github.com/rahul-1809/DataCraze.git
cd DataCraze
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure you have the preprocessed dataset `final_preprocessed.csv` in the project root directory.

4. Run the app:

```bash
streamlit run app.py
```

Then, open your browser and go to `http://localhost:8501`.

## Live Demo

Visit the live dashboard hosted on Streamlit Cloud:
👉 [https://twitter-analytics.streamlit.app](https://twitter-analytics.streamlit.app/)

## Project Highlights

* Built during a data analytics competition.
* Focus on visual clarity and interactivity.
* Modular, scalable, and easy to extend for other social media platforms.

## License

This project is licensed under the MIT License.
