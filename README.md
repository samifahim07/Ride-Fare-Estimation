# Ride Fare Estimation

Ride Fare Estimation is a Machine Learning project that predicts the estimated fare of a ride.

The project uses multiple Machine Learning regression models and selects the best-performing model for fare prediction.

A Flask web application is also created to make predictions through a simple and interactive user interface.

## Project Features

* Ride fare prediction
* Pickup and drop-off location input
* Passenger count input
* Date and time input
* Distance calculation
* Estimated trip time
* Estimated fare range
* Interactive map
* Machine Learning based prediction
* Flask web application

## Dataset

The dataset contains ride information and fare values.

The main features include:

* Pickup latitude
* Pickup longitude
* Drop-off latitude
* Drop-off longitude
* Passenger count
* Pickup date and time
* Fare amount

## Data Processing

The following steps were used in the project:

1. Load the dataset
2. Check the dataset shape
3. Check the columns
4. Check missing values
5. Check duplicate values
6. Process the date and time
7. Create new time-based features
8. Select the input features
9. Split the data into training and testing sets

### Time-Based Features

The following features were created from the pickup date and time:

* Hour
* Day
* Month
* Year
* Day of Week

## Machine Learning Models

Several regression models were tested:

* Decision Tree
* Random Forest
* AdaBoost
* Extra Trees
* Gradient Boosting
* XGBoost
* CatBoost

### Evaluation Metrics

The models were compared using:

* MSE
* RMSE
* MAE
* R² Score

## Model Performance

The final CatBoost model achieved:

| Metric    |  Score |
| --------- | -----: |
| Test R²   | 72.01% |
| Test RMSE |   5.46 |
| Test MAE  |   2.04 |
| Test MSE  |  29.76 |

CatBoost was selected as the final model used in the application.

## Final Model

The trained model is saved as:

```text
final_model_cat.pkl
```

## Project Screenshot

![Ride Fare Estimation](https://github.com/samifahim07/Ride-Fare-Estimation/blob/148b045037ccf1a7b10a9f44a6890a47258ce963/Capture.PNG)

## Technologies Used

* Python
* Pandas
* Scikit-learn
* XGBoost
* CatBoost
* Flask
* HTML
* CSS
* Machine Learning

## Project Structure

```text
Ride-Fare-Estimation/
│
├── main.py
├── final_model_cat.pkl
├── Capture.PNG
├── requirements.txt
└── README.md
```

## Conclusion

This project demonstrates how Machine Learning regression models can be used to estimate ride fares based on trip-related information such as location, passenger count, date, and time.

The final CatBoost model achieved a Test R² score of **72.01%** and was integrated into a Flask web application for practical use.
