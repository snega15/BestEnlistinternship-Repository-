Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> List=[34,64,43,79,24334,8096,3536,69878]
>>> List.append(34)
>>> print(List)
[34, 64, 43, 79, 24334, 8096, 3536, 69878, 34]
>>> List.remove(79)
>>> print(List)
[34, 64, 43, 24334, 8096, 3536, 69878, 34]
>>> List.sort()
>>> print(List[-1])
69878
>>> print(List[1])
34
>>> Tuble=(4365,54,5897,"dhg")
>>> Tuble=Tuble[::-1]
>>> print(Tuble)
('dhg', 5897, 54, 4365)
>>> tup=[(1,2),(3,6),(34,76)]
>>> out=list(sum(tup,()))
>>> print(out)
[1, 2, 3, 6, 34, 76]
>>> 