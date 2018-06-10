
# coding: utf-8

# ## 1. Include a section with your name

# In[1]:


print('My name is Zhicheng (Jason) Xue')


# ## Import Numpy package

# In[2]:


import numpy as np


# ## 2.  Create matrix A with size (3,5) containing random numbers A = np.random.random(15)

# In[3]:


A=np.matrix(np.random.random(15))


# In[4]:


A=A.reshape(3,5)


# In[5]:


A


# ## 3.  Find the size and length of matrix A

# In[6]:


A.size #size of matrix A


# In[7]:


len(A) #length of matrix A using len() function in Python which returns number of rows in a matrix


# #### Comment: I looked up definition of length of matrix in Matlab (https://www.mathworks.com/help/matlab/ref/length.html)
# #### length of a matrix should be length of largest array dimension so I also tried below

# ![Example From Matlab](Matlab_MatrixLength.png)

# In[8]:


np.max(A.shape)


# ## 4.  Resize (crop/slice) matrix A to size (3,4)

# In[9]:


A=A[:,:4]


# In[10]:


A


# ## 5.  Find the transpose of matrix A and assign it to B

# In[11]:


B=A.T


# In[12]:


B


# ## 6.  Find the minimum value in column 1 of matrix B (check the properties of a matrix – ‘B.min()’)

# In[13]:


B.min(0)[0,0]


# ## 7.  Find the minimum and maximum values for the entire matrix A

# ### minimum of A

# In[14]:


A.min()


# ### maximum of A

# In[15]:


A.max()


# ## 8.  Create vector X (an array) with 4 random numbers

# In[16]:


X=np.array(np.random.random(4))


# In[17]:


X


# In[18]:


X.shape


# In[19]:


A.shape


# ## 9.  Create a function and pass vector X and matrix A in it

# In[20]:


def matmul_new(X,A):
    D=A.dot(X)
    return D


# ## 10.  In the new function multiply vector X with matrix A and assign the result to D
# (note: you may get an error! ... think why and fix it. Recall matric manipulation in class!)

# In[21]:


D=matmul_new(X,A)


# In[22]:


D


# ## 11.  Create a complex number Z with absolute and real parts != 0

# In[23]:


Z=3+4j


# In[24]:


type(Z)


# ## 12.  Show its real and imaginary parts as well as it’s absolute value

# ### real part

# In[25]:


Z.real


# ### imaginary part

# In[26]:


Z.imag


# ### absolute part

# In[27]:


np.absolute(Z)


# ## 13.  Multiply result D with the absolute value of Z and record it to C

# In[28]:


D.shape


# In[29]:


C=D*np.absolute(Z)


# In[30]:


C


# ## 14.  Convert matrix B from a matrix to a string and overwrite B

# In[31]:


B


# In[32]:


B=np.array_str(B)


# In[33]:


B


# ## 15.  Display a text on the screen: ‘Your Name is done with HW2‘

# In[34]:


print('Zhicheng Xue is done with HW2')


# ## 16.  Organize your code: use each line from this assignment as a comment line before each step
# ## 17.  Save all steps as a script in a .py file
# ## 18.  Email your Github link to me including your .py file + screenshots of your running code no later than midnight on Saturday Jun.09.
