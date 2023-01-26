# used fun : maketrans() and translate()

s = "Error 404 page not found"
table = s.maketrans("aeiou","AEIOU", "0123456789")
s_table = s.translate(table)
print(s)
print(s_table)