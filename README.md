# Recommendation_system
## Objective 
The objective of this system is to create an API that will return the top 10 products recommended giving what's inside the cart This model achieves 96% of accuracy and 0.04 rmse for predicting the frequency confidence on the given dataset. 
The frequency confidence is calculated using Fpgrowth Algorithm and the predictor is the RandomForest classifier.
----------------------------
### The Dataset 
__Data provided by Hibsaborada Ecommerce for recommendation system split into 2 data sources:__
- __Events__ This shows the cart Id with a time stamp.
- __Meta__ This shows the information for each product in the cart. 
_________________________
### Data preprocessing 
The data preprocessing for this task is following steps that will be a downstream pipeline for every new instance. 
- Merge the meta to the events to obtain the product information. 
- To pair products we consider frequency patterns algorithms specifically the FPgrowth Algorithm to minimize pairs selection.
- We build a frequency table by adjusting the minimum support as a hyperparameter 
- Then we build the association rules and with minimum confidence of 70%. 
- We use the Confidence metric to add to our dataset. 
- The confidence metric is considered a score for each pair.
- To fit the data into a model we use TFidf as a method for vectorization. 
_________________________
### Model creation 
We choose a machine-learning algorithm to predict the confidence of each pair; We are using the Random forest algorithm because it is fast and accurate. we recommend using the deep-learning model for better performance. 
We use random search to tune the Model and choose the best hyperparameters. [cite](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74)
_________________________
### Saving the best Model
After the training is complete we save the model to use it in our API. 
____________________________
### Building The API 
here we use Flask to build the API the API will take a product and match it with all other products and return the top 10 confidence. 
Application instuction;
- Create python/conda enviroment python==3.6x
- ``` pip install -r requirements.txt```
- ```python app.py```
After running the application on the server
To use the API you have to provide the following POST request 
```{
'productid':
'brand':
'category':
'subcategory':
'name':
}
```
once you provided the schema you will receive a list of the top 10 items id with their confidence scores such as 
```
{'product names': array(['Palette Kalıcı Doğal Renkler 10-4 PAPATYA',
        'Best Pet Jöle İçinde Parça Etli Somonlu Konserve Yetişkin Kedi Maması 415 gr',
        'Türkiye Tarım Kredi Koop.Yeşil Mercimek 1 kg',
        'Namet Fıstıklı Macar Salam 100 gr',
        'Muratbey Burgu Peyniri 250 gr', 'Sek Quark Sade 140 g',
        'Sırmakeş Doğal Kaynak Suyu 1,5 lt',
        "Asil Fırın Gurme Cookie Çikolata 8'li",
        'Granny Smith Elma 500 gr', 'Ekşi Mayalı Ekmek 1 Kg'], dtype=object),
 'scores': [array([['HBV00000AX6LR', 0.9581529657690381],
         ['HBV00000BSAQG', 0.9581529657690381],
         ['HBV00000JUHBA', 0.9581529657690381],
         ['HBV00000NE0QI', 0.9581529657690381],
         ['HBV00000NE0UQ', 0.9581529657690381],
         ['HBV00000NE1NR', 0.9581529657690381],
         ['HBV00000NH2LJ', 0.9581529657690381],
         ['HBV00000NVZ7D', 0.9581529657690381],
         ['HBV00000NVZCG', 0.9581529657690381],
         ['HBV00000OEL9Q', 0.9581529657690381]], dtype=object)]}
```
