import streamlit as st
import numpy as np
# from scipy.stats import binom

st.header("Binomial Calculator")
st.write('X~Binomial(n,p)')
st.write('The possible values of X range from 0 to n and the probabilities for each of those values are given by')
st.latex(r'''P(X=x)={n \choose x} p^x (1-p)^{n-x}''')

num3=st.number_input(label='Insert a number for the number of trials',min_value=1)
num4=st.number_input(label='Select a number for p',
min_value=0.0,
max_value=1.0,value=0.5,step=0.01)

num1=st.number_input(label='Enter a number for the number of successes (x)',min_value=0,max_value=num3)
st.write("Number of successes (x)",num1)

# pmfx=binom.pmf(num1,num3,num4)
# st.write("Binomial probability P(X=x):",pmfx)
# cdfx= binom.cdf(num1, num3, num4)
# st.write("Cumulative probability P(X<=x):",cdfx)

#Let us try to estimate our PDF and PMF by drawing large samples
pmfx=sum(np.random.binomial(num3,num4,100000)==num1)/100000
st.write("Binomial probability P(X=x):",pmfx)