# Short Title

Build streams flow to analyse and predict realtime data using IBM Streaming Analytics

# Long Title

Build streams flow to analyse data using IBM Streaming Analytics and to predict value in realtime using a python model deployed on IBM Watson Machine Learning.

# Author
1. [Manoj Jahgirdar](https://www.linkedin.com/in/manoj-jahgirdar-6b5b33142/)
2. [Srikanth Manne]()
3. [Manjula Hosurmath](https://www.linkedin.com/in/manjula-g-hosurmath-0b47031)

# URLs

### Github repo

> "Get the code": 
* https://github.com/IBM/live-streaming-of-IoT-data-using-streaming-analytics

### Other URLs

# Summary

There is no product that appeals to all potential customers. How are those offering products to know which potential customer is likely to purchase the product? In this pattern, we gather a customer-related dataset and, based on that, predict whether the customer will buy the product if offered. All of this will happen in real-time on a dashboard so that it helps the retailer to better understand which type of customers to target to get the maximum sales of their product.

# Technologies

# Description

We take the use case of a bank selling the personal loan to its customers and predict whether the customer will accept a loan offered to them or not. We will code the Machine Learning model in a Jupyter notebook in Watson Studio and deploy the model to Watson Machine Learning. Further, we design a Streams Flow in Watson Studio that has an input node which brings in the data from various sources such as REST API calls, Stream events from a Kafka broker, IBM Event Streams, MQTT broker, Watson IoT device platform etc... which is streamed as input to the next node that is the python model invoked from Watson Machine Learning. The predictions and various features affecting the prediction are reviewed as output which is then stored in Cloud Object Storage as a CSV file. A Streaming analytics instance associated with the flow will start running as soon as the flow is deployed and live data and predictions can be monitored on the IBM Streaming Analytics dashboard in real-time.

# Flow

1. Create a REST API with Python and deploy it to Cloud Foundry service. Calling this API returns a json with random attribute values of the outsource dataset. Thus it simulates real-time data.
2. Create a Watson Studio instance and a Watson Machine Learning instance in IBM Cloud.
Create a new Jupyter notebook in Watson Studio and execute the cells to successfully train, test, get accuracy and deploy the model to Watson Machine Learning.
Once the real-time data source and the machine learning model is ready the stream flow can be built. Create a new Streams Flow in Watson Studio.
Build a flow with input as the REST API, data processing by the deployed Watson Machine Learning model and save the output to a csv file in Cloud Object Storage.
Launch the Streaming Analytics dashboard and visualize the data in real-time.

# Instructions

> Find the detailed steps for this pattern in the [readme file](https://github.com/IBM/live-streaming-of-IoT-data-using-streaming-analytics/blob/master/README.md)

# Components and services

# Runtimes

# Related IBM Developer content

# Related links

# Announcement
