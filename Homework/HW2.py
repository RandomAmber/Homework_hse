
# coding: utf-8

# In[ ]:


print ("Введите предложение на русском языке:")
s = input()
# Подготавливаем предложение: 
text = s.split()
output_text = []
last_word = []
ending = []
for i in text[-1]:
    if i != "!" and i != "." and i != "?":
        last_word.append(i)
    else:
        ending.append(i)
text[-1] = text[-2]
text[-2] = "".join(last_word)

# Создаем словарь:
abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя .,?!:;"
inv = "бвгдеёжзийклмнопрстуфхцчшщъыьэюяа .,?!:;"
lower = list(abc)
upper = list(abc.upper())
inv_lower = list(inv)
inv_upper = list(inv.upper())
keys = lower + upper
values = inv_lower + inv_upper
d = dict(zip(keys, values))

# Шифруем предложение:
for letter in s:
    output_text.append(d[letter])
print (''.join(output_text)[:-1], ''.join(ending), sep = "", end = "")

