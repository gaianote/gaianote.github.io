# sort与sorted

```python
>>> a = ["1","2","3","a","Z","5"]
>>>
>>> a.sort()
>>> a
['1', '2', '3', '5', 'Z', 'a']
# 通过true和false来实现更精准的排序,让数字拍在字母后面
>>> a.sort(key=lambda x:(x.isdigit(),x)) 
>>> a
['Z', 'a', '1', '2', '3', '5']
# 通过true和false来实现更精准的排序,让数字拍在字母后面并且让小写字母排在大写字母前
>>> a.sort(key=lambda x:(x.isdigit(),not x.islower(),x))
>>> a
['a', 'Z', '1', '2', '3', '5']
```