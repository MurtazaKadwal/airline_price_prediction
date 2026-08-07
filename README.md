# ✈️ AirFare AI --- Airline Ticket Price Prediction

AirFare AI is a machine learning project that predicts the estimated
price of an airline ticket based on flight-related information such as
airline, route, departure time, number of stops, class, flight duration,
and the number of days remaining before departure.

The trained model is integrated into a modern Streamlit web application
where users can enter flight details and receive an estimated ticket
price.

------------------------------------------------------------------------

## 🚀 Project Overview

Airline ticket prices can vary significantly depending on several
factors. This project uses machine learning to learn the relationship
between flight attributes and ticket prices.

### 🎯 Objective

The primary objective is to build a regression model that predicts:

> **Target Variable: `price`**

The final model is deployed through Streamlit to provide an interactive
price-prediction experience.

------------------------------------------------------------------------

## 🧠 Machine Learning Approach

This project follows a standard supervised machine learning workflow:

1.  Load and inspect the dataset
2.  Perform data preprocessing
3.  Analyze relationships between features and ticket price
4.  Handle categorical variables using One-Hot Encoding
5.  Scale numerical features
6.  Split the dataset into training and testing sets
7.  Train regression models
8.  Evaluate model performance using regression metrics
9.  Save the trained model and preprocessing objects using Joblib
10. Build a Streamlit application for deployment

------------------------------------------------------------------------

## 📊 Dataset Features

The dataset contains the following features:

  Feature              Description
  -------------------- -------------------------------------------
  `airline`            Airline operating the flight
  `source_city`        City from which the flight departs
  `departure_time`     Departure time category
  `stops`              Number of stops during the journey
  `arrival_time`       Arrival time category
  `destination_city`   Destination city
  `class`              Travel class
  `duration`           Flight duration in hours
  `days_left`          Number of days remaining before departure
  `price`              Airline ticket price --- target variable

------------------------------------------------------------------------

## 🔎 Feature Engineering

### Categorical Features

The categorical variables are converted into numerical representations
using **One-Hot Encoding**.

The following columns are treated as categorical:

``` text
airline
source_city
departure_time
stops
arrival_time
destination_city
class
```

`drop_first=True` is used during encoding to avoid redundant dummy
variables.

### Numerical Features

The numerical variables used by the model are:

``` text
duration
days_left
```

These features are scaled using the saved scaler before making
predictions.

------------------------------------------------------------------------

## 🤖 Model

The final application uses:

### Linear Regression

Linear Regression is used as the prediction model because this is a
supervised regression problem where the target variable, `price`, is
continuous.

The model achieved an **R² score of approximately 0.91 during model
evaluation**, indicating that it explains a large proportion of the
variation in ticket prices on the evaluated data.

> Note: The reported R² score is based on the project's model evaluation
> and should not be interpreted as a guarantee of real-world prediction
> accuracy.

------------------------------------------------------------------------

## 📈 Model Evaluation

The primary evaluation metric used during the project is:

### R² Score

R² (Coefficient of Determination) measures how much of the variation in
the target variable can be explained by the model.

A value closer to `1.0` generally indicates stronger explanatory
performance on the evaluation data.

The project achieved approximately:

``` text
R² Score ≈ 0.91
```

------------------------------------------------------------------------

## 📦 Saved Model Files

The Streamlit application uses three Joblib files.

``` text
linear_regression_model.pkl
scaler.pkl
feature_columns.pkl
```

### 1. `linear_regression_model.pkl`

Contains the trained Linear Regression model used to generate ticket
price predictions.

### 2. `scaler.pkl`

Contains the fitted scaler used to transform:

``` text
duration
days_left
```

The same fitted scaler must be used during inference as was used during
model training.

### 3. `feature_columns.pkl`

Contains the exact feature names and order expected by the trained
model.

This is important because the model was trained using One-Hot Encoded
features.

------------------------------------------------------------------------

## 🔄 Prediction Pipeline

When a user enters flight information into the Streamlit application,
the following process occurs:

``` text
User Input
    ↓
Create DataFrame
    ↓
One-Hot Encoding
    ↓
Match Training Feature Columns
    ↓
Scale duration & days_left
    ↓
Linear Regression Model
    ↓
Predicted Ticket Price
```

The input data is reindexed using the saved `feature_columns.pkl` file
so that the prediction input has the same feature structure as the
training data.

------------------------------------------------------------------------

## 🖥️ Streamlit Application

The project includes a modern Streamlit interface called **AirFare AI**.

### User Inputs

The application allows users to enter:

