
# Creating an empty set
st = set();

#  Set with initial items
st = {'item1','item2','item3'};

fruits = {'banana', 'orange', 'mango', 'lemon'}

# FInd length of set
len(fruits);

# Accessing items in set
print('mango' in fruits);

# Adding items at the end
st.add('apple');

# Adding multiple items using update
fruits.update(['lime','kiwi']);

# Removing Item frorm set

# pop() removes a random item
fruits.pop(); 

# Clearing all items from set
st.clear();

# Deleting a set
del st;

# Converting list to set
lst = ['item1','item2','item3'];
st = set(lst)

# Union - combine two sets and returns a new set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) 

# Finding intersection items
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using thia : st1 & st2

# Difference between two sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1

# If two sets do not have common items we call them disjoint sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1

