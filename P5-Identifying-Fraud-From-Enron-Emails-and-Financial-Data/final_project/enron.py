#!/usr/bin/python

import sys
import csv
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit

from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedShuffleSplit



def convert_csv(data_dict):
    with open('../data/data.csv', 'w') as csvfile:
        fieldnames = ['name'] + data_dict.itervalues().next().keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for value in data_dict:
            key = data_dict[value]
            key['name'] = value
            writer.writerow(key)


def remove_outliers(data_dict, indices):
    for index in indices:
        data_dict.pop(index, 0)


def get_k_best(data_dict, features_list, k):

    data = featureFormat(data_dict, features_list)
    labels_train, features_train = targetFeatureSplit(data)

    k_best = SelectKBest(f_classif, k=k)
    k_best.fit(features_train, labels_train)

    unsorted_list = zip(features_list[1:], k_best.scores_)
    sorted_list = sorted(unsorted_list, key=lambda x: x[1], reverse=True)
    k_best_features = dict(sorted_list[:k])

    return ['poi'] + k_best_features.keys()


def fraction_poi_communication(data_dict):
    features = ['to_messages', 'from_messages', 'from_this_person_to_poi', 'from_poi_to_this_person']

    for key in data_dict:
        name = data_dict[key]

        is_null = False
        for feature in features:
            if name[feature] == 'NaN':
                is_null = True

        if not is_null:
            name['fraction_poi_communication'] = float(name['from_this_person_to_poi'] + name['from_poi_to_this_person']) /\
                                                 (name['to_messages'] + name['from_messages'])
        else:
            name['fraction_poi_communication'] = 'NaN'


def total_wealth(data_dict):
    features = ['salary', 'bonus', 'total_stock_value', 'exercised_stock_options']

    for key in data_dict:
        name = data_dict[key]

        is_null = False
        for feature in features:
            if name[feature] == 'NaN':
                is_null = True

        if not is_null:
            name['total_wealth'] = name['salary'] + name['total_stock_value'] +\
                                    name['bonus'] + name['exercised_stock_options']
        else:
            name['total_wealth'] = 'NaN'



def get_best_parameters_reports(clf, parameters, features, labels):


    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.3, random_state=60)


    cv_strata = StratifiedShuffleSplit(labels_train, 100, test_size=0.2, random_state=60)

    grid_search = GridSearchCV(clf, parameters, n_jobs=-1, cv=cv_strata, scoring='f1')
    grid_search.fit(features_train, labels_train)

    '''
    prediction = grid_search.predict(features_test)
    print 'Precision:', precision_score(labels_test, prediction)
    print 'Recall:', recall_score(labels_test, prediction)
    print 'F1 Score:', f1_score(labels_test, prediction)
    '''

    print 'Best score: %0.3f' % grid_search.best_score_
    print 'Best parameters set:'
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print '\t%s: %r' % (param_name, best_parameters[param_name])

