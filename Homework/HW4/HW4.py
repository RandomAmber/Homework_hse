
# coding: utf-8

# In[1]:


import re


# In[2]:


def get_text(path):
    with open(path, "r", encoding = "utf-8") as file:
        text = "".join(file.readlines())
    return text
        

def write_processed_text(path, text):
    with open(path, "w", encoding = "utf-8") as file:
        file.write(text)


# In[12]:


def main():
    
    linguistics_text = get_text("linguistics.txt")
    shashlik_text = re.sub("язык(\w{0,3})([^е́а-я])", r"шашлык\1\2", linguistics_text)
    shashlik_text = re.sub("Язык(\w{0,3})(\W)", r"Шашлык\1\2", shashlik_text)
    write_processed_text("shashlik.txt", shashlik_text)
    
    finland_text = get_text("finland.txt")
    malasya_text = re.sub("Финл(я|я́)нди(\w{0,2})(\W)", r"Малази\2\3", finland_text)
    malasya_text = re.sub("ФИНЛЯНДИ(\w{0,2})(\W)", r"МАЛАЗИ\1\2", malasya_text)
    write_processed_text("malasya.txt", malasya_text)
    
    philosophy_text = get_text("philosophy.txt")
    astrology_text = re.sub("философи(\w{0,3})(\W)", r"астрологи\1\2", philosophy_text)
    astrology_text = re.sub("Филос(о|о́)фи(\w{0,3})(\W)", r"Астрологи\2\3", astrology_text)
    astrology_text = re.sub("ФИЛОСОФИ(\w{0,3})(\W)", r"АСТРОЛОГИ\1\2", astrology_text)
    write_processed_text("astrology.txt", astrology_text)
    

if __name__ == '__main__':
    main()

