test_dict = {
    'city' : 'Moscow',
    'temperature' : '20',   
}
print(test_dict['city'])
test_dict['temperature'] = str(int(test_dict['temperature']) - 5)
print(test_dict)
print(test_dict.get('country', 'Russia'))
test_dict['date'] = '27.05.2019'
print(len(test_dict))
