import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.markdown("# Probability Distribution Function")
st.sidebar.markdown("# Probability Distribution Function")

st.markdown('''
# Intro
We will cover possible probability distribution functions that you will encounter in your probability and statistics course.
Topics that will be covered include:
* discrete random variable
* continuous random variable
* probability density function and probablity mass function
* expected value and variance
* application
# Discrete RV vs Continuous RV
\                    |Discrete RV          | Continuous RV 
---------------------|---------------------|------------------
def                  |Countable, finite    |infinite 
examples             |Bernoulli, Binomial  |Uniform, Normal, Exponential 


# Some definitions
1. **random variable**: a function that assigns values to each of an experiment's outcomes
2. **probability density function**: nonnegative everywhere and the area under the curve is 1
3. **probability mass function**: a function that gives the probability that a discrete random variable is exactly equal to some value
4. **expected value**: $E(x)=\sum xp(x)$
5. **variance**: $Var(x)=E(X^2)-(E(X))^2$'''
)

image = Image.open('probability_distribution.png')
st.image(image, caption='Types of probability distribution')