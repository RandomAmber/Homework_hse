
# coding: utf-8

# In[ ]:


def main():
    sentences = [random_imperative(), random_conditional(), random_negative(), random_question(), random_sentence()]
    with open('text.txt', 'w') as f:
        for i in range(len(sentences)):
            f.write(random.choice(sentences))
    return 0

if __name__ == '__main__':
    main()

