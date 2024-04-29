*******AirBNB Price Prediction*******

Overview

This repository contains the code and data for the AirBNB Price Prediction project. We aim to predict AirBNB rental prices using machine learning techniques. The project utilizes datasets from Airbnb_Kaggle and Zillow websites, merging them for analysis and modeling.

Data Sources

Airbnb dataset: This dataset consists of various columns including id, log_price, property_type, room_type, amenities, accommodates, bathrooms, bed_type, cancellation_policy, cleaning_fee, city, description, first_review, host_has_profile_pic, host_identity_verified, host_response_rate, host_since, instant_bookable, last_review, latitude, longitude, name, neighbourhood, number_of_reviews, review_scores_rating, thumbnail_url, zipcode, bedrooms, and beds.
Zillow dataset: The Zillow dataset includes columns such as RegionID, SizeRank, zipcode, RegionType, StateName, State, City, Metro, CountyName, and monthly property values from 2000 to 2023.
Analysis

We have focused on the last three years' data (2021, 2022, and 2023) from both datasets. The main steps of our analysis include:

Data Cleaning and Preparation: We cleaned and preprocessed the datasets, handling missing values, and ensuring data consistency.
Feature Engineering: We performed feature engineering to extract relevant features for our predictive modeling.
Merging Datasets: The Airbnb and Zillow datasets were merged based on zip codes to enrich the feature set.
Exploratory Data Analysis: We conducted exploratory data analysis to understand the distributions, correlations, and patterns in the data.
Statistical Analysis: Calculated mean and median values based on zip codes to understand the average rental prices and property values.
ROI Analysis: Identified the best and least cities based on Return on Investment (ROI) using a combination of rental prices and property values.
Files

data/: Directory containing the raw datasets.


notebooks/: Jupyter notebooks containing data preprocessing, analysis, and modeling scripts.


Clone this repository: git clone https://github.com/ashishkesari18/AirBNB-Price-Prediction




Contributors:

Ashish Kesari
Sujith Cholleti
Harini Payala
Acknowledgments

We would like to thank Airbnb and Zillow for providing the datasets used in this project. Special thanks to the contributors and collaborators who helped in various aspects of this project.
