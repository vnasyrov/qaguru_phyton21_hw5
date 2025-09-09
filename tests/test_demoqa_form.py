from selene import browser, have

def test_demoqa_form():
    # Настройка браузера
    browser.config.timeout = 2
    # Открываем форму
    browser.open('https://demoqa.com/automation-practice-form')

    # Убираем баннер и футер, мешающие кнопке Submit
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

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
    browser.element('#subjectsInput').type('Maths').press_enter()
    # Hobbies
    browser.element('label[for="hobbies-checkbox-1"]').click()
    # Picture
    browser.element('#uploadPicture').set_value('/Users/user/Desktop/logo.jpg')
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
        'Maths',
        'Sports',
        'logo.jpg',
        'Los Angeles',
        'NCR Delhi'
    ))