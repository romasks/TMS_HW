# Дан список строк. С помощью filter() получить 
# список тех строк из исходного списка, 
# которые являются палиндромами 
# (читаются в обе стороны одинаково, например, ’abcсba’).

words = ["abccba", "apple", "довод", "bob", "random"]
print(words)

palindroms = [word for word in words if word == word[::-1]]
print(palindroms)