"""

-problem
---
---


-logic
1 splitting sentences 
    every dot is the end for the sentence. and we will split from there



2 handling sentences
    functions will control every sentence and fix 

then ""join(list_of_sentences)


"""
def sentenceVerification(sentence):
    """sentence has to have space before starting except first sentence"""
    s = []
    for i in sentence[first_letter_ident(sentence):]:
        s.append(i)
    
    for i in s:
        if str(i).isalpha():    
            
            s[s.index(i)] = i.upper()
            break

        else:
            
            s.remove(i)


    return "".join(s)+". "

def first_letter_ident(word):
    """that return index of first letter in string"""
    x = 0
    for i in word:
        if str(i).isalpha():
           return x
        else:
            x +=1
    return False    

paragraph ="***********Paragraphs are the building blocks of papers.many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc.In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph.A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph."
list_of_sentences=paragraph.split(".")


a=0
for i in list_of_sentences:
    if i =="":
        del i 
        continue
    list_of_sentences[a] = sentenceVerification(i)
    a=a+1
    
verificated = "".join(list_of_sentences)    
print(verificated)