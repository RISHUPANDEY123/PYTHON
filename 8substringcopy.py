def substring_copy(str, n):
  flen = 7
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 6))
print(substring_copy('p', 3));

