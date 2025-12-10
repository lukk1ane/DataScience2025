from sklearn.linear_model import Lasso
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures

# task 1
np.random.seed(42)

n = 500

square_feet = np.random.randint(300, 2000, n)
bedrooms = np.random.randint(1, 5, n)
age_years = np.random.randint(0, 40, n)

rent_price = (
    square_feet * 1.8 + bedrooms * 150 + age_years * (-20) + np.random.normal(0, 200, n)
)

df = pd.DataFrame(
    {
        "square_feet": square_feet,
        "bedrooms": bedrooms,
        "age_years": age_years,
        "rent_price": rent_price,
    }
)


X = df[["square_feet", "bedrooms", "age_years"]]
y = df["rent_price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)  # R squared, r is the coefficient of determination
mae = mean_absolute_error(y_test, y_pred)  # Mean Absolute Error
mse = mean_squared_error(y_test, y_pred)  # Mean Squared Error
rmse = np.sqrt(mse)  # Root Mean Squared Error

print(r2)
print(mae)
print(mse)
print(rmse)

# task 2

square_feet = np.random.randint(500, 5000, n)
lot_size_acres = np.random.uniform(0.1, 2.5, n)
num_bedrooms = np.random.randint(1, 6, n)
distance_to_downtown_km = np.random.uniform(0.5, 45, n)

# used ai for realistic formula, i don't know real house prices
price = (
    150 * square_feet
    + 30000 * lot_size_acres
    + 20000 * num_bedrooms
    - 1200 * distance_to_downtown_km
    + np.random.normal(0, 50000, n)
)

df = pd.DataFrame(
    {
        "square_feet": square_feet,
        "lot_size_acres": lot_size_acres,
        "num_bedrooms": num_bedrooms,
        "distance_to_downtown_km": distance_to_downtown_km,
        "price": price,
    }
)

X = df[["square_feet", "lot_size_acres", "num_bedrooms", "distance_to_downtown_km"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model_no_scaling = LinearRegression()
model_no_scaling.fit(X_train, y_train)

y_pred_no = model_no_scaling.predict(X_test)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_scaled = LinearRegression()
model_scaled.fit(X_train_scaled, y_train)

y_pred_scaled = model_scaled.predict(X_test_scaled)
print("  ")
print("without scaling")
print(model_no_scaling.coef_)
print(model_no_scaling.intercept_)
print("  ")
print("with scaling")
print(model_scaled.coef_)
print(model_scaled.intercept_)

# task 3


square_feet = np.random.randint(500, 5000, n)
bedrooms = np.random.randint(1, 6, n)
age = np.random.randint(0, 80, n)
distance = np.random.uniform(0.5, 40, n)
neighborhood = np.random.choice(["A", "B", "C"], n)

price = (
    180 * square_feet
    + 25000 * bedrooms
    - 800 * age
    - 1500 * distance
    + (neighborhood == "A") * 80000
    + (neighborhood == "B") * 40000
    + np.random.normal(0, 40000, n)
)

df = pd.DataFrame(
    {
        "square_feet": square_feet,
        "bedrooms": bedrooms,
        "age": age,
        "distance": distance,
        "neighborhood": neighborhood,
        "price": price,
    }
)

X = df.drop("price", axis=1)
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# A
A = LinearRegression().fit(X_train[["square_feet"]], y_train)
predA_train, predA_test = A.predict(X_train[["square_feet"]]), A.predict(
    X_test[["square_feet"]]
)


# B
df2 = pd.get_dummies(df, columns=["neighborhood"], drop_first=True)

X = df2.drop("price", axis=1)
y = df2["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

B = LinearRegression().fit(X_train, y_train)

pred_train_B = B.predict(X_train)
pred_test_B = B.predict(X_test)

# C
C = Pipeline(
    [
        ("poly", PolynomialFeatures(degree=3, include_bias=False)),
        ("model", LinearRegression()),
    ]
).fit(X_train, y_train)

predC_train = C.predict(X_train)
predC_test = C.predict(X_test)

models = {"A": A, "B": B, "C": C}
for name, model in models.items():
    if name == "A":
        y_pred_train, y_pred_test = predA_train, predA_test
    elif name == "B":
        y_pred_train, y_pred_test = pred_train_B, pred_test_B
    else:
        y_pred_train, y_pred_test = predC_train, predC_test

    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)

    print(f"Model {name}(R2 Train: {r2_train:.4f}, R2 Test: {r2_test:.4f})")


# task 3.2

df3_2 = pd.get_dummies(df, columns=["neighborhood"], drop_first=True)

kf = KFold(n_splits=5, shuffle=True, random_state=42)

# B
model_b = LinearRegression()
scores_b = cross_val_score(model_b, X, y, cv=kf, scoring="r2")
print("model b", scores_b)


model_c = Pipeline(
    [
        ("poly", PolynomialFeatures(degree=3, include_bias=False)),
        ("lr", LinearRegression()),
    ]
)
scores_c = cross_val_score(model_c, X, y, cv=kf, scoring="r2")

print("model c", scores_c)

model_lasso = Lasso(alpha=0.1, max_iter=10000)
scores_lasso = cross_val_score(model_lasso, X, y, cv=kf, scoring="r2")
print("model lasso", scores_lasso)


# 1
# Because it tests the model on multiple splits instead of just one, reducing the
# chance of getting a lucky or unlucky train-test split.

# 2
# It means Model C is unstable and its performance varies a lot. I would choose a
# more consistent model (Model B or Lasso) for production.

# 3
# No. The test set is just one split, so its score can differ. Noise, randomness,
# and a harder test set can make the final R² lower than the CV mean.

# 4
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(LinearRegression(), X, y, cv=kf, scoring="r2")
print(scores)

# 3.3

# 1
# R squared 0.80 means the model explains 80 percent of the changes in house prices.
# The predictions follow the real prices well.
# I cannot say it is good enough without more information.
# I need to know how much error the business can accept.
# I also need to know how important price precision is for company decisions.


# 2
# RMSE 45000 means the model is wrong by about 45000 dollars on average.
# This is about a 13 percent error for a 350000 dollar house.
# This may be fine for rough estimates.
# This may not be fine for exact pricing.
# Acceptable error depends on business needs.

# 3
# The housing market may have changed so the model no longer fits the new data.
# New data may be lower quality and this can hurt accuracy.
# The model may be outdated because it was not retrained.
