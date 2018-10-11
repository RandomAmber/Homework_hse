
# coding: utf-8

# In[ ]:


# Импорт библиотеки, считывание файлов. 
import random

def read_from_file(file):
    with open(file, "r", encoding = 'utf-8-sig') as open_file:
        data = open_file.read().splitlines()
    return data

adj_list = read_from_file("adjectives.tsv")
nom_list = read_from_file("nominatives.tsv")
acc_list = read_from_file("accusatives.tsv")
indef_pst_list = read_from_file("indef.pst.tsv")
inst_list = read_from_file("instrumentals.tsv")
when_list = read_from_file("times.tsv")
where_list = read_from_file("locatives.tsv")
question_list = read_from_file("questions.tsv")
def_pst_list = read_from_file("def.pst.tsv")
def_imp_list = read_from_file("def.imp.tsv")
indef_imp_list = read_from_file("indef.imp.tsv")


# ### Первый тип предложения

# In[ ]:


# 1. Egy pontos disznó a nemzeti ünnepen ebédelt a strandon és után bulizott a komoly bátyával a belvárosban.

def nominative(): # csiga
    """ Возвращает случайное  Nom.Sg """ #disznó
    return random.choice(nom_list)

def instumental():
    """ Возвращает случайное Instr.Sg  """ #bátyával
    return random.choice(inst_list)

def adjective(nom): # a buta csiga
    """ Возвращает случайную пару adj + noun """ #pontos disznó
    return random.choice(adj_list) + " " + nom

def time(np):
    """ Возвращает adj + noun + time """ #pontos disznó a nemzeti ünnepen
    return np + " " + random.choice(when_list)

def locative():
    """ Возвращает location """ #strandon
    return random.choice(where_list) 

def verb(where): 
    """ Возвращает verb + location """ #ebédelt strandon
    return random.choice(indef_pst_list) + " " + where

def random_sentence():
    sentence = "Egy" + " " + time(adjective(nominative())) + " " + verb("a" + " " + locative()) + " és után "    + verb("a" + " " + adjective(instumental())) + " " + "a" + " " + locative() + "."
    return sentence


# ## Второй тип предложения

# In[ ]:


# 2. Mikortól teátezett a strandon a büszke macska a karácsonyon?

def question(vp):
    """ Возвращает вопросительное местоимение + VP""" #Mikortól teátezett...
    return random.choice(question_list) + " " + vp

def random_question():
    question_sentence = question(verb("a" + " " + locative())) + " " + time("a" + " " + adjective(nominative())) + "?"
    return question_sentence


# ## Третий тип предложения

# In[ ]:


# 3. A barátságos tengerimalac nem találta sünöt a vidámparkban az ő születésnapján.

def accusative():
    """ Возвращает случайное  Acc.Sg """ #sünöt
    return random.choice(acc_list)

def def_verb(np):
    """ Возвращает глагол + NP """ #nem találta ...
    return "nem" + " " + random.choice(def_pst_list) + " " + np 

def random_negative():
    negative_sentence = "A " + adjective(nominative()) + " " + def_verb(time(accusative())) + "."
    return negative_sentence


# ## Четвертый тип предложения

# In[ ]:


# 4. Ha a szigorú ló vásárolt volna a Duna parton a nemzeti ünnepen,
# egy szorgalmas kutya a húsvét héten vacsorázott volna a színházban

def random_conditional():
    conditional_sentence = "Ha a" + " " + adjective(nominative()) + " " + verb("volna" + " " +    time("a" + " " + locative())) + "," + " " + time("egy" + " " + adjective(nominative())) + " " +    verb("volna" + " " + "a" + " " + locative()) + "."
    return conditional_sentence


# ## Пятый тип предложения

# In[ ]:


# 5. Ne egyél oroszlánot és ne rajzold a pontos szarvast!

def indef_imp(obj):
    """ Возвращает императивную безобъектную форму глагола + неопределенный объект """ #Ne egyél oroszlánot
    return "Ne" + " " + random.choice(indef_imp_list) + " " + obj

def def_imp(def_obj):
    """ Возвращает императивную объектную форму глагола + определенную NP """ #ne rajzold a pontos szarvast
    return "ne" + " " + random.choice(def_imp_list) + " " + def_obj

def random_imperative():
    imperative_sentence = indef_imp(accusative()) + " " + "és" + " " + def_imp("a" + " " + adjective(accusative())) + "!"
    return imperative_sentence


# In[ ]:


def main():
    sentences = [random_imperative(), random_conditional(), random_negative(), random_question(), random_sentence()]
    for i in range(len(sentences)):
        random_index = random.randrange(len(sentences))
        print(sentences.pop(random_index), sep = " ", end = " ")
    return 0


# In[ ]:


if __name__ == '__main__':
    main()

