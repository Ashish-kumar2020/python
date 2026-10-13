# Creating Strings

letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence);

# MultiLine string
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string);

first_name = "Ashish";
last_name = "Singh";
space = ' ';
full_name = first_name + space + last_name;
print(full_name);
print(len(first_name));
print(len(last_name));
print(len(first_name) > len(last_name));

#\n: new line
#\t: Tab means(8 spaces)
#\\: Back slash
#\': Single quote (')
#\": Double quote (")

# Escape Sequences in Strings
print('Days\tTopics\tExercise');
print('Day 1\t5\t5');
print('Day 2\t6\t20');
print('Day 3\t5\t23');
print('Day 4\t1\t35');

# Old way of formatting the string
radius = 10
pi = 3.14
area = pi * radius ** 2;
formatter_string = 'The are of circle with a radius %d is %.2f.'%(radius,area);
print(formatter_string)


# New Way of Formatting the string
formatted_string = 'The are of circle with a radius {} is {}.'.format(radius,area);
print(formatted_string);

# Unpacking Characters
language = 'Python';
a,b,c,d,e,f = language;
print(a,b,c,d,e,f);

#Accessing Characters in Strings by Index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# Slicing Python Strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Reverse a string
greeting = "Hello, world";
print(greeting[::-1])