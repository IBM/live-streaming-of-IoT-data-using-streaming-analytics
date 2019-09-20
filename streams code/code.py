#
# YOU MUST EDIT THE SCHEMA and add all attributes that you are returning as output.
#
# Preinstalled Python packages can be viewed from the Settings pane.
# In the Settings pane you can also install additional Python packages.

import sys
import logging
import pickle
import pandas as pd

# Use this logger for tracing or debugging your code:
logger = logging.getLogger(__name__)
# Example:
#     logger.info('Got to step 2...')

# init() function will be called once on flow initialization
# @state a Python dictionary object for keeping state. The state object is passed to the process function
def init(state):
    # do something once on flow initialization and save in the state object
    pass


# process() function will be invoked on every event tuple
# @event a Python dictionary object representing the input event tuple as defined by the input schema
# @state a Python dictionary object for keeping state over subsequent function calls
# return must be a Python dictionary object. It will be the output of this operator.
#        Returning None results in not submitting an output tuple for this invocation.
# You must declare all output attributes in the Edit Schema window.
def process(event, state):
    id = event['ID']
    age = event['Age']
    experience = event['Experience']
    income = event['Income']
    zipcode = event['ZIPCode']
    family = event['Family']
    ccavg = event['CCAvg']
    education = event['Education']
    motgage = event['Mortgage']
    securitiesaccount = event['SecuritiesAccount']
    cdaccount = event['CDAccount']
    online = event['Online']
    creditcard = event['CreditCard']
    
#   mytupple = (id,age,experience,income,zipcode,family,ccavg,education,motgage,securitiesaccount,cdaccount,online,creditcard)
    mylist = []
    mylist.append([age,income,zipcode,family,ccavg,education,motgage,securitiesaccount,cdaccount,online,creditcard])

    test_set = pd.DataFrame(mylist, columns=['Age', 'Income', 'ZIPCode', 'Family', 'CCAvg', 'Education', 'Mortgage', 'SecuritiesAccount', 'CDAccount', 'Online', 'CreditCard'])

# Invoke the model-specific scoring function
    model = state['model']
    event['Prediction'] = model.predict(test_set)
    
    return event

# Ensure that the Python packages used in this streams flow are compatible
# with the packages that you used to create the model. (Click Settings > Runtime).
def load_model(state, model):
	state['model'] = model
