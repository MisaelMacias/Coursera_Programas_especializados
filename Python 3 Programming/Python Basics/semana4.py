#Currently there is a string called str1. Write code to create a list called chars 
#which should contain the characters from str1. Each character in str1 should be 
#its own element in the list chars.

str1 = "I love python"
# HINT: what's the accumulator? That should go here.

chars = []
for i in str1:
    a = i
    chars.append(a)
print(chars)

#For each character in the string saved in ael, append that character to a list 
#that should be saved in a variable app.

ael = "python!"
app = []
for i in ael:
    app.append(i)

#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). 
#Save these past tense words to a list called past_wrds.




wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for i in wrds:
    a = i + "ed"
    b = past_wrds.append(a)
print(b) 

#variable acro. The first two letters of each word should be used, each letter in the 
#acronym should be a capital letter, and each element of the acronym should be separated 
#by a “. ” (dot and space). Words that should not be included in the acronym are stored 
#in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” 
#then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

sent2=sent.split()

acro=''

for word in sent2:
    if word not in stopwords:
        acro=acro+word[0].upper()+word[1].upper()+'. '
        

acro=acro[:-2]

print(acro)

#A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks 
#if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal 
#to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we 
#can check your work.

p_phrase = "was it a car or a cat I saw"

r_phrase=''

for char in p_phrase:
    r_phrase=char+r_phrase
    
print(r_phrase)
print(r_phrase==p_phrase)

#Provided is a list of data about a store’s inventory where each item in the list represents 
#the name of an item, how much is in stock, and how much it costs. Print out each item in the 
#list with the same formatting, using the .format method (not string concatenation). 
#For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


for item in inventory:
    print("The store has {} {}, each for {} USD.".format(item.split(', ')[1],item.split(', ')[0],item.split(', ')[2]))