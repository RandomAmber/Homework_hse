
# coding: utf-8

# In[1]:


import os
import re


# In[2]:


def count_dir_with_the_same_format_files(dirs): #6
    count = 0
    for dir in dirs:
        files = os.listdir(dir)
        formats = []
        for file in files:
            if not os.path.isdir(file):
                formats.append(file[file.rfind('.'):])
        if len(formats) != len(set(formats)):
            count += 1
    return count


# In[3]:


def deep(dir_names): #1
    deep = []
    for name in dir_names:
        deep.append(len(name.split('/')))
    return max(deep)


# In[54]:


def get_bigger_dir(file_names): #7
    files = []
    for file in file_names:
        files.append(file[:file.rfind('/')])
    files = {files.count(key):key for key in set(files)}
    result = files[max(files.keys())]
    if result == '.':
        return ", в которой находится данная программа"
    else:
        return files[max(files.keys())]


# In[5]:


def get_cyrillic_dirs(dirs): #2
    cyrillic_dirs = []
    for d in dirs:
        if d.split('/')[-1] == "".join(re.findall('[а-яА-Я]', d.split('/')[-1])):
            cyrillic_dirs.append(d)
    return cyrillic_dirs


# In[6]:


def get_all_dir_start_with(dirs, s): #5
    starts_dir = []
    for dir in dirs:
        if dir.split('/')[-1].startswith(s):
            starts_dir.append(dir)
    return starts_dir

def unique_file_names(dirs): #5
    unique_files = []
    for dir in dirs:
        files = os.listdir(dir)
        for file in files:
            if not os.path.isdir(file):
                unique_files.append(file[file.rfind('/')+1:])
    return len(set(unique_files))
                


# In[7]:


def freq_dir_start(dirs):#4
    start = []
    for dir in dirs:
        s = dir[dir.rfind('/')+1:][0]
        if s.isalpha():
            start.append(s)
    start = {start.count(key):key for key in set(start)}
    return start[max(start.keys())]


# In[69]:


def freq_format(dirs): #3
    file_names = []
    for dir in dirs:
        files = os.listdir(dir)
        for file in files:
            if os.path.isfile(file):
                file_names.append(file)
    formats = []
    for name in file_names:
        form = os.path.basename(name).split('.')[-1]
        if form != os.path.basename(name):
            formats.append(os.path.basename(name).split('.')[-1])
    formats = {formats.count(key):key for key in set(formats)}
    return formats[max(formats.keys())]


# In[65]:


def walk(dir_name='.', files=[], dirs=[]):
    for file in os.listdir(dir_name):
        if os.path.isdir(dir_name + '/' + file):
            dirs.append(dir_name + '/' + file)
            walk(dir_name + '/' + file, files, dirs)
        else:
            files.append(dir_name + '/' + file)
    return set(files), set(dirs)


# In[70]:


def main():
    with open("result.txt", "w+") as file:
        file.write("Сейчас мы здесь: {}.\n".format(os.getcwd()))
        files, dirs = walk()
        max_depth = deep(dirs) - 1
        file.write("Максимальная глубина папки в этом дереве равна {}.\n".format(max_depth))
    
        cyrillic_dirs = get_cyrillic_dirs(dirs)
        count_cyrillic_dirs = len(cyrillic_dirs)
        file.write("Папок с полностью кириллическими названиями в этом дереве {}.\n".format(count_cyrillic_dirs))
    
        if count_cyrillic_dirs == 0:
            file.write("Папок с полностью кириллическими названиями в этом дереве нет, поэтому мы не можем сказать ничего про частоту встречаемости каких-либо файлов :(\n")
        else:
            freq = freq_format(cyrillic_dirs)
            file.write("Чаще всего в этих папках встречаются файлы с расширением {}.\n".format(freq))
    
        freq_start = freq_dir_start(dirs)
        file.write("Название большинства папок начинается на -{}.\n".format(freq_start))
    
        starts_dirs = get_all_dir_start_with(dirs, freq_start)
        unique_file_names_count = unique_file_names(starts_dirs)
        file.write("В папках, название которых начинается на -{}, количество разных названий файлов без учета расширений равно {}.\n".format(freq_start, unique_file_names_count))
    
        c = count_dir_with_the_same_format_files(dirs)
        file.write("В {} папках встречается несколько файлов с одинаковым расширением.\n".format(c))
    
        bigger_dir = get_bigger_dir(files)
        file.write("Больше всего файлов лежит в папке {}.".format(bigger_dir))
    


# In[71]:


main()

