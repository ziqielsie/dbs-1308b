#!/usr/bin/env python
# coding: utf-8

# In[18]:


from flask import Flask,render_template,request    
import joblib


# In[19]:


app = Flask(__name__) 


# In[20]:


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        rates = float(request.form.get('rates'))
        print(rates)
        model1 = joblib.load('regression_DBS')
        pred1 = model1.predict([[rates]])
        
        model2 = joblib.load('tree_DBS')
        pred2 = model2.predict([[rates]])
        
        
        return(render_template('index.html',result1=pred1, result2=pred2))
    else:
        return(render_template('index.html',result1='waiting',result2='waiting'))
    


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




