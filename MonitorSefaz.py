#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyautogui')


# In[2]:


import pyautogui
import time

pyautogui.TIME = 5
# passo a passo
# passo 1: Entra no google
# passo 2: Acessar site (pelo link)

pyautogui.hotkey("ctrl","t") 
time.sleep(5)
pyautogui.write("https://conta.tecnospeed.com.br/login")
time.sleep(5)
pyautogui.press("enter")

# Pode ser que o navegador demore a carregar 
time.sleep(10)

# passo 3: fazer login
# Clicar no espaço de Login
pyautogui.click(x=924, y=495)
pyautogui.write("financeirogrupoparceria@gmail.com")
pyautogui.press("tab")
pyautogui.write("Senha do email")
pyautogui.click(x=988, y=580)

# passo 4: Acessar a sefaz de PE



# In[3]:


time.sleep(5)
print(pyautogui.position())


# In[4]:


# Passo 5: Acessar Chat Do suporte
#Abrir uma nova aba

pyautogui.hotkey("ctrl","t")

#Informar o link do site
time.sleep(5)
pyautogui.write("www.smsolucoesdigital.com.br/")

#Precionar enter para entrar no site
time.sleep(5)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=1634, y=748)
time.sleep(5)
pyautogui.click(x=77, y=216)
time.sleep(5)
pyautogui.click(x=143, y=329)
time.sleep(5)
pyautogui.press("F11")


# In[ ]:




