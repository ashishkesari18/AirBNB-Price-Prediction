  ![Designer-3](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/209e2aaa-0806-4229-91f5-37ea84acbdbf)


                                          

#                                                   AirBNB Price Prediction
Overview

This repository contains the code and data for the AirBNB Price Prediction project including the Visualizations and results.

We aim to predict AirBNB rental prices using machine learning techniques. The project also utilizes AirBNB dataset from Kaggle and Zillow dataset from Zillow website, merging them for analysis and modeling.

Data Sources

Airbnb dataset: This dataset consists of various columns including id, log_price, property_type, room_type, amenities, accommodates, bathrooms, bed_type, cancellation_policy, cleaning_fee, city, description, first_review, host_has_profile_pic, host_identity_verified, host_response_rate, host_since, instant_bookable, last_review, latitude, longitude, name, neighbourhood, number_of_reviews, review_scores_rating, thumbnail_url, zipcode, bedrooms, and beds.

![2](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/16969b7c-e5a8-47c6-9b56-19d60e9e8398)


Zillow dataset: The Zillow dataset includes columns such as RegionID, SizeRank, zipcode, RegionType, StateName, State, City, Metro, CountyName, and monthly property values from 2000 to 2023.
Analysis

We have focused on the last three years' data (2021, 2022, and 2023). 

the project architecture is as follows:

![1](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/bf61cdd8-ba85-4f54-82a6-56a1c5ad4ef4)


The main steps of our analysis include:

![data-cleaning-in-flat-outline-icon-editable-vector](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/8334a5fa-387f-4fa2-acee-28032f5c43ae)

Step-1: Data Cleaning And Preparation: We cleaned and preprocessed the datasets, handling missing values, and ensuring data consistency.

![Exploratory-Data-Analysis](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/a0a4ca35-b5ad-4859-8979-699073f19ecb)

Step-2: Exploratory Data Analysis: We conducted exploratory data analysis to understand the distributions, correlations, and patterns in the data.

![image-3](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/da5a8668-50e3-4c3f-bccb-3b3fdfdc4fc6)

![image-4](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/932a2cce-2034-4dce-a91a-48e1828eeffe)


Step-3: Merging Datasets: The Airbnb and Zillow datasets were merged based on zip codes to enrich the feature set.

Step-4:  Calculated mean and median values based on zip codes to understand the average rental prices and property values.

Step-5: ROI Analysis: Identified the best and least cities based on Return on Investment (ROI) using a combination of rental prices and property values.

![roi1](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/f2cf2cba-1f4a-44ac-829c-fdf7bb0c396f)

![roi2](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/6f930673-aa09-4894-a41c-c342e837674e)

Step-6: Feature Engineering: We performed feature engineering to extract relevant features for our predictive modeling.

![image](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/4200776b-19d4-429a-803b-984ca67d47c2)


These are the top features that we are going to use for Predicting and modeling.

Step-7: Machine Learning Analysis: Our Machine Learning Analysis is only done for AirBNB Dataset as our primary aim is to predict the Price for rental dataset, but  Obtained good amount of inisghts from Combined dataset. 

       * For Machine Learning Analysis, The target variable here is log_price and has various features and performed Machine Learning Analysis on AirBNB Dataset 
       * Performed various machine Learning techniques like :  Linear Regression, Random Forest,Gradient Boosting, XGBoost.


![image-5](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/6c3904ba-64cd-4924-85c5-beba11f7ad6c)

![image-6](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/22da123c-07cf-4521-96d6-4271f175b168)

![image-7](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/3fbf82d8-7037-46a4-9b54-44d0db3e0bf0)

![image-8](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/0a9c6474-2632-49e4-98c9-3fd9a70bad52)

       
       * Achieved good R^2 Values :
             - Linear Regression  : 0.51
             - Random Forest      : 0.65
             - Gradient Boosting  : 0.64
             - XG Boost           : 0.66

![comp](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/96d84581-d296-49db-bda4-842a97b83d22)

![comp2](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/35c20aba-0e0b-4e69-882a-cee1cea59b34)


![streamlit](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/c41b9640-86a0-467e-9a74-d6c911d22936)

Step-8 : We have selected our final model as XGboost and then later on using streamlit we have Created UI using the Top features for Price Prediction.

![image-9](https://github.com/ashishkesari18/AirBNB-Price-Prediction/assets/88103934/95dbf67a-168e-4207-9753-834d8d0d0888)


Datasets/: Directory containing the raw datasets.

           * train.csv - refers to AirBNB Dataset
           * zillowhouses.csv- refers to zillow Housing dataset.
images/: Contains images used for ReadMe file.
      
Phase-2: Directory which has teh Jupyter Notebook file that contains the work done till Phase-2.

Phase-3: Directory which has a Jupyter Notebook file which was uploaded with few changes which were made to Phase-2.

            * xgboost.pkl is the pickle file fir the XG Boost model
            
            * main.py is the python file where we have used streamlit library for Price Prediction.
            

Clone this repository: git clone https://github.com/ashishkesari18/AirBNB-Price-Prediction




Contributors:

Ashish Kesari

Sujith Cholleti

Harini Payala
