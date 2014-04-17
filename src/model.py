#Python Modules
# from sklearn.ensemble import GradientBoostingRegressor as Model
# from sklearn.linear_model import Ridge as Model
from sklearn.ensemble import RandomForestRegressor as Model
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error as score



#Local Modules
import config
from wrappers import debug
import data as dc
import feature_selection as fs

@debug
def loadData(datafile, cost, d):
    """
    Loads the feature pickle file from feature_selection.py
    """
    path = config.path("..","data",datafile,"features","features%s.p" % cost)
    if not config.os.path.exists(path):
        fs.select([d.tags.index(cost)], datafile, d)
    return config.load(path)

@debug
def main(cost, datafile, importance):
    """
    Runs main model and predicts for an accuracy score
    """
    #Get Data Handler
    d = config.get(config.path("..","data",datafile,"data","dHandler.p"), dc.Data, datafile = datafile, include_costs = False)
    #Get Data
    features, target = loadData(datafile, cost, d)
    #Splitting to testing and training datasets
    x_train, x_test, y_train, y_test = train_test_split(features[:,:importance], target,test_size=0.15, random_state=42)

    model = Model()
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    accuracy = score(predictions, y_test)
    print accuracy ** .5


if __name__ == "__main__":
    import sys
    datafile = sys.argv[1]

    # Clean Past Data
    config.clean([\
        # "data",\
        # "features",\
        # "formatted",\
        # "models",\
        ], datafile = datafile)
        
    d = config.get(config.path("..","data",datafile,"data","dHandler.p"), dc.Data, datafile = datafile, include_costs = False)  
    print "\n".join([d.tags[tag] + "\t" + d.features[d.tags[tag]][1] for tag in d.costs])
    main(raw_input("Pick a cost\n"),datafile, 15)