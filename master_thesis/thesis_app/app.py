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
from .models import user_rate

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
    
    
def get_top_n_for_user(target_user_id, recom_alg, recom_size):
    
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