-   Airline
-   Source City
-   Destination City
-   Departure Time
-   Arrival Time
-   Number of Stops
-   Travel Class
-   Flight Duration
-   Days Left Before Departure

After clicking:

> **✈️ Predict Ticket Price**

the application displays the estimated ticket price.

------------------------------------------------------------------------

## 🎨 UI/UX

The application uses a modern dark-themed interface with:

-   Gradient backgrounds
-   Airline-themed visual elements
-   Responsive layout
-   Modern input components
-   Prediction result card
-   Flight summary cards
-   Responsive mobile styling
-   Clear visual hierarchy

The prediction result is presented in Indian Rupees:

``` text
₹36,201
```

for example, depending on the entered flight information and model
prediction.

------------------------------------------------------------------------

## 📁 Project Structure

``` text
airfare-ai/
│
├── app.py
├── linear_regression_model.pkl
├── scaler.pkl
├── feature_columns.pkl
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd airfare-ai
```

### 2. Create a virtual environment

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 📋 Requirements

The application requires:

``` text
streamlit
pandas
numpy
scikit-learn==1.5.1
joblib
```

The scikit-learn version is pinned to `1.5.1` to maintain compatibility
with the serialized model and preprocessing objects used in the project.

------------------------------------------------------------------------

## ▶️ Run the Application

Start the Streamlit application using:

``` bash
streamlit run app.py
```

The application will open in your browser.

------------------------------------------------------------------------

## 🧪 Example Prediction

Example input:

``` text
Airline: SpiceJet
Source City: Delhi
Destination City: Mumbai
Departure Time: Evening
Arrival Time: Night
Stops: zero
Class: Economy
Duration: 2.17 hours
Days Left: 1
```

The model will process these values and return an estimated ticket
price.

> The prediction will vary depending on the exact trained model and
> input values.

------------------------------------------------------------------------

## 🔐 Important Deployment Notes

The following files are required for the application to work:

``` text
linear_regression_model.pkl
scaler.pkl
feature_columns.pkl
```

They must be located in the same directory as `app.py`, unless their
paths are changed in the application.

Do not retrain or refit the scaler inside the Streamlit application. The
application should use the scaler that was fitted during training.

Similarly, the application should use the saved feature-column list to
ensure the inference data matches the model's training structure.

------------------------------------------------------------------------

## 🌐 Deployment

The Streamlit application can be deployed to a cloud hosting platform
that supports Streamlit applications.

Before deployment, make sure the repository contains:

``` text
app.py
linear_regression_model.pkl
scaler.pkl
feature_columns.pkl
requirements.txt
README.md
```

The dependency versions should be compatible with the serialized model.

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Python**
-   **Pandas**
-   **NumPy**
-   **Scikit-learn**
-   **Joblib**
-   **Streamlit**
-   **Jupyter Notebook**

------------------------------------------------------------------------

## 💡 Key Learning Outcomes

This project demonstrates practical understanding of:

-   Regression-based machine learning
-   Categorical feature preprocessing
-   One-Hot Encoding
-   Feature scaling
-   Train/test model development
-   R²-based model evaluation
-   Model serialization using Joblib
-   Consistent preprocessing during inference
-   Streamlit model deployment
-   Building a modern ML application UI

------------------------------------------------------------------------

## 🔮 Future Improvements

Potential improvements for future versions include:

-   Compare multiple regression algorithms
-   Hyperparameter tuning
-   Cross-validation
-   Feature importance and model explainability
-   Confidence or prediction intervals
-   Better handling of unusual/extreme ticket prices
-   Automated preprocessing pipelines using `Pipeline` and
    `ColumnTransformer`
-   More advanced models such as Random Forest or Gradient Boosting
-   Add historical price visualization
-   Add downloadable prediction reports
-   Deploy the application publicly

------------------------------------------------------------------------

## ⚠️ Disclaimer

This application provides an **estimated airline ticket price** based on
the patterns learned by the trained machine learning model.

The prediction should not be considered an actual airline fare or a
guaranteed booking price. Real-world ticket prices can change due to
availability, demand, booking platforms, promotions, taxes, and other
factors not necessarily represented in the dataset.

------------------------------------------------------------------------

## 👨‍💻 Project

**AirFare AI --- Airline Ticket Price Prediction**

Built as a machine learning regression and deployment project using
Python, Scikit-learn, Joblib, and Streamlit.

------------------------------------------------------------------------

## ⭐ If You Like This Project

If this project helped you understand machine learning model deployment,
consider giving the repository a ⭐ on GitHub.
