"""
Дана строка, состоящая из слов, разделенных пробелами. 
(Вот 4 варианта тестовых данных для программы: ‘Hello world’, ‘a b c’, ‘test’, ‘test1 test2 test3 test4 test5’). 
Определите, сколько в ней слов.
"""

test_str_1 = "Hello world"
test_str_2 = "a b c"
test_str_3 = "test"
test_str_4 = "test1 test2 test3 test4 test5"

print("Number of words in 1st string: ", len(test_str_1.split(" ")))
print("Number of words in 2nd string: ", len(test_str_2.split(" ")))
print("Number of words in 3rd string: ", len(test_str_3.split(" ")))
print("Number of words in 4th string: ", len(test_str_4.split(" ")))