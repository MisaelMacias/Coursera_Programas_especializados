#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.

letters = "alwnfiwaksuezlaeiajsdl"
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse = True)
print(sorted_letters)

#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals_sorted = sorted(animals)
print(animals_sorted)

#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. 
#Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

alphabetical = sorted(medals)
print(alphabetical)

#Given the same dictionary, medals, now sort by the medal count. Save the three countries with 
#the highest medal count to the list, top_three.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

def g(k,d):
    return d[k]
top_three = sorted(medals, reverse = True, key = lambda x:g(x, medals))[:3]
print(top_three)

#We have provided the dictionary groceries. You should return a list of its keys, but they should 
#be sorted by their values, from highest to lowest. Save the new list as most_needed.

most_needed = []
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15,
             'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
def g(k,d):
    return d[k]
most_needed = sorted(groceries, reverse = True, key = lambda x: g(x, groceries))

#Create a function called last_four that takes in a single ID number and returns the last four digits. 
#For example, the number 17573005 should return 3005. Then, use the resulting function to sort the 
#list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, 
#sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.

def last_four(x):
    return str(x)[-4:]


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key = last_four)
print(sorted_ids)

#Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. 
#Save this sorted list in the variable sorted_id.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key = lambda x: str(x)[-4:])
print(sorted_id)

#Sort the following list by each element’s second letter a to z. Do so by using lambda. 
#Assign the resulting value to the variable lambda_sort.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key = lambda x: x[1])

#We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv 
#file named project_twitter_data.csv which has the text of a tweet, the number of retweets 
#of that tweet, and the number of replies to that tweet. We have also words that express 
#positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
#Your task is to build a sentiment classifier, which will detect how positive or negative each 
#tweet is. You will create a csv file, which contains columns for the Number of Retweets, 
#Number of Replies, Positive Score (which is how many happy words are in the tweet), 
#Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. 
#At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
#To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, 
#and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    
    for char in string:
        if char in punctuation_chars:
            string=string.replace(char,"")

    return string

#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, 
#a string which represents one or more sentences, and calculates how many words in the string are considered positive words. 
#Use the list, positive_words to determine what words will count as positive. 
#The function should return a positive integer - how many occurrences there are of positive words in the text. 
#Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string 
#to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(string):
    
    for char in string:
        if char in punctuation_chars:
            string=string.replace(char,"")

    return string  

def get_pos(x):
    c=0
    words=x.split()
    for word in words:
        word= strip_punctuation(word)
        if word in positive_words:
            c=c+1
    return c

#Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, 
#a string which represents one or more sentences, and calculates how many words in the string are considered negative words. 
#Use the list, negative_words to determine what words will count as negative. 
#The function should return a positive integer - how many occurrences there are of negative words in the text. 
#Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string 
#to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(string):
    
    for char in string:
        if char in punctuation_chars:
            string=string.replace(char,"")

    return string  

def get_neg(sentence):
    
    count=0
    
    for string in sentence.split(" "):
        if strip_punctuation(string) in negative_words:
            count+=1
    
    return count

#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which 
#has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, 
#and the number of replies to that tweet). Your task is to build a sentiment classifier, 
#which will detect how positive or negative each tweet is. Copy the code from the code windows above, 
#and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, 
#which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), 
#Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) 
#for each tweet. The file should have those headers in that order. Remember that there is another component to this project. 
#You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. 
#Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_pos(x):
    c=0
    words=x.split()
    for word in words:
        word= strip_punctuation(word)
        if word in positive_words:
            c=c+1
    return c

def get_neg(x):
    c=0
    words=x.split()
    for word in words:
        word= strip_punctuation(word)
        if word in negative_words:
            c=c+1
    return c

def strip_punctuation(s):
    for x in s:
        if x in punctuation_chars:
            s = s.replace(x, "")
    return s

outfile = open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')


fileconnection = open("project_twitter_data.csv", 'r')

lines = fileconnection.readlines()
print(lines)
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    
    vals = row.strip().split(',')
    row_string = '{},{},{},{},{}'.format(vals[1],vals[2],get_pos(vals[0]),get_neg(vals[0]),get_pos(vals[0])-get_neg(vals[0]))
    outfile.write(row_string)
    outfile.write('\n')


outfile.close()