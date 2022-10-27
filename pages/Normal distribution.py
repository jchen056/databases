import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.markdown("# Normal distribution")
st.sidebar.markdown("# Normal distribution")
st.markdown('''X~Normal($\mu$,$(\sigma)^2$)''')
st.latex(r'''pdf: f(x)=\frac{1}{\sqrt{2\pi (\sigma)^2}}e^{-\frac{(x-u)^2}{2 (\sigma)^2}}''')

st.subheader("Expected value and variance for Normal random variable")
st.markdown('''E(X)=$\mu$''')
st.markdown('''Var(X)=$(\sigma)^2$''')

st.subheader('PDF for normal random variable')
num1=st.number_input("Insert a number for mean",value=0)
num2=st.number_input("Insert a number for standard deviation",value=1)
num3=st.number_input("Insert a number for the number of trials",value=1000)
st.write("The mean is",num1)
st.write("The standard deviation is",num2)
st.write("The number of trials is",num3)
s = np.random.normal(loc=num1, scale=num2,size=int(num3))
fig,ax=plt.subplots()
ax.hist(s,density=True)
st.pyplot(fig)
st.code('''mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 10000)''',language="python")

st.subheader('Food for thought')
st.markdown('''1. Explain why the PDF for normal distribution is a valid PDF.
1. Find the E(X) and Var(X) for normal distribution.
1. Prove that a linear transformation of a normal random variable is normal.''')