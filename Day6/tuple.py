# Tuple - A tuple is a collection of different data types which is ordered and unchangeable (immutable).

# Creating a Tuple
# Syntax
empty_tuple = ();
# Using tuple constructor
empty_tuple = tuple();

# tuple with intial values
tpl = ('item1', 'item2', 'item3');
fruits = ('banana','orange', 'mango','lemon');

# Tuple Length
print(len(tpl));

# Accessing tuple values
first_item = tpl[0];
second_item = tpl[1];
print(first_item);
print(second_item);

# Slicing tuple
all_items = tpl[0:2]
all_items = tpl[-3:-1];
print(all_items)

# Changing tuple to list
lst = list(tpl);
print('item20' in tpl);

tpl1 = ('item1','item2','item3');
tpl2 = ('item4','item5','item6');
tpl3 = tpl1 + tpl2

# Deleting a tuple
# del(tpl3);
print(tpl3);