from sklearn.cluster import DBSCAN # Use scikit-learn to perform clustering

# ElementList contains a line for each element we want to cluster with his top and left position, width and eight and xpath

'''

xpath_dict = set() # Build a dictionnary of XPATH of each element
for item in ElementList:
    path_split_idx = find(item["xpath"],"/")
    for idx in path_split_idx:
        xpath_dict.add(item["xpath"][:idx])
xpath_dict=list(xpath_dict)

# Build feature matrix with each element

features = [] # Table will store features for each element to cluster
for item in ElementList:
    # Keep only inside browser visual boundary
    if (item["left"] >0 and (item["top"] >0
        and item["features"]["left"]+item["width"] <1200):
        visual_features = (
            [item["left"] ,
            item["left"] + item["width"],
            item["top"],
            item["top"] + item["height"],
            (item["left"] + item["width"] + item["left"]) / 2,
            (item["top"] + item["top"] + item["height2"])/ 2)
        dom_features = [0] * len(xpath_dict) # using DOM parent presence as a feature. Default as 0
        path_split_idx = find(item["xpath"], "/")

        for i, idx in enumerate(path_split_idx):
            # give an empirical 70 pixels distance weight to each level of the DOM (far from perfect implementation)
            dom_features[xpath_dict.index(item["xpath"][:idx])] = 800 / (i + 1)

        # create feature vector combining visual and DOM features
        feayures.append(visual_features + dom_features)

features = np.asarray(features) # Convert to numpy array to make DBSCAN work

# DBSCAN is a good general clustering algorithm
eps_value=900 # maximum distance between clusters
db = DBSCAN(eps=eps_value, min_samples=1, metric='cityblock').fit(features)

# DBSCAN Algorithm returns a label for each vector of input array
labels = db.labels_

'''