text = open('./day2.txt')
total = 0
for lines in text:
    l, w, d = lines.split('x')
    l, w, d = int(l), int(w), int(d)    
    s1 = l * w
    s2 = l * d
    s3 = w * d
    ext = min(s1, s2, s3)
    paper = 2*s1 + 2*s2 + 2*s3 + ext
    total += paper
print("Result:  needed", total, "MTS")
