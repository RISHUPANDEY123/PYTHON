import re
pattern = [abc]
string = 'ahyss'
result = re.match(pattern,string)
if result:
  print("Search successful")
else:
  print("Search unsuccessful")	
