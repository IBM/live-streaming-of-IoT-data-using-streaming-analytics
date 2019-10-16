# Short Title

Build streams flow to analyse and predict realtime data using IBM Streaming Analytics

# Long Title

Build streams flow to analyze data using IBM Watson Streaming Analytics and predict the outcome in real-time using a Machine Learning model deployed on IBM Watson Machine Learning

# Author
* [Manoj Jahgirdar](https://www.linkedin.com/in/manoj-jahgirdar-6b5b33142/)
* [Srikanth Manne]()
* [Manjula Hosurmath](https://www.linkedin.com/in/manjula-g-hosurmath-0b47031)

# URLs

### Github repo

* https://github.com/IBM/live-streaming-of-IoT-data-using-streaming-analytics

# Summary

There is no product that appeals to all potential customers. How are those offering products to know which potential customer is likely to purchase the product? In this pattern, we gather a customer-related dataset and, based on that, predict whether the customer will buy the product if offered. All of this will happen in real-time on a dashboard so that it helps the retailer to better understand which type of customers to target to get the maximum sales of their product.

# Technologies

* [Analytics](https://developer.ibm.com/technologies/analytics/): Uncover insights with data collection, organization, and analysis.
* [Machine learning](https://developer.ibm.com/technologies/machine-learning/): Teach systems to learn without them being explicitly programmed.
* [Predictive analytics](https://developer.ibm.com/technologies/predictive-analytics/): Analyze current and historical data to make predictions.
* [Python](https://developer.ibm.com/technologies/python): An open-source interpreted high-level programming language for general-purpose programming.

# Description

We take the use case of a bank selling the personal loan to its customers and predict whether the customer will accept a loan offered to them or not. We will code the Machine Learning model in a Jupyter notebook in Watson Studio and deploy the model to Watson Machine Learning. Further, we design a Streams Flow in Watson Studio that has an input node which brings in the data from various sources such as REST API calls, Stream events from a Kafka broker, IBM Event Streams, MQTT broker, Watson IoT device platform etc... which is streamed as input to the next node that is the python model invoked from Watson Machine Learning. The predictions and various features affecting the prediction are reviewed as output which is then stored in Cloud Object Storage as a CSV file. A Streaming analytics instance associated with the flow will start running as soon as the flow is deployed and live data and predictions can be monitored on the IBM Streaming Analytics dashboard in real-time.

# Flow

![Architecture](https://github.com/IBM/live-streaming-of-IoT-data-using-streaming-analytics/doc/source/images/architecture.png)

1. Create a REST API with python and deploy it to Cloud Foundary service. Calling this API returns a json with random attribute values of the outsource dataset. Thus it simulates real-time data.
2. Create a Watson Studio instance and a Watson Machine Learning instance in IBM Cloud.
3. Create a new Jupyter notebook in Watson Studio and execute the cells to successfully train, test, get accuracy and deploy the model to Watson Machine Learning.
4. Once the Real-time data source and the machine learning model is ready the stream flow can be built. Create a new Streams Flow in Watson Studio.
5. Build a flow with input as the REST API, data processing by the deployed Watson Machine Learning model and Save the output to a csv file in Cloud Object Storage.
6. Launch the Streaming Analytics dashboard and visualize the data in real-time.

# Instructions

> Find the detailed steps for this pattern in the [readme file](https://github.com/IBM/live-streaming-of-IoT-data-using-streaming-analytics/blob/master/README.md)

1. Clone the repo
2. Deploy API
3. Create Watson Services
4. Run the Jupyter Notebook and Deploy the ML Model
5. Create IBM Streaming Analytics service
6. Create the Streams Flow in Watson Studio
7. Visualize the Streams Dashboard

# Components and services

* [IBM Streaming Analytics](https://cloud.ibm.com/catalog/services/streaming-analytics): Leverage IBM Streams to ingest, analyze, monitor, and correlate data as it arrives from real-time data sources. View information and events as they unfold.

* [IBM Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio): Watson Studio democratizes machine learning and deep learning to accelerate infusion of AI in your business to drive innovation. Watson Studio provides a suite of tools and a collaborative environment for data scientists, developers and domain experts.

* [IBM Machine Learning](https://cloud.ibm.com/catalog/services/machine-learning): IBM Watson Machine Learning is a full-service IBM Cloud offering that makes it easy for developers and data scientists to work together to integrate predictive capabilities with their applications.
