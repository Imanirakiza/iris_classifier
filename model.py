{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4b2fa7bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import sklearn\n",
    "import csv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "86095e76",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read original dataset\n",
    "iris_df = pd.read_csv('iris.csv')\n",
    "# iris_df.sample(frac=1, random_state=seed)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2aedf373",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>SepalLengthCm</th>\n",
       "      <th>SepalWidthCm</th>\n",
       "      <th>PetalLengthCm</th>\n",
       "      <th>PetalWidthCm</th>\n",
       "      <th>Species</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species\n",
       "0   1            5.1           3.5            1.4           0.2  Iris-setosa\n",
       "1   2            4.9           3.0            1.4           0.2  Iris-setosa\n",
       "2   3            4.7           3.2            1.3           0.2  Iris-setosa\n",
       "3   4            4.6           3.1            1.5           0.2  Iris-setosa\n",
       "4   5            5.0           3.6            1.4           0.2  Iris-setosa"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "35a12c40",
   "metadata": {},
   "outputs": [],
   "source": [
    "# selecting features and target data\n",
    "X = iris_df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]\n",
    "y = iris_df[['Species']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "434d204f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# split data into train and test sets\n",
    "# 70% training and 30% test\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "a06b86e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "d2c858df",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "9a507fa1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Species</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>146</th>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>147</th>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148</th>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>150 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            Species\n",
       "0       Iris-setosa\n",
       "1       Iris-setosa\n",
       "2       Iris-setosa\n",
       "3       Iris-setosa\n",
       "4       Iris-setosa\n",
       "..              ...\n",
       "145  Iris-virginica\n",
       "146  Iris-virginica\n",
       "147  Iris-virginica\n",
       "148  Iris-virginica\n",
       "149  Iris-virginica\n",
       "\n",
       "[150 rows x 1 columns]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "c72f4b1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy:  {0.9111111111111111}\n"
     ]
    }
   ],
   "source": [
    "# create an instance of the random forest classifier\n",
    "clf = RandomForestClassifier(n_estimators=100)\n",
    "# train the classifier on the training data\n",
    "clf.fit(X_train, y_train.values.ravel())\n",
    "# ravel().clf.fit(X_train, y_train)\n",
    "# predict on the test set\n",
    "y_pred = clf.predict(X_test)\n",
    "# calculate accuracy\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(\"Accuracy: \",{accuracy}) # Accuracy: 0.9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c4af689d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "a1d3542c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['rf_model.sav']"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# save the model to disk\n",
    "joblib.dump(clf, \"rf_model.sav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a476a0e5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
