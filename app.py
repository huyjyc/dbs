#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[ ]:





# In[2]:


import joblib


# In[ ]:





# In[3]:


app = Flask(__name__)


# In[ ]:





# In[ ]:





# In[4]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression")
        pred1 = model1.predict([[rates]])
        model2 = joblib.load("decision_tree")
        pred2 = model2.predict([[rates]])
        
        return(render_template("index.html", result1 =pred1, result2 = pred2))
    else:
        return(render_template("index.html", result1 = "WAITTING", result2 = "WAITTING"))


# In[ ]:





# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




