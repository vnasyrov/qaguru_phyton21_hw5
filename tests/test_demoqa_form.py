from selene import browser, have

def test_demoqa_form():
    # Настройка браузера
    browser.config.timeout = 6
    # Открываем форму
    browser.open('https://demoqa.com/automation-practice-form')
    # Основные поля
    browser.element("#firstName").type('Valeriy')
    browser.element("#lastName").type('Nasyrov')
    browser.element("#userEmail").type('user@example.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element("#userNumber").type('9999999999')
    # Дата рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="1993"]').click()
    browser.element('.react-datepicker__day--012').click()
    # Subjects
    browser.element('#subjectsInput').type('Python').press_enter()
    # Hobbies
    browser.element('label[for="hobbies-checkbox-1"]').click()
    # Picture
    browser.element('#uploadPicture').set_value('/Users/user/Desktop/Снимок экрана 2025-08-03 в 20.17.57.png')
    # Current Address
    browser.element("#currentAddress").type('Los Angeles')
    # State
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    # City
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    # Submit
    browser.element('#submit').click()

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(

        'Valeriy Nasyrov',
        'user@example.com',
        'Male',
        '9999999999',
        '12 July,1993',
        'Python',
        'Sports',
        '/Users/user/Desktop/Снимок экрана 2025-08-03 в 20.17.57.png',
        'Los Angeles',
        'NCR Delhi'
    ))