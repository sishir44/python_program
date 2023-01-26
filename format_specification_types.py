'''syntax:
    "{position:format_specification}"

1. Alignment = right(>), left(<), center(^)
2. Presentation = f-(fixed point notation), e-(exponent notation)
3. Conversion = '''

s1= "{0:*>10}".format(999)
print(s1)

s2= "{0:*<10}".format(999)
print(s2)

s3= "{0:*^10}".format(999)
print(s3)