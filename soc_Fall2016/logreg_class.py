import pandas as pd
import numpy as np
from statsmodels import api as sm


class logreg_class:
    # reading input file
    def __init__(self):
        print 'Create Machine Learning Instance'
    def initialize(self):
        input_file = pd.read_csv("/home/hduser1/Downloads/reduced/training_model/part-r-00000")

        input_file.columns = ["market", "repeat", "repeat_trips"
            , "chain", "same_company_purchases", "same_brand_purchases", "same_category_purchases"]

        # summarize the data

        # print input_file.describe()

        # take a look at the standard deviation of each column
        print input_file.std()

        data_columns = ["repeat", "same_company_purchases", "same_brand_purchases", "same_category_purchases"]

        new_input = input_file[data_columns]

        # modelling
        train_cols = new_input.columns[1:]
        logit = sm.Logit(new_input["repeat"], new_input[train_cols])

        # fit the model
        result = logit.fit()
        return result

    # summary of model
    # print result.summary()

    # look at the confidence interval of each coeffecient
    # print result.conf_int()
    def predict(self, result, input_list):
        # reading testdata
        # train_cols= ["same_company_purchases","same_brand_purchases","same_category_purchases"]
        # output= pd.read_csv("/home/hduser1/Desktop/pig_scripts/tables/test_data.csv")
        # print "output"
        # print output
        # output.columns=["same_company_purchases","same_brand_purchases","same_category_purchases"]
        # print output[train_cols]
        # output["repeat_prediction"]=result.predict(output)
        output = [input_list]
        #print 'About to predict the result for the '+str(input_list)
        return result.predict(output)

    '''r=initialize()
    predicted_value predict(r,[0,0,0])'''

