from sklearn import tree

clf = tree.DecisionTreeClassifier()

# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3

# [AB, hits, hr, strikeout]
X = [[384, 113, 20, 43], [380, 124, 15, 43], [361, 94, 26, 61], [347, 97, 10,40], [281, 83, 23, 66],
     [272, 78, 15, 6], [247, 57, 12, 88],
     [190, 56, 11,51], [163, 37, 7, 29], [125, 40, 11, 39], [182, 60, 20, 87]]

Y = ['average', 'average', 'power', 'power', 'power', 'power', 'average', 'average',
     'average', 'power', 'power']

# # [height, weight, shoe_size]
# X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
#      [190, 90, 47], [175, 64, 39],
#      [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
# 
# Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
#      'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

prediction = clf.predict([[150, 40, 2, 70]])

# CHALLENGE compare their reusults and print the best one!

print(prediction)