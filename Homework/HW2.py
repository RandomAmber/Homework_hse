
# coding: utf-8

# In[ ]:


import string
text = input().split(" ")
if len(text) < 2:
    print ("Попробуйте снова")
    
punct = ""
output_text = []

#Работаем с пунктуацией и изменением порядка слов:
if text[-2][-1] in string.punctuation:
    punct = text[-2][-1]
    text[-2] = text[-2].replace(punct, "")
last = text[-1]
znaki = ''.join([last[-i] if last[-i] in string.punctuation else '' for i in range(1,len(last)+1)])
last = last[:-len(znaki)]
text[-1],text[-2] = text[-2], last + punct
text = " ".join(text) + znaki


#Работа над словарем:

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
keys = alphabet.upper() + alphabet + string.punctuation + string.whitespace
values = alphabet.upper()[1:] + alphabet.upper()[0] + alphabet[1:]+ alphabet[0] + string.punctuation + string.whitespace
shifr = dict(zip(keys, values))


#Шифрование:
for letter in text:
    output_text.append(shifr[letter])
print(''.join(output_text), sep = "", end = "")

