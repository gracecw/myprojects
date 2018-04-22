## Sentiment Analysis on Yelp Reviews with Apache Spark

Project descriptionIn this project, we used the public Yelp dataset and conducted sentiment analysis on over 800,000 Yelp reviews (3.6 GB) in a distributed system using Apache Spark.

We performed data ETL with SparkSQL and MongoDB; built feature extraction and machine learning pipeline with Spark ML on AWS EMR cluster. 
The sentiment analysis model used a multilayer perceptron classifier trained on TF-IDF weighting as features, which achieved an accuracy of 0.89 and AUC of 0.91.

In addition, an unsupervised text mining model has been built to extract keywords from customer reviews to provide insights into attributes and features pertaining to a specific business.

- Sentiment Analysis: Sentiment analysis model using Spark ML
- Keyword Extraction: Discover the top words appears in Postive/Negative reviews and build a worldcloud using keywords extracted from the reviews of a specific business