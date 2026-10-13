# dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Syntax
empty_dict = {};
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# Accessing dictonary items
print(dct['key1']);
print(person['first_name']); # Asavebeh

# Adding items to a dictionar
dct['key5'] = 'value5'

# Modifying items in a dictionary
dct['key1'] = 'value-one';

# Checking keys in Dictionary
print('key2' in dct);
print('key5' in dct);

# Removing key and value pair from a dictonary
# pop(key) : removes the items with the specified key name:
# popitem() : removes the last item
# del : removes an item with specified key name

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item


# Chaning dictionary to a list of items
print(dct.items());

# Clearing a dictonary
print(dct.clear()) # None

# Deleting a dictionary
del dct;

# copying a dictionary
dct_copy = dct.copy();
