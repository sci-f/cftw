#!/usr/bin/env python

# Competition Hosts

# ADD IMPORTS HERE #######################################

from helpers.data import load_data
from helpers.logger import bot

#bot.debug("Hello, here is a debug message!")
#bot.debug("Hello, here is a warning message!")
#bot.debug("Hello, here is an error message!")
#bot.debug("Hello, here is an info message!")


train = load_data(name="training")

## BUILD EXAMPLE MODEL HERE #############################


variables = []

model = "build model here"

# fit model here



# MODEL TESTING ########################################


# import checking functions here
from metrics import *


# show the user how to use them here
# check_agreement(model,variables)
# check_correlation(model,variables)

# train_eval = train[train['min_ANNmuon'] > 0.4]
# check_auc(model,train_eval)



# DERIVE RESULT FOR TEST ###############################
from helpers.result import save_result


test = load_data(name="test")
#result = pandas.DataFrame({'id': test.index})
#result['prediction'] = baseline.predict_proba(test[variables])[:, 1]
save_result(result)
