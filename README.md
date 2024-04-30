*******AirBNB Price Prediction*******

Overview

This repository contains the code and data for the AirBNB Price Prediction project including the Visualizations and results.

We aim to predict AirBNB rental prices using machine learning techniques. The project also utilizes AirBNB dataset from Kaggle and Zillow dataset from Zillow website, merging them for analysis and modeling.

Data Sources

Airbnb dataset: This dataset consists of various columns including id, log_price, property_type, room_type, amenities, accommodates, bathrooms, bed_type, cancellation_policy, cleaning_fee, city, description, first_review, host_has_profile_pic, host_identity_verified, host_response_rate, host_since, instant_bookable, last_review, latitude, longitude, name, neighbourhood, number_of_reviews, review_scores_rating, thumbnail_url, zipcode, bedrooms, and beds.


Zillow dataset: The Zillow dataset includes columns such as RegionID, SizeRank, zipcode, RegionType, StateName, State, City, Metro, CountyName, and monthly property values from 2000 to 2023.
Analysis

We have focused on the last three years' data (2021, 2022, and 2023). 

The main steps of our analysis include:

Step-1: Data Cleaning aEDAnd Preparation: We cleaned and preprocessed the datasets, handling missing values, and ensuring data consistency.

Step-2: Exploratory Data Analysis: We conducted exploratory data analysis to understand the distributions, correlations, and patterns in the data.

Step-3: Merging Datasets: The Airbnb and Zillow datasets were merged based on zip codes to enrich the feature set.

Step-4:  Calculated mean and median values based on zip codes to understand the average rental prices and property values.

Step-5: ROI Analysis: Identified the best and least cities based on Return on Investment (ROI) using a combination of rental prices and property values.

Step-6: Feature Engineering: We performed feature engineering to extract relevant features for our predictive modeling.

Step-7: Machine Learning Analysis: Our Machine Learning Analysis is only done for AirBNB Dataset as our primary aim is to predict teh Proce for rental dataset, but  Obtained good amount of inisghts from Combined dataset. 

       * For Machine Learning Analysis, The target variable here is log_price and has various features and performed Machine Learning Analysis on AirBNB Dataset 
       * Performed various machine Learning techniques like :  Linear Regression, Random Forest,Gradient Boosting, XGBoost.
       * Achieved good R^2 Values :






data/: Directory containing the raw datasets.


notebooks/: Jupyter notebooks containing data preprocessing, analysis, and modeling parts.


Clone this repository: git clone https://github.com/ashishkesari18/AirBNB-Price-Prediction




Contributors:

Ashish Kesari
Sujith Cholleti
Harini Payala
