def IsPalindrone(product):
  if str(product) == str(product)[::-1]:
    return product

def LargestPalindrone():
  Max=0
  for i in range(100,1000):
    for j in range(i,1000):
      product = i*j
      if IsPalindrone(product) and product > Max:
        Max = product
  return Max

result = LargestPalindrone()
print(result)
