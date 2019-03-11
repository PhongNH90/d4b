def bo_dau(s):
  s1 = s.lower()
  s1 = s1.replace("à","a")
  s1 = s1.replace("á","a")
  s1 = s1.replace("ả","a")
  s1 = s1.replace("ã","a")
  s1 = s1.replace("ạ","a")
  s1 = s1.replace("ă","a")
  s1 = s1.replace("ằ","a")
  s1 = s1.replace("ắ","a")
  s1 = s1.replace("ẳ","a")
  s1 = s1.replace("ẵ","a")
  s1 = s1.replace("ặ","a")
  s1 = s1.replace("â","a")
  s1 = s1.replace("ầ","a")
  s1 = s1.replace("ấ","a")
  s1 = s1.replace("ẩ","a")
  s1 = s1.replace("ẫ","a")
  s1 = s1.replace("ậ","a")
  s1 = s1.replace("ò","o")
  s1 = s1.replace("ó","o")
  s1 = s1.replace("ỏ","o")
  s1 = s1.replace("õ","o")
  s1 = s1.replace("ọ","o")  
  s1 = s1.replace("ô","o")
  s1 = s1.replace("ồ","o")
  s1 = s1.replace("ố","o")
  s1 = s1.replace("ổ","o")
  s1 = s1.replace("ỗ","o")
  s1 = s1.replace("ộ","o")
  s1 = s1.replace("ơ","o")
  s1 = s1.replace("ờ","o")
  s1 = s1.replace("ớ","o")
  s1 = s1.replace("ở","o")
  s1 = s1.replace("ỡ","o")
  s1 = s1.replace("ợ","o")
  s1 = s1.replace("è","e")
  s1 = s1.replace("é","e")
  s1 = s1.replace("ẻ","e")
  s1 = s1.replace("ẽ","e")
  s1 = s1.replace("ẹ","e")  
  s1 = s1.replace("ê","e")
  s1 = s1.replace("ề","e")
  s1 = s1.replace("ế","e")
  s1 = s1.replace("ể","e")
  s1 = s1.replace("ễ","e")
  s1 = s1.replace("ệ","e")
  s1 = s1.replace("ù","u")
  s1 = s1.replace("ú","u")
  s1 = s1.replace("ủ","u")
  s1 = s1.replace("ũ","u")
  s1 = s1.replace("ụ","u")  
  s1 = s1.replace("ư","u")
  s1 = s1.replace("ừ","u")
  s1 = s1.replace("ứ","u")
  s1 = s1.replace("ử","u")
  s1 = s1.replace("ữ","u")
  s1 = s1.replace("ự","u")
  return s1
def get_max(l,k):
  l1 = []
  for item in l:
    if item[k] != None:
      l1.append(item[k])
    else:
      l1.append(0)
  i_max = l1.index(max(l1))
  item_max = l[i_max]
  return item_max
def get_top(l,k,n):
  l1 = []
  for item in l:
    l1.append(item)
  l_top =[]
  for i in range(n):
    item_max = get_max(l1,k)
    l_top.append(item_max)
    l1.remove(item_max)
  return l_top
def count_item(l1,l2,k):
  ci = 0
  l_1 = []
  l_2 = []
  for i in l1[k]:
    i1 = bo_dau(i)
    l_1.append(i1)
  for i in l2[k]:
    i1 = bo_dau(i)
    l_2.append(i1)
  for i in l_1:
    if i in l_2:
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
  if i1["gender"] == "male":
    if i1["age"] - i2["age"] > 2:
      p = 0
    else:
      if (i1["age"] - i2["age"]) in [1,2,4]:
        p1 = 1
      elif i1["age"] == i2["age"]:
        p1 = 0.5
      else:
        p1 = 0
      if (i1["city"],i2["city"]) in region["Bắc"] or (i1["city"],i2["city"]) in region["Trung"] or (i1["city"],i2["city"]) in region["Nam"]:
        p2 = 1
      else:
        p2 = 0
      p3 = min(3, count_item(i1,i2,"hobby"))
      p = p1*3 + p2*2 + p3*5/3
  else:   
    if i1["age"] - i2["age"] < -2:
      p = 0
    else: 
      if (i2["age"] - i1["age"]) in [1,2,4]:
        p1 = 1
      elif i1["age"] == i2["age"]:
        p1 = 0.5
      else:
        p1 = 0
      p3 = min(3, count_item(i1,i2,"hobby"))
      p = p1*3 + p2*2 + p3*5/3
  return p
def suggest(item,l):
  l_p = []
  for i,it in enumerate(l):
    point = get_point(item,i)
    x = {"index": i, "point": point}
    if x["id"] not in item["follow_list"]:
      l_p.append(x)
  list_arr = arrange(l_p,"point")
  list_sugg = []
  for i in list_arr:
    idx = i["index"]
    list_sugg.append(l[i])
  return list_sugg
def search(l,v):
  va = bo_dau(v)
  search_list = []
  for i in l:
    n = bo_dau(i["name"])
    if n == va:
      search_list.append(place_img(i))
  return search_list
def place_img(u):
  if u["img"] == None:
    if u["gender"] == "female":
      u["img"] = "static/girl.png"
    else:
      u["img"] = "static/boy.png"
  return u
def place_stt(u):
  if u["stt"] == None:
    u["stt"] = "Đang buồn đang chán, ai tán yêu luôn!!!"
  return u    

region = {
  "Bắc" :  ["Lào Cai", "Yên Bái", "Điện Biên", "Hoà Bình", "Lai Châu", "Sơn La", "Hà Giang", "Cao Bằng", "Bắc Kạn", "Lạng Sơn", "Tuyên Quang", "Thái Nguyên", "Phú Thọ", "Bắc Giang", "Quảng Ninh", "Bắc Ninh", "Hà Nam", "Hà Nội", "Hải Dương", "Hải Phòng", "Hưng Yên", "Nam Định", "Ninh Bình", "Thái Bình", "Vĩnh Phúc"],
  "Trung" : ["Thanh Hoá", "Nghệ An", "Hà Tĩnh", "Quảng Bình", "Quảng Trị", "Thừa Thiên-Huế", "Đà Nẵng", "Quảng Nam", "Quảng Ngãi", "Bình Định", "Phú Yên", "Khánh Hoà", "Ninh Thuận", "Bình Thuận", "Kon Tum", "Gia Lai", "Đắc Lắc", "Đắc Nông", "Lâm Đồng"],
  "Nam" : ["Bình Phước", "Bình Dương", "Đồng Nai", "Tây Ninh", "Bà Rịa-Vũng Tàu", "TP HCM", "Long An", "Đồng Tháp", "Tiền Giang", "An Giang", "Bến Tre", "Vĩnh Long", "Trà Vinh", "Hậu Giang", "Kiên Giang", "Sóc Trăng", "Bạc Liêu", "Cà Mau", "Cần Thơ"]

}
def check_username(n):
  if User.objects(name) != None:
    fl = "Username exist"
  else if isalnum