#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle 
import streamlit as st

model_file = open('./decision_tree_iris.sav', 'rb')
model = pickle.load(model_file)

classes = {
    0: "Iris setosa",
    1: "Iris versicolor",
    2: "Iris virginica"
}

st.title("Iris - Decision tree prediction")

petal_width = st.slider("Petal width", min_value=0.0, max_value=4.0, step=0.1)
petal_length = st.slider("Petal length", min_value=0.0, max_value=4.0, step=0.1)
sepal_width = st.slider("Sepal width", min_value=0.0, max_value=4.0, step=0.1)
sepal_length = st.slider("Sepal length", min_value=0.0, max_value=4.0, step=0.1)

flower_like = st.selectbox(
    'Do you like flowers?',
    ('Nope', 'Maybe', 'What is a flower???'))

if st.button("Predict flower"):
    prediction = model.predict([[petal_width, petal_length, sepal_width, sepal_length]])[0]
    flower_name = classes[prediction]
    st.write("The flower is", flower_name)

    st.write("Your answer to 'Do you like flowers' is: ", flower_like)

