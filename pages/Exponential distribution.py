import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.markdown("# Exponential distribution")
st.sidebar.markdown("# Exponential distribution")
st.markdown('''X ~ Exponential($\lambda$)''')
st.markdown('''pdf: $f(x;\lambda)=\lambda e^{- \lambda x}$ supported on (0,$\infty$)''')

num1=st.number_input("Insert a number for rate parameter",value=2)
st.write("The rate parameter is",num1)


st.subheader("Expected value and variance of exponential random variable")
st.latex(r'''E(X)=\frac{1}{\lambda}''')
st.latex(r'''Var(X)=\frac{1}{(\lambda)^2}''')
exp_var=st.checkbox("Compute the expected value and variance?")
if exp_var:
    st.write("The expected value of X is ",1/num1)
    st.write("The variance of X is",(1/num1)*(1/num1))

st.subheader("Display the pdf graph")
arr=np.random.exponential(1/num1,10000)
fig,ax=plt.subplots()
ax.hist(arr,bins=20,density=True)
st.pyplot(fig)

st.subheader("Food for thought")
st.markdown('''1. Find E(X) and Var(X) for Exponential random variable.
2. Suppose that a radioactive element has a half life of h years. What is the probability that the atom will decay after a years but before b years.''')