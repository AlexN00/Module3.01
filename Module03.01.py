calls = 0
def count_calls():
  global calls
  calls += 1
def  string_info():
    string= input('')
    print(len(string),string.upper(),string.lower())
    count_calls()
def  is_contains():
    print('Введите слово: ')
    string=input('').lower()
    print('Напишите список, чтобы узнать есть ли там ваше слово: ')
    list_to_search=input().lower()
    print(string.lower() in str(list_to_search.lower()))
    count_calls()

string_info()
string_info()
is_contains()
is_contains()
print(calls)



