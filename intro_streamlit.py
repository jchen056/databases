import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.markdown("# Unifrom distribution")
st.sidebar.markdown("Unifrom distribution")
st.latex(r'''pdf: p(x)=\frac{1}{b-a}''')

num1=st.number_input("Insert a number for lower bound")
num2=st.number_input("nsert a number for upper bound")
st.write("The lower bound is",num1)
st.write("The lower bound is",num2)

st.subheader("Expected value and variance of uniform random variable")
st.latex(r'''E(X)=\frac{(a+b)}{2}''')
st.latex(r'''Var(X)=\frac{(b-a)^2}{12}''')
exp_var=st.checkbox("Compute the expected value and variance?")
if exp_var:
    st.write("The expected value of X is ",(num1+num2)/2)
    st.write("The variance of X is",(num2-num1)*(num2-num1)/12)

st.subheader("Display the pdf graph")
arr=np.random.uniform(num1,num2,10000)
fig,ax=plt.subplots()
ax.hist(arr,bins=20,density=True)
st.pyplot(fig)