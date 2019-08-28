from datetime import datetime
import csv

from surprise import BaselineOnly
from surprise import SVDpp, SVD, SlopeOne, KNNBaseline,NormalPredictor, BaselineOnly, \
                     KNNBasic, KNNBasic, KNNWithMeans, NMF, CoClustering
from surprise import Dataset
from surprise import Reader
from collections import defaultdict
import os
import pandas as pd


#--------------------- Append new user to csv file (data) --------------------------
def add_to_csv(auth_user):
    fields = []
    
    # get user rating from database
    user_rating = user_rate.objects.filter(user_id = auth_user)
    
    # prepare the fields    
    for field in user_rating:
        obj = []
        user_id = str(field.user_id.id)
        obj.append(user_id)
        obj.append(str(field.id))
        obj.append(str(field.country_rating*20))
        obj.append(str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        fields.append(obj)
        
    # append new user to csv file
    with open(r'static/CRdata.csv', 'a') as f:
        for user_obj in fields:
            writer = csv.writer(f)
            writer.writerow(user_obj)
    
    # test if well appended
    nok = '---------> not appended'
    with open(r'static/CRdata.csv', 'r') as f:    
        if (list(csv.reader(f))[-1][0]) == user_id :
            return  user_id
        else:
            return nok 
    
    
def get_top_n_for_user_all_algo(target_user_id, recom_alg, recom_size):
    
    file_path = os.path.expanduser('static/CRdata.csv')
    reader = Reader(line_format='user item rating timestamp', sep=',', rating_scale=(0,100))
    data = Dataset.load_from_file(file_path,reader=reader)
    trainset = data.build_full_trainset()
    testset = trainset.build_anti_testset()
    
    
    if(recom_alg == 'KNNBaseline_user'):
    
        similarity = {'name': 'cosine',
            'user_based': True  # compute  similarities between users
            }
        algo = KNNBaseline(sim_options=similarity)
    
    
    elif(recom_alg == 'KNNBaseline'):
        algo = KNNBaseline()
    else:
        algo = SVD()

    algo.fit(trainset)
    predictions  = algo.test(testset)

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:recom_size]

    return top_n[str(target_user_id)]


def get_top_n_for_user(target_user_id, rec_algs, recom_size):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''
    
    

    file_path = os.path.expanduser('./CRdata.csv')
    reader = Reader(line_format='user item rating timestamp', sep=',', rating_scale=(0,100))
    data = Dataset.load_from_file(file_path,reader=reader)
    trainset = data.build_full_trainset()
    testset = trainset.build_anti_testset()
    #print 'before'
    for recom_alg in rec_algs:
        if(recom_alg == 'KNNBaseline_user'):
            print(1)
    #   print 'inside'
            similarity = {'name': 'cosine',
                   'user_based': True  # compute  similarities between users
                   }
            algoKNNBaseline_user = KNNBaseline(sim_options=similarity)
    #  print "else"
            #eval('algo = ' + recom_alg + '()')
        elif(recom_alg == 'KNNBaseline'):
            print(2)
            algoKNNBaseline = KNNBaseline()
        else:
            print(3)
            algoSVD = SVD()
    #print "after"
    algoKNNBaseline_user.fit(trainset)
    algoKNNBaseline.fit(trainset)
    algoSVD.fit(trainset)
    
    predictionsKNNBaseline_user  = algoKNNBaseline_user.test(testset)
    predictionsKNNBaseline  = algoKNNBaseline.test(testset)
    predictionSVD  = algoSVD.test(testset)

    # First map the predictions to each user.
    top_nKNNBaseline_user = defaultdict(list)
    top_nKNNBaseline = defaultdict(list)
    top_nSVD = defaultdict(list)
    
    
    for uid, iid, true_r, est, _ in predictionsKNNBaseline_user:
        top_nKNNBaseline_user[uid].append((iid, est))
    for uid, iid, true_r, est, _ in predictionsKNNBaseline:
        top_nKNNBaseline[uid].append((iid, est))
    for uid, iid, true_r, est, _ in predictionSVD:
        top_nSVD[uid].append((iid, est))

        
        
    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_nKNNBaseline_user.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_nKNNBaseline_user[uid] = user_ratings[:recom_size]
        
    for uid, user_ratings in top_nKNNBaseline.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_nKNNBaseline[uid] = user_ratings[:recom_size]

    for uid, user_ratings in top_nSVD.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_nSVD[uid] = user_ratings[:recom_size]
    
    return [top_nKNNBaseline_user[str(target_user_id)],
            top_nKNNBaseline[str(target_user_id)],
            top_nSVD[str(target_user_id)]]