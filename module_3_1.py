calls = int(0)
string = str(input('ввод строки ', ))

def string_info ():
    global string
    print(tuple((len(string) , string.upper() , string.lower() )))
    count_calls()

def is_contains ():
    global string
    list_to_search = ['12','46','track','armageddon', '     ' , '1111111']
    print(string in list_to_search)
    count_calls()

def count_calls ():
    global calls
    calls = + 1

string_info()
string_info()
string_info()
is_contains()
is_contains()
is_contains()
print(calls)
