
def get_max(l,k):
  l1 = []
  for item in l:
    l1.append(item[k])
  i_max = index(max(l1))
  item_max = l[i_max]
  return item_max
def get_top(l,k,n)
  l1 = []
  for item in l:
    l1.append(item)
  l_top =[]
  for i in range(n):
    i_max = get_max(l1,k)
    l_top.append(i_max)
    l1.remove(i_max)
  return l_top
def count_item(l1,l2,k):
  ci = 0
  for i in l1[k]:
    if i in l2[k]:
      ci += 1
  return ci
def arrange(l,k):
  l1 = []
  for item in l:
    l1.append(item)
  l_arr =[]
  for i in len(l):
    i_max = get_max(l1,k)
    l_arr.append(i_max)
    l1.remove(i_max)
  return l_arr
def get_point(i1,i2):
  if i1["gender"] == male:
    if i1["age"] - i2["age"] > 2:
      p = 0
    else:
      if (i1["age"] - i2["age"]) in [1,2,4]:
        p1 = 1
      elif i1["age"] == i2["age"]:
        p1 = 0.5
      else:
        p1 = 0
      p2 = 72 - abs(i1["city_point"] - i2["city_point"])
      p3 = min(3, count_item(i1,i2,"hobby")
      p = p1*30 + p2*30/72 + p3*40/3
  else:   
    if i1[age] - i2[age] < -2:
      p = 0
    else: 
      if (i2["age"] - i1["age"]) in [1,2,4]:
        p1 = 1
      elif i1["age"] == i2["age"]:
        p1 = 0.5
      else:
        p1 = 0
      p2 = 72 - abs(i1["city_point"] - i2["city_point"])
      p3 = min(3, count_item(i1,i2,"hobby")
      p = p1*30 + p2*30/72 + p3*40/3
  return p
def suggest(item,l):
  l_p = []
  for i,it in enumerate(l):
    point = get_point(item,i)
    l_p.append({"index": i; "point": point})
  list_arr = arrange(l_p,"point")
  list_sugg = []
  for i in list_arr:
    idx = i["index"]
    list_sugg.append(l[i])
  return list_sugg
    
    
  
 
    
  
