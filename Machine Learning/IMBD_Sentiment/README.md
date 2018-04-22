## How do they like the movies? - IMBD movie reviews sentiment analysis
Used a XGBoost classifier with BOW(bag of words) and word embeddings from GloVe as features for sentiment analysis.   
- Text preprocessing includes: remove punctuations and numbers, tokenize and removing stopwords.
- BOW approach only used the top 10000 features with highest frequency.
- Word embedding approach used the GloVe vector of 300 dimension, and calculated the average embedding of words in the review.
