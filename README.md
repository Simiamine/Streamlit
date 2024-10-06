# Tips Analysis and Uber Data Application

## Overview

This application, built using Streamlit, provides detailed analyses on two datasets: the **Tips dataset** and the **Uber dataset**. The application aims to explore various aspects of tipping behavior and Uber ride patterns through interactive visualizations and insightful metrics.

### Main Features

The application is divided into multiple sections to provide users with an interactive exploration of the data:

1. **Tips Analysis**
   - Understand customer tipping behavior and identify patterns in different tipping scenarios.
2. **Uber Analysis**
   - Analyze the ride data to determine peak hours, popular locations, and other trends.
3. **Joint Analysis**
   - Discover relationships between tipping behaviors and Uber ride patterns to gain comprehensive insights.

## Installation and Setup

To run this application, you need Python installed on your system. You will also need the required libraries, which you can install using the following command:

```bash
pip install streamlit pandas plotly
```

Once all dependencies are installed, you can launch the application by running:

```bash
streamlit run analysis_app.py
```

## Dataset Information

### Tips Dataset

The **tips.csv** dataset provides information about customer behavior in restaurants, specifically tipping patterns. The columns are:

- **total_bill**: Total bill amount (in dollars)
- **tip**: The tip amount (in dollars)
- **sex**: Gender of the customer (Male or Female)
- **smoker**: Whether the customer is a smoker (Yes or No)
- **day**: The day of the week (Thu, Fri, Sat, Sun)
- **time**: Time of the day (Lunch or Dinner)
- **size**: The size of the dining party

### Uber Dataset

The **uber-raw-data-apr14.csv** dataset contains information on Uber pickups throughout the city, including:

- **Date/Time**: The pickup time (date and hour)
- **Lat**: Latitude of the pickup location
- **Lon**: Longitude of the pickup location
- **Base**: The base code indicating the Uber station or type of ride

## Analysis Sections

### Tips Analysis

#### 1. Tipping Behavior Analysis

- **Distribution of Total Bill**: This analysis shows how much customers are typically spending using a histogram representation.
- **Distribution of Tips**: A histogram that displays the distribution of the tips given by customers.
- **Tip Percentage by Total Bill**: We calculate the tip percentage, which is plotted against the total bill to identify if higher bills lead to higher or lower tipping percentages.
- **Average Tip by Gender**: A bar chart to explore whether tipping behaviors differ between male and female customers.
- **Average Tip by Smoking Status**: Compares tipping amounts between smokers and non-smokers.

#### 2. Gender and Smoking Analysis

- **Average Tip by Gender and Smoking Status**: This bar chart visualizes how the average tipping amount changes depending on both the gender and smoking habits of the customers.
- **Tip Percentage by Gender and Smoking Status**: A box plot is used to show the distribution of tip percentages in each category, helping understand variations in tipping by customer gender and whether they smoke.

#### 3. Day and Time Analysis

- **Average Tip by Day of the Week**: Analysis of tipping habits on different days (e.g., are weekends more generous in tips?).
- **Average Tip by Time (Lunch/Dinner)**: Analysis of tipping behavior differences between lunch and dinner times.
- **Tip Percentage by Day of the Week**: A box plot showing the distribution of tipping percentages across different days of the week.

### Uber Analysis

#### 1. Temporal Analysis

- **Number of Trips by Hour**: Shows the distribution of Uber trips throughout the day, identifying peak hours.
- **Number of Trips by Day of Week**: Understand which days of the week are the busiest.
- **Average Number of Trips per Hour**: Calculates and presents the average trips per hour.

#### 2. Spatial Analysis

- **Map of Uber Pickups**: Visual representation of Uber pickup locations in NYC.
- **Top 10 Busiest Pickup Locations**: Identifies the busiest locations based on latitude and longitude, with a breakdown of their frequencies.

#### 3. Base Analysis

- **Number of Trips by Base**: Breakdown of Uber trips by different base codes (i.e., Uber station or type).
- **Analysis of Bases during Peak Hour**: Focused analysis during the peak hours to show which bases are most in demand.

#### 4. Trip Duration Analysis

- **Estimated Trip Duration Distribution**: Shows a histogram of estimated trip durations.
- **Trip Duration by Hour of Day**: A box plot that displays how trip duration changes depending on the hour.

#### 5. Heatmap Analysis

- **Heatmap of Pickups by Hour and Day of Week**: A heatmap to represent the frequency of pickups during different hours and days, allowing identification of peak periods.

### Joint Analysis

The **Joint Analysis** section provides insights by merging insights from both the Tips and Uber datasets.

#### 1. Temporal vs Tips Analysis

- **Average Tip Percentage vs Uber Trips by Hour**: A line chart showing the comparison between the average tip percentage and Uber trip frequency, normalized to make both metrics comparable.

#### 2. Spatial vs Tips Analysis

- **Tip Percentage by Uber Pickup Location**: A scatter mapbox plot that assigns Uber pickup locations to tips, allowing us to understand how tipping changes geographically across NYC.

## Features and Functionalities

### Sidebar Navigation

The application includes a sidebar for easy navigation between different analysis sections:

- **Portfolio**: Includes About, Education, Experience, Projects, and Contact sections.
- **Analyse Uber**: Includes various analyses such as Temporal, Spatial, and Base Analysis.
- **Analyse Tips**: Includes Tipping Behavior, Gender and Smoking Analysis, and Day and Time Analysis.
- **Joint Analysis**: Includes Temporal vs Tips Analysis and Spatial vs Tips Analysis.

### Interactive Visualizations

All visualizations are built with **Plotly**, which provides highly interactive plots where users can zoom, hover, and get details about specific data points.

## Improvements and Future Enhancements

- **Filtering Options**: Add filters to allow users to select specific subsets of data such as specific hours, days, or customer attributes.
- **More Data Integrations**: Add additional datasets, such as weather data or traffic data, to provide a richer context for Uber pickups and tipping behavior.
- **Predictive Analytics**: Use machine learning models to predict high or low tipping scenarios based on bill size, customer details, etc.

## Technologies Used

- **Python**: Programming language used to develop the application.
- **Streamlit**: Framework for building interactive web apps with Python.
- **Pandas**: Library for data manipulation and analysis.
- **Plotly**: Used for creating interactive and visually appealing visualizations.

## How to Run the Application

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run analysis_app.py
```

## Author

Developed by **Amine M'ZALI**. Feel free to reach out for any questions or suggestions regarding the application.

## License

This project is licensed under the MIT License.