'''
There are 3 rules for a valid string:

An empty string is valid
You can add same character to a valid string X, and create another valid string yXy
You can concatenate two valid strings X and Y, so XY will also be valid.
Ex: vv, xbbx, bbccdd, xyffyxdd are all valid.
'''

def ValidCoupon(coupon):
  let stack=[];
  for i in range(len(coupon)):
    if stack.length==0 or coupon[i]!=stack[len(stack)-1]:
      stack.append(coupon[i]) 
    else:
      stack.pop()
  
  if not stack:
    return 1
 
  return 0 
 
 