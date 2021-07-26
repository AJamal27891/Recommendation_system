# Recommendation_system
## Objective 
The objective of this system to creat an API that will return the top 10 product recommended giving whats inside the cart
----------------------------
### The Dataset 
__Data provided by Hibsaborada Ecommerce for recommendation system splited into 2 data sources:__
- __Events__ This shows the cart Id with time stamp.
- __Meta__ This shows the information for each product in the cart. 
_________________________
### Data preprocessing 
The data preprocessing for this task is following steps that will be a downstreem pipline for every new instance. 
- Merge the meta to the envet to optain the product information. 
- To pair products we consider frequency patterns algorithms spesifically FPgrowth Algorithm to minimize pari selection.
- We build a frequency table by adjusting the minimum support as a hyperparameter 
- Then we build the assosiation rules and with minimum confidence 25%. 
- We use the Confidence metric to add to our dataset. 
- The confidence metric is considered a score for each pairs.
- To fit the data into a model we use TFidf as a method for vectorization. 
_________________________
### Model creation 
We choose machine learning algorithm to predicet the confidence of each pairs; We are using Randomforest alogrithm because it is fast and accurate. we reccomend using deeplearning model for petter performance. 
We use random search to tune the Model and choose the best hyperparameters. [cite](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74)
_________________________
### Saving the best Model
After the training is complete we save the model to use it in our API. 
____________________________
### Building The API 
here we use Flask to build the API the API will take a product and matche it with all other products and return the top 10 confidence. 
