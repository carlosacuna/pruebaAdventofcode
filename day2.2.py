text = open('./day2.txt')
total = 0
for lines in text:
    l, w, d = lines.split('x')
    l, w, d = int(l), int(w), int(d)    
    r= min(l+l+w+w, l+l+d+d, w+w+d+d)
    b = l * w * d
    total += (r + b)
print("Result:  needed", total, "MTS")
