import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.markdown("# Exponential distribution")
st.sidebar.markdown("# Exponential distribution")
st.latex(r'''pdf: f(x;\lambda)=\lambda e^{- \lambda x}''')

num1=st.number_input("Insert a number for rate parameter")
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