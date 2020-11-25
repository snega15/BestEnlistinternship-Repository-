Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d1={'a':100,'b':200}
>>> d2={'x':300,'d':400}
>>> d=d1.copy()
>>> d.update(d2)
>>> print(d)
{'a': 100, 'b': 200, 'x': 300, 'd': 400}
>>> myDict={'a':1,'b':20,'c':33}
>>> print(myDict.pop('a'))
1
>>> print(myDict)
{'b': 20, 'c': 33}
>>> keys=['red','green','blue']
>>> values=['#FF0000','#008000','#0000FF']
>>> color_dictionary = dict(zip(keys,values))
>>> print(color_dictionary)
{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
>>> seta = set([5,10,14,456,2,3,])
>>> print(len(seta))
6
>>> sn1 = {1,2,3,4,5}
>>> sn2 = {4,5,6,7,8}
>>> sn1.difference_update(sn2)
>>> print(sn1)
{1, 2, 3}
>>> 