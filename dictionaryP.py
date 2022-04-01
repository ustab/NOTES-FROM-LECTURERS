'''
#1-iki listeyi dictionary haline getirelim
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#print(dict1)
zip(keys, values)
#dict1=dict(['Ten', 'Twenty', 'Thirty'],[10, 20, 30])
dict1=dict(zip(keys, values))# keys and values liste icini yazmiyoruz sadece
# keys and values olarak yazmak gerekiyor
print(dict1)

#second solution update() metodudur.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1=dict()
#for i in range(len(keys)):
for i in range(len(keys)):
    dict1.update({keys[i]: values[i]})
print(dict1)

#2.soru merge two dictionaries

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#dictm=dict1.update({'Thirty': 30, 'Fourty': 40, 'Fifty': 50})
#print(dictm)
# sampl:d1.update({'e': 50, 'f': 60}) dogru yol bu olmali ama sonuc none olarak cikiyor
#oteki yol soyle:dictmerge={**dict1, **dict2}
dictm={**dict1, **dict2}
print(dictm)
#other version;iki liste icinde tarafsiz olacak ucuncu bir liste hayal ediyoruz ve listeleri bunun icinde topluyoruz
# yoksa biri digerinin yanina gitmiyor kopyasini aldigimiz dict1 artik dict degil yeni bir dictionary
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)
#soru 3 Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}
#istenen kisim marks key in icinde oldugu icin bu kisim print edilecek
print(sampleDict['class']['student']['marks']['history'])

# ogrencinin adi sorulsaydi
print(sampleDict['class']['student']['name'])
#ogrencinin fizik notu soruysaydi
print(sampleDict['class']['student']['marks']['physics'])

#soru 4 Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

#dictD=dict(**employees, **defaults) bu yol yalnis fromkeys metodu kullan.
#The fromkeys() method returns a dictionary with the specified keys and the specified value.
dictD= dict.fromkeys(employees, defaults)
print(dictD)

#soru5 Create a dictionary by extracting the keys from a given dictionary.
# Write a Python program to create a new dictionary by extracting
# the mentioned keys from the below dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
newd={i:sample_dict[i] for i in keys}

print(newd)
#cozum 2.yol:Using the update() method and loop
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# newd
newd=dict()
for i in keys:
    newd.update({i:sample_dict[i]})
print(newd)

#soru 6 Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
#del keys({sample_dict}) bu yalnis
#Solution 1: Using the pop() method and loop
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]
for i in keys:
    sample_dict.pop(i)
print(sample_dict)

#Solution 2: Dictionary Comprehension
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

sample_dict = {i: sample_dict[i] for i in sample_dict.keys() - keys}
print(sample_dict)

#soru 7 :Check if a value exists in a dictionary.dict icinde value var mi yok mu?

#Write a Python program to check if value 200 exists in the following dictionary.
#sample_dict = {'a': 100, 'b': 200, 'c': 300}
#for 200 in sample_dict.values():# burda bir hata var
   #print('present in a dict')

#Exercise 8: Rename key of a dictionary
#Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)





#Exercise 1: Convert two lists into a dictionary
#Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)
 Run
Solution 2: Using a loop and update() method of a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)
 Run
Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Show Solution
Python 3.5+

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)
 Run
Other Versions

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
 Run
Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

Expected output:

80

Show Hint
Show Solution
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# solution
print(sampleDict['class']['student']['marks']['history'])
 Run
Exercise 4: Initialize dictionary with default values

In Python, we can initialize the keys with the same values.

Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Expected output:

{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

Show Hint
Show Solution
The fromkeys() method returns a dictionary with the specified keys and the specified value.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])
 Run
Exercise 5: Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.


Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
Expected output:


{'name': 'Kelly', 'salary': 8000}
Show Hint
Show Solution
Solution 1: Dictionary Comprehension

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)
 Run
Solution 2: Using the update() method and loop

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)
 Run
Exercise 6: Delete a list of keys from a dictionary
Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
Expected output:

{'city': 'New york', 'age': 25}
Show Hint
Show Solution
Solution 1: Using the pop() method and loop

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
Solution 2: Dictionary Comprehension

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)
 Run
Exercise 7: Check if a value exists in a dictionary
We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

Write a Python program to check if value 200 exists in the following dictionary.

Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:

200 present in a dict
Show Hint
Show Solution
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')
 Run
Exercise 8: Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.

Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:

{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
Show Hint
Show Solution
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

#Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sample_dict, key=sample_dict.get))

'''

#Exercise 10: Change value of a key in a nested dictionary
#Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)





















