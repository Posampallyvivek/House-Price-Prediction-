# House Price Prediction
 House price prediction is a common task in machine learning where the goal is to develop a model that can predict the price of a house based on various features. The provided code is a simplified example of building and evaluating such a predictive model.
# Stages For House Price Prediction
# Data Loading:

The code starts by loading a dataset from a CSV file into a Pandas DataFrame (data). This dataset likely contains information about different houses, such as the number of bedrooms, size, and price.
# Data Exploration and Cleaning:

The initial exploration involves checking the first few rows, the shape, and general information about the dataset. This step helps understand the structure of the data.
Missing values are checked, and specific columns ('lot_size' and 'lot_size_units') are dropped, indicating a basic form of data cleaning.
# Feature Engineering:

A new feature, 'price_per_sqft,' is created by dividing the 'price' by the 'size' of the house. This additional feature could potentially help the model learn more about the relationship between size and price.
# Data Preparation:

The 'size_units' column is dropped, and the modified dataset is saved to a new CSV file ('final_dataset.csv'). This step is part of preparing the data for training the machine learning models.
# Model Training and Evaluation:

The dataset is split into features (X, representing input variables) and the target variable (y, representing house prices). The data is further split into training and testing sets using the train_test_split function.
A linear regression model is trained on the training set. The features undergo one-hot encoding for the 'beds' column and standard scaling. The model is then evaluated on the test set using the R-squared metric.
# Regularization Models (Lasso and Ridge):

Lasso and Ridge regression models are introduced as regularization techniques. These models help prevent overfitting by adding penalty terms to the linear regression model's coefficients. They are trained and evaluated similarly to the linear regression model.
# Model Comparison:

The R-squared scores of the linear regression model with no regularization, Lasso, and Ridge are printed and compared. The R-squared score is a metric that measures the proportion of the variance in the dependent variable (house prices) that is predictable from the independent variables.
