bad_data = ''
good_data = ''

with open('registrations.txt', 'r', encoding='utf-8') as information:
    for line in information:
        line = line.replace('\n', '')
        data = line.split()
        try:
            if len(data) != 3:
                raise IndexError
            if not data[0].isalpha():
                raise NameError
            if not '@' in data[1] or not '.' in data[1]:
                raise SyntaxError
            if not 10 <= int(data[2]) <= 99:
                raise ValueError
        except ValueError:
            print('Поле «Возраст» НЕ является числом от 10 до 99: ValueError.')
            bad_data += ''.join([line, ' ', 'Поле «Возраст» НЕ является числом от 10 до 99', '\n'])
        except SyntaxError:
            print('Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError')
            bad_data += ''.join([line, ' ', 'Поле «Имейл» НЕ содержит @ и .(точку)', '\n'])
        except IndexError:
            print('НЕ присутствуют все три поля: IndexError.')
            bad_data += ''.join([line, ' ', 'НЕ присутствуют все три поля', '\n'])
        except NameError:
            print('Поле имени содержит НЕ только буквы: NameError')
            bad_data += ''.join([line, ' ', 'Поле имени содержит НЕ только буквы', '\n'])
        else:
            good_data = ''.join([line, '\n'])

with open('registrations_good.log', 'w', encoding='utf-8') as good_file:
    good_file.write(good_data)

with open('registrations_bad.log', 'w', encoding='utf-8') as bad_file:
    bad_file.write(bad_data)
