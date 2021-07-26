# Building the API 
import flask
import joblib
import io
import string
import time
import os
import numpy as np
from flask import Flask, jsonify, request
import pandas as pd

model = joblib.load(r'/data/resys.model')
pca = joblib.load(r'/data/pca.model')
vectorizer = joblib.load(r'/data/vectorizer.model')

products = pd.read_json(r'/data/meta.json')
products.meta.to_json(r'meta.json')
products = pd.read_json(r'meta.json').T
#antecedents 	consequents 	productid 	brand 	category 	subcategory 	name 	
#productid_right 	brand_right 	category_right 	subcategory_right 	name_right

def get_productdata(id):
  if id in meta.productid.values:
    df = meta.rename(columns={'productid':'productid_right', 	'brand':'brand_right',
                              'category':'category_right', 	'subcategory':'subcategory_right', 'name':	'name_right'})
    df['antecedents'] = id
    df['consequents'] = meta.productid
    print(len(meta.productid))
    cols = ['productid', 	'brand', 	'category', 	'subcategory', 	'name']
    for c in cols :
      df[c] = meta[meta['productid'] == id ][c].values[0]

    df = df[['antecedents', 	'consequents', 	'productid', 	'brand', 	'category', 	'subcategory', 	'name',
            'productid_right', 	'brand_right', 'category_right',	'subcategory_right', 	'name_right']]
    return df
  else :
    return None

def pipline(df):
  corpus_list = []
  for seq in df.values:
    try:
      x = ' '.join(seq)
    
    except :
      x = 'Empty' 
    corpus_list.append(x)
  features = vectorizer.transform(corpus_list)
  features = pca.transform(features)
  df['confidence'] = model.predict(features)
  df.sort_values('confidence',ascending=False)
  return df[['consequents','confidence']].values[:10],df['name_right'].values[:10]




def return_list(img):
    return 1 if model.predict(img)[0][0] > 0.5 else 0


app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def infer_recommender():
    id = request.get_json('id')
    df = get_productdata(id)
    if df:
      return jsonify(pipline(df))
    else :
      return jsonify("This ID doesn't exist")    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
