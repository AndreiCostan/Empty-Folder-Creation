import os, locale, getpass
from datetime import date

def get_input_year():
    # Prompts the user to input an integer for the targeted year and verifies it's validity
    while True:
        try:
            user_input = int(input('Please enter an integer representing the year you wish to generate template folders for (between 1 and 9999): '))
        except ValueError:
            print('Invalid input. Please enter a valid year.')
            continue
        except KeyboardInterrupt:
            print('\nProgram interrupted. Exiting...')
            exit()

        if 1 <= user_input <= 9999:
            return user_input
        else:
            print('Input is not within the specified range. Please try again.')

def add_daily_folder_templates(target_folder, year):
    # Adds the empty template folders in the business days of the selected year
    for month in range(1,13):
        months_list.append(int(date(year, month, 1).strftime("%m")))
        month_folder_format_list.append(f'{date(year, month, 1).strftime("%m")}.{date(year, month, 1).strftime("%B").capitalize()}')
        for day in range(1,32):
            try:
                thisdate = date(year, month, day)
            except(ValueError):
                break
            if thisdate.weekday() < 5:
                days_list.append(f'{date(year, month, day).strftime("%d")}.{date(year, month, day).strftime("%m")}')
                for template in template_folders:
                    path = os.path.join(target_folder, str(year), month_folder_format_list[-1], days_list[-1], template)
                    print(f'Created Folder: {path}')
                    try:
                        os.makedirs(path, exist_ok = True)
                    except OSError as error:
                        print(f'Error!\n{error}')

locale.setlocale(locale.LC_TIME, 'ro_RO')
year = get_input_year()
target_folder = f'C:\\Users\\{getpass.getuser()}\\Desktop\\desktop target folder'
template_folders = ['folder 1', 'folder 2\\folder 2.1', 'folder 3\\folder 3.1', 'folder 3\\folder 3.2', 'folder 3\\folder 3.3']
months_list = []
month_folder_format_list = []
days_list = []
path = ''

if __name__ == '__main__':
    add_daily_folder_templates(target_folder, year)

locale.setlocale(locale.LC_TIME, 'en_EN')