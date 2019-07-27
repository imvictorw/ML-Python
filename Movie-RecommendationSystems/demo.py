import numpy as np
from fetch_lastfm import fetchlastfm
from lightfm import LightFM

#CHALLENGE part 1 of 3 - write your own fetch and format method for a different recommendation
#dataset. Here a good few https://gist.github.com/entaroadun/1653794
#And take a look at the fetch_movielens method to see what it's doing
#

#fetch data and format it
data = fetchlastfm()

#CHALLENGE part 2 of 3 - use 3 different loss functions (so 3 different models), compare results, print results for
#the best one. - Available loss functions are warp, logistic, bpr, and warp-kos.

#create model
model = LightFM(loss='warp')
#train model
model.fit(data['matrix'], epochs=30, num_threads=2)

#CHALLENGE part 3 of 3 - Modify this function so that it parses your dataset correctly to retrieve
#the necessary variables (products, songs, tv shows, etc.)
#then print out the recommended results

def get_recommendations(model, coo_mtrx, users_ids):

    n_items = coo_mtrx.shape[1]

    for user in users_ids:

        # TODO create known positives
        # Artists the model predicts they will like
        scores = model.predict(user, np.arange(n_items))
        top_scores = np.argsort(-scores)[:3]

        print('Recomendations for user:', user)

        for x in top_scores.tolist():
            for artist, values in data['artists'].items():
                if int(x) == values['id']:
                    print('   -', values['name'])

        print('\n') # Get it pretty


get_recommendations(model, data['matrix'], [123, 1, 3])
