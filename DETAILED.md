
* The Streams Canvas will look like this. 

![](/doc/source/images/streamcanvas.png)

We need three blocks for our demo.

1. **Input Block** - HTTP Request Block
2. **Processing Block** - Python Model
3. **Output Block** - Debug

#### 6.1 Input Block 

* Add the _`Http`_ block from the _`SOURCES`_ tab from the left panel and set the properties as shown.

![](doc/source/images/Http-input-block2.gif)

* Set the HTTP REQUEST DEFINATION as follows:

|URL   |Method   |Headers   |Polling Interval(sec)   |Response body parsing   |
|---|---|---|---|---|
|can be found in step 2 https://my-api-xx-yy.eu-gb.mybluemix.net   |GET  |leave blank  |1  |JSON  |

>NOTE: Polling Interval is the time in seconds for how often the API call is made by the Stream.

* Set the OUTPUT SCHEMA as follows:

|Attribute Name |Type |Path |
|---|---|---|
|ID |Number |/ID  |
|Age |Number |/Age  |
|Experience |Number |/Experience  |
|Income |Number |/Income  |
|ZIPCode |Number |/ZIPCode  |
|Family |Number |/Family  |
|CCAvg |Number |/CCAvg  |
|Education |Number |/Education  |
|Mortgage |Number |/Mortgage  |
|SecuritiesAccount |Number |/SecuritiesAccount  |
|CDAccount |Number |/CDAccount  |
|Online |Number |/Online  |
|CreditCard |Number |/CreditCard  |

>NOTE: These Attributes are taken from the Dataset.

* Finally you can click on the _Preview_ button to view the Incoming data stream every polling second.

#### 6.2 Processing Block

* Add the _`Python Model`_ block from the _`PROCESSING AND ANALYTICS`_ tab from the left panel and set the properties as shown.

![](/doc/source/images/python-block.gif)

* **Python Model** : Select the Naive Bayes model Deployed on Watson Machine Learning.

* Under CODE tab click on _**Python Packages**_ and add the following three python packages:
  * scikit-learn == 0.21.3
  * numpy == 1.17.2
  * pandas == 0.25.1
  
 ![](/doc/source/images/python-block2.gif)
 
* Click on the Python model block again to get the Model Settings panel. Under code, delete the existing code and add the following code:

```python
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
```

* **SCHEMA** : Drag and connect the 1st Block to the 2nd block as shown, you can then notice the Attributes defined in step 6.1 appearing as Input Schema for the model. Now set the Output Schema as follows:

|Attribute Name |Type |
|---|---|
|ID	|Number	|
|Prediction	|Number	|
|Income	|Number	|
|CCAvg	|Number	|
|Mortgage	|Number	|
|SecuritiesAccount	|Number	|

#### 6.4 Output Block

* Add the _`Debug`_ block from the _`TARGETS`_ tab from the left panel and set the properties as shown.

![](/doc/source/images/output-block.gif)

* Finally save and run the Stream Flow as shown. It may take some time to deploy and run. Once the Stream is deployed and running you can visualize the Stream in the Streaming Analytics Dashboard.
