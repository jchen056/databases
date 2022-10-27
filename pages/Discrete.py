import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

st.markdown("# Discrete Random Variable")
st.sidebar.markdown("# Discrete Random Variable")

st.header("Bernoulli Random Variable")
st.markdown('''X~Bern(p)''')
st.latex(r'''PMF=P(X=x)=
\begin{cases}
p & x=1 \\
1-p & x=0\\
0 & otherwise
\end{cases}''')
st.markdown('''There are two possible outcomes for Bernoulli random variables, success and failture.
P(Success)=p and P(Failture)=1-p. Conventionally, we assign the value of 1 to the event of success and the value of 0 to the event of failure. ''')

num1 = st.slider(
    label='Select a number for p',
    min_value=0.0,max_value=1.0,value=0.5)
st.write('The probability of success is', num1)

st.subheader("Expected value and variance of bernoulli random variable")
st.latex(r'''E(X)=p''')
st.latex(r'''Var(X)=p(1-p)''')
exp_var=st.checkbox("Compute the expected value and variance for selected p?")
if exp_var:
    st.write("The expected value of X is ",num1)
    st.write("The variance of X is",num1*(1-num1))

st.subheader("Generate Bernoulli random numbers")
num2=st.number_input('Insert a number for the number of Bernoulli trials')
r = bernoulli.rvs(num1, size=int(num2))
fig,ax=plt.subplots()
ax.bar(['Success(1)','Failure(0)'],[np.count_nonzero(r),len(r)-np.count_nonzero(r)])
st.pyplot(fig)
st.download_button("Download the sequence of random numbers in the binary file",r.tobytes())

st.latex(r'''---''')
st.header("Binomial Random Variable")
st.write('X~Binomial(n,p)')
st.write('The possible values of X range from 0 to n and the probabilities for each of those values are given by')
st.latex(r'''P(X=j)={n \choose j} p^j (1-p)^{n-j}''')
st.write('The random variable is used to count the number of successes as opposed to failures in n total independent attempts.')

num3=st.number_input('Insert a number for the number of trials')
num4=st.slider(label='select a number for p',
min_value=0.0,
max_value=1.0,value=0.5,step=0.01)

st.subheader('Expected value and variance of binomial random variable')
st.latex(r'''X=X_1+X_2+...+X_n''')
st.latex(r'''E(X)=E(X_1)+E(X_2)+...+E(X_n)=np''')
st.latex(r'''Var(X)=np(1-p)''')
if st.button("Compute the expected value and variance for X"):
    st.write("The expected value of X is ",num3*num4)
    st.write("The variance of X is",num3*num4*(1-num4))

st.subheader("Generate random numbers")
st.code('''n,p=10,0.5#number of trials, probability of each trial
s=np.random.binomial(n,p,1000)
#result of flipping a fair coin 10 times, tested 1000 times''')

st.latex(r'''---''')
st.header('Poisson random variables')
st.write('X~Poisson(a)')
st.latex(r'''P(X=i)=\frac{a^i e^{-a}}{i!}''')
st.write('The possible values for X are non-negative integers, 0,1,2,3...')

st.subheader('Expected value and variance of Poisson random variable')
st.write('E(X)=a')
st.write('E(X)=a')

st.subheader("Generate random numbers")
num5=st.number_input('Insert a number for the expected number of events ocurring in a fixed-time interval')
num6=st.number_input('Insert a number for the number of trials',key=1000)
s=np.random.poisson(num5,int(num6))
fig,ax=plt.subplots()
plt.hist(s,density=True)
st.pyplot(fig)
st.code('''s=np.random.poisson(5,10000)
plt.hist(s,density=True)''')

st.subheader('Application of Poisson Random Variable')
st.write('Poisson random variables can be used to approximate the PMF of Binomial random variables when n is really big and p is small.')
st.write('Ex. A rare disease occurs in 0.5% of the population. 5000 people are randomly chosen. What is the probability that exactly 24 people in this sample are carriers of this disease?')
st.markdown('''We can define the success as carrying the disease and failure as not carrying the disease. X is the number of carriers in our sample. X~Binomial(5000,0.005).''')
st.latex(r'''P(X=24)={5000 \choose 24} 0.005^{24} 0.995^{4976} \approx 0.0797''')
st.write('For those using plain calculators, it can be hard to compute.')
st.latex(r'''E(X)=a=np=5000*0.005=25 \\
P(X=24)=\frac{a^i e^{-a}}{i!}=\frac{25^{24} e^{-25}}{24!} \approx 0.0795''')
st.write('Our estimation is not too far away from the actual value.')


st.latex(r'''---''')

st.markdown('''**Food for thought** 
1. Prove that the PMF for Poisson random variable is a valid PMF. (Hint:sum up the probabilities to see if they add up to one)
2. Derive the formulas for the expected value and variance for Poisson random variable.''')



