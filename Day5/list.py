empty_list = list();
print(len(empty_list));

# List of fruits
fruits = ['banana','apple','orange','mango','apple'];
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'];

print("Fruits : ", fruits);
print("Vegetables : ", vegetables)

# Modifying list
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0];
print(first_fruit);
# last fruit
last_fruit = len(fruits) -1;
print(fruits[last_fruit]);

# Slicing Items 
all_fruits = fruits[0:4];
all_fruits = fruits[0:];
orange_and_mango = fruits[1:3];
print(all_fruits, orange_and_mango);

# Checking Items
does_exists = 'banana' in fruits;
print(does_exists);

# Append
fruits.append('lime');
fruits.append('kiwi');
print(fruits);

# insert
fruits.insert(2, 'kiwi');
print(fruits);

# remove
fruits.remove('kiwi');

# del -> removes particular index
del fruits[0];

# clear -> removes all elemnets
# fruits.clear();

# copying a list
fruits_copy = fruits.copy();
print(fruits_copy);

# join
positive_number = [1,2,3,4,5];
zero = [0]
negative_number = [-5,-4,-3,-2,-1];
integers = negative_number + zero + positive_number;
print(integers);

# join with extend
num1 = [0,1,2,3];
num2 = [4,5,6];
num1.extend(num2);
print(num1)

# count -> count the instanses in a list
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24)) 


# index -> used to find the index
print(fruits.index('orange'));

# reverse -> reverse the list
# fruits.reverse();
print(fruits);


# sort 
# fruits.sort();
alphabets = ['b','a','c'];
alphabets.sort(reverse=True) #it modifies the original list directly and does not create a new one. If the list contains strings, it will sort them in reverse alphabetical order (Z to A)

print(alphabets);