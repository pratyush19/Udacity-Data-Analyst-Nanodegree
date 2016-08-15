# Identifying Fraud From Enron Emails and Financial Data

**Pratyush Kumar**


##Project Overview
This project involves a real messy data so you have good knowledge of **Data Wrangling** and **Data Visualization** to clean and visualize the data, find correlation between various features and identify extreme outliers and finally using **Machine Learning** algorithm to predict **Person of Interest** 'POI'.

In 2000, Enron was one of the largest companies in the United States. By 2002, it had collapsed into bankruptcy due to widespread corporate fraud. In the resulting Federal investigation, a significant amount of typically confidential information entered into the public record, including tens of thousands of emails and detailed financial data for top executives. In this project, you will play detective, and put your new skills to use by building a person of interest identifier based on financial and email data made public as a result of the Enron scandal. To assist you in your detective work, we've combined this data with a hand-generated list of persons of interest in the fraud case, which means individuals who were indicted, reached a settlement or plea deal with the government, or testified in exchange for prosecution immunity.

##1. Dataset and Outliers
The dataset contains a total of **146 data points** with **21 features**, **18 POIs** and **128 Non POIs**.

After Exploratory Data Analysis, I found three 3 records need removal:

* ``TOTAL``: Contains extreme values for most numerical features.
* ```THE TRAVEL AGENCY IN THE PARK```: Not represent an individual
* ```LOCKHART EUGENE E```: Contains only NaN values.


Data before removal:

![](https://github.com/pratyush19/Udacity-Data-Analyst-Nanodegree/blob/master/P5-Identifying-Fraud-From-Enron-Emails-and-Financial-Data/image/enron.jpeg)

Data after removal: 

![](https://github.com/pratyush19/Udacity-Data-Analyst-Nanodegree/blob/master/P5-Identifying-Fraud-From-Enron-Emails-and-Financial-Data/image/enron_remove.jpeg) 

##2. Features Selection
Besides **21 features**, I have created **3 features** additionally by using existing features which I think should help to find more accurate results.

* ```fraction_poi_communication```: fraction of emails related to POIs
* ```total_wealth```: salary, bonus, total stock value, exercised stock options.

Using ```SelectKBest```, below are the top 10 features of the dataset:

| Features                      | Scores   | 
| ----------------------------- |:--------:| 
| Exercised Stock Options       | 24.815   | 
| Total Stock Value             | 24.183   |  
| Bonus                         | 20.792   |
| Salary							  | 18.289   |
| Total Wealth 					  | 15.369   |
| Deferred Income				  | 11.458   |
| Long Term Incentive           | 9.922    |
| Restricted Stock				  | 9.213    |
| Total Payments				  	  | 8.772    |
| Shared Receipt with POI       | 8.589    |

##3. Parameters Tuning
Tuning the parameters of an algorithm involves changing the algorithm input parameters to a set of range and measuring the performances of each combinations in order to determine the optimal input parameters. Parameters tuning greatly helps to improve the performance of any algorithm.

For each algorithms, a number of operation applied at once using ```Pipeline``` function, where parameters tuning is done using ```GridSearchCV``` and ```StratifiedShuffleSplit```.

Following parameters are used to tune an algorithm:

* Select K Best (```SeleckKBest```) : ```k```
* Principal Components Analysis (```PCA```) : ```n_components```, ```whiten```
* Gaussian Naive Bayes (```GaussianNB```) : None
* Logistic Regression (```LogisticRegression```) : ```C```, ```tol```, ```penalty```,  ```random_state```
* Support Vector Classifier(```SVC```) : ```C```, ```gamma```, ```kernel```
* Decision Tree(```DecisionTreeClassifier```) : ```min_samples_split```, ```min_samples_leaf```, ```criterion```, ```max_depth```, ```random_state```.
* Random Forest (```RandomForestClassifier```) : ```n_estimators```, ```max_depth```, ```random_state```
* Ada Boost (```AdaBoostClassifier```) : ```n_estimators```, ```algorithm```, ```learning_rate```

##4. Validation
Validation is performed to ensure that a machine learning algorithm generalizes well, and to prevent overfitting. Overfitting occurs when an algorithm perform very well on the training data, but failed to perform on the testing (or, unseen) data. Therefore, it is important to split the dataset into training and testing set.
In Scikit-Learn, training and testing data are created using ```StratifiedShuffleSplit```, which shuffled the data and split into K different set, called folds. In this dataset, I split the data into **100 folds**.



##5. Algorithm Selection

I performed 6 different algorithms using ```scikit-learn``` and tune the parameters using ```GridSearchCV```.
Below are the optimal parameters value achieved after performing the parameters tuning for each of the algorithms.

###Gaussian Naive Bayes

```python
clf = GaussianNB()
```

###Logistic Regression

```python
number_of_best_features = 9

clf = Pipeline(steps=[
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=4, whiten=False)),
        ('classifier', LogisticRegression(tol=0.01, C=1e-08, penalty='l2', random_state=42))])
```

###Support Vector Machine

```python
number_of_best_features = 8

clf = Pipeline(steps=[
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=6, whiten=True)),
        ('classifier', SVC(C=1000, gamma=.001, kernel='rbf'))])
```

###Decision Tree

```python
number_of_best_features = 9

clf = Pipeline(steps=[
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=5, whiten=True)),
        ('classifier', DecisionTreeClassifier(criterion='entropy',
                                              min_samples_leaf=2,
                                              min_samples_split=2,
                                              random_state=46,
                                              max_depth=None))                                          
```
 
###Random Forest

```python
number_of_best_features = 9

clf = Pipeline(steps=[
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(max_depth=5,
                                              n_estimators=25,
                                              random_state=42))
```

###Ada Boost

```python
number_of_best_features = 9

clf = Pipeline(steps=[
        ('scaler', StandardScaler()),
        ('classifier', AdaBoostClassifier(learning_rate=1.5,
                                          n_estimators=30,
                                          algorithm='SAMME.R'))
    ])
```
The use PCA worsen the performance of **Random Forest** and **Ada Boost**, so I discarded PCA for these algorithms in my final evaluation.
Out of all the algorithms, **Logistic Regression** gives overall best performance using evaluation matrices which is discussed below.


##6. Evaluation Metrics

I have used three evaluation matrices **Precision**, **Recall** and **F1-score**. Theses matrices are based on comparing the predicted values to actual ones.

**Precision :** Out of all items that are truly positive, how many are correctly classified as positive. It is calculated as ```(True Positive)/(True Postive + False Positive)```

**Recall :** Out of all items are predicted as positive, how many are truly belong to positive case. It is calculated as ```(True Positive)/(True Postive + False Negative)```

**F1-score :** It is a harmonic mean of recall and precision. It is calculated as ```(2*recall*precision)/(recall + precision)```

The precision, recall and f1-score for each algorithms are given below:

| Algorithm                     | Precision   | Recall    | F1-score  | 
| ----------------------------- |:-----------:| :--------:| :--------:|
| Logistic Regression           | 0.437       | 0.449     | 0.443     |
| Gaussian Naive Bayes          | 0.392       | 0.331     | 0.359     | 
| Random Forest 					  | 0.461       | 0.192     | 0.271     |
| Ada Boost      				  | 0.316       | 0.230     | 0.266     |
| Support Vector Machine        | 0.490       | 0.151     | 0.230     |
| Decision Tree  				  | 0.194       | 0.160     | 0.176     |


Therefore, **Logisitic Regression** gives overall best scores for the evaluation matrices, followed by **Gaussian NB**, **Random Forest**, **AdaBoost**, **Support Vector** and **Decision Tree**.


                                         
                                              
                                              
                                              
                                              
                                              
                                              
                                              
                                            

