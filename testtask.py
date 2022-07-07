def task(array):
    return (array.find('0'))

def task2():
    import requests
    from bs4 import BeautifulSoup as bs
    import json
    import os.path


    letters = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')
    loop = True
    data = dict()
    url = r"https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D0%90"


    if not os.path.exists('animal.json'):
        print('Файла нету, ну ничего страшного сейчас создадим)')
        while loop:
            r = requests.get(url)
            
            html = bs(r.content, 'html.parser')

            for el in html.select('#mw-pages > div > div > div '):
                for el in el.select('li'):
                    title = el.get_text()
                    startswith = title[0]
                    print(title, startswith)
                    if startswith.upper() == 'A':
                        loop = False
                        break
                    data[title] = startswith
                    
                    for link in html.select('#mw-pages > a:nth-child(7)'):
                        url = r'https://ru.wikipedia.org' + link.get('href')



        with open('animal.json', 'w') as file:
            json.dump(data, file, indent= 2)
        print('Файл создан.')


    with open('animal.json', 'r') as file:
        data = json.load(file)

    result = dict()
    
    for letter in letters:
        result[letter] = (str(data.values())).count(letter)
        
    return result

def appearance(intervals):
    lesson_all = set()
    pupil_all = set()
    tutor_all = set()

    range_lesson = len(intervals['data']['lesson']) / 2 
    range_pupil = len(intervals['data']['pupil']) / 2 
    range_tutor = len(intervals['data']['tutor']) / 2

    for i in range(int(range_lesson)):
        lesson_all.update(range((intervals['data']['lesson'][i*2-2]),intervals['data']['lesson'][i*2-1])) 
        
    for i in range(int(range_pupil)):
        pupil_all.update(range((intervals['data']['pupil'][i*2-2]),intervals['data']['pupil'][i*2-1])) 

    for i in range(int(range_tutor)):
        tutor_all.update(range((intervals['data']['tutor'][i*2-2]),intervals['data']['tutor'][i*2-1])) 

    result = len(set(lesson_all & pupil_all & tutor_all))
    
    return result

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
