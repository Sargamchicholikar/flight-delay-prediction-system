# Flight Delay Prediction System

![Flight Delay Banner](https://img.shields.io/badge/Project-Flight%20Delay%20Prediction-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)
![Year](https://img.shields.io/badge/Year-2025--26-orange)

> A Big Data Analysis project developed as a part of Bachelor of Technology in Computer Engineering at Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Models](#models)
- [Web Interface](#web-interface)
- [Results](#results)
- [Future Scope](#future-scope)
- [Technologies Used](#technologies-used)
- [Team Members](#team-members)
- [Acknowledgements](#acknowledgements)

## 🔭 Overview

The Flight Delay Prediction System is a comprehensive solution designed to analyze and predict flight arrival delays using historical flight data from New York City airports. In the aviation industry, flight delays cause significant operational and economic challenges, affecting airlines and passengers alike. This project leverages Big Data Analytics and machine learning techniques to uncover hidden patterns within flight data and build predictive models that can forecast potential delays.

The project aims to:
- Identify key factors contributing to flight delays
- Understand the impact of variables like time of day, carrier type, and airport traffic on arrival times
- Develop accurate predictive models for flight delay estimation
- Provide a user-friendly web interface for delay predictions

## ✨ Features

- **Data Analysis**: Comprehensive analysis of flight data from NYC airports
- **Predictive Modeling**: Machine learning models to predict arrival delays
- **Feature Importance**: Identification of key factors influencing flight delays
- **User Interface**: Web-based interface for real-time delay predictions
- **Visual Analytics**: Interactive visualizations of delay patterns and trends
- **Model Comparison**: Performance evaluation of different prediction algorithms

## 📂 Project Structure

The project is organized into the following key phases:

1. **Data Collection**: Acquisition of the NYC Flight Delay dataset from Kaggle
2. **Data Preprocessing**: Cleaning, transformation, and preparation of the dataset
3. **Exploratory Data Analysis (EDA)**: Visual and statistical analysis to uncover patterns
4. **Modeling**: Development of predictive models using various ML algorithms
5. **Evaluation**: Assessment of model performance using multiple metrics
6. **Web Implementation**: Creation of a Flask-based web interface for model testing

## 📊 Dataset

The project uses a comprehensive dataset of flight operations from New York City airports (JFK, LaGuardia, and Newark) obtained from Kaggle. Key attributes include:

- Scheduled and actual departure/arrival times
- Delay durations (departure and arrival)
- Airline carrier information
- Origin and destination airports
- Flight distances and routes
- Time-related features (hour, minute, day, month)

## 🔬 Methodology

### Data Preprocessing
- Handling missing values in critical fields
- Encoding categorical variables (airline names, airport codes)
- Feature scaling using StandardScaler for normalization
- Removal of inconsistent or impossible values

### Feature Engineering
- Time-based feature extraction (hour, day_of_week, month)
- Combining correlated features
- Invalid record handling
- Creating derived features to enhance model performance

### Exploratory Data Analysis
- Delay distribution visualization
- Carrier-wise delay analysis
- Airport and route trend identification
- Correlation analysis between features
- High-traffic period pattern detection

## 🧠 Models

Three supervised learning algorithms were implemented for this regression task:

1. **Linear Regression (Baseline Model)**
   - Establishes basic patterns in the data
   - Serves as a comparison benchmark for more complex models

2. **Decision Tree Regressor**
   - Captures non-linear interactions between features
   - Provides interpretability through feature importance ranking

3. **Random Forest Regressor**
   - Ensemble model that reduces overfitting
   - Offers highest accuracy among implemented models
   - Successfully captures complex delay dynamics

### Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score (Coefficient of Determination)

## 🖥️ Web Interface

The project includes a web-based interface built with Flask, HTML, and CSS that allows users to:

- Input flight details (carrier, origin, destination, scheduled times)
- Get real-time delay predictions
- View prediction confidence and explanation
- Explore key factors affecting the prediction

The interface is designed to be user-friendly and accessible, making the predictive model's capabilities available to all stakeholders.

## 📈 Results

The project successfully developed predictive models with the following insights:

- Strong positive correlation between departure and arrival delays
- Higher delays during late afternoon and evening hours
- Mondays and Fridays identified as high-delay days
- Variations in performance across different carriers and routes
- Random Forest Regressor emerged as the best-performing model

## 🚀 Future Scope

Future enhancements for the project include:

- **Integrating Weather and Air Traffic Data**: Incorporating real-time weather conditions and air traffic patterns to improve prediction accuracy
- **Deploying as a Web Service**: Making the predictive insights accessible through a dedicated web service for real-time updates
- **Implementing Time Series Forecasting**: Applying time series methods to predict delays based on historical trends over specific periods
- **Mobile Application Development**: Creating a mobile app for passenger convenience
- **Integration with Airline Systems**: Developing APIs to integrate with airline management systems

## 💻 Technologies Used

- **Python**: Core programming language
- **Pandas & NumPy**: Data manipulation and processing
- **Scikit-learn**: Machine learning model implementation
- **Matplotlib & Seaborn**: Data visualization
- **Flask**: Web framework for the user interface
- **HTML & CSS**: Frontend development
- **Jupyter Notebooks**: Exploratory analysis and model development

## 👥 Team Members

- **Sargam Chicholikar** (2214110137-59)

## 🙏 Acknowledgements

- **Dr. Sunita Dhotre** - Course Coordinator
- **Dr. S. Vanjale** - HOD, Computer Engineering Department
- Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune

---

© 2025-26 | Department of Computer Engineering | Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune-43