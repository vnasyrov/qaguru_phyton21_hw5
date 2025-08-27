from selene import browser, have, command, be

def test_submit_form():
    browser.config.timeout = 2
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    browser.open('https://demoqa.com/automation-practice-form')
    browser.element("#firstName").type('Валерий').press_enter()
    browser.element("#lastName").type('Насыров').press_enter()
    browser.element("#userEmail").type('user@example.com').press_enter()
    browser.element('label[for="gender-radio-1"]').click()
    browser.element("#userNumber").type('8999999999').press_enter()

    # Дата рождения
    #browser.element("#dateOfBirthInput").type('12 Jul 1993').press_enter()
    browser.element('#dateOfBirthInput').perform(command.js.click)
    browser.element('.react-datepicker__month-select').element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="1993"]').click()
    browser.element('.react-datepicker__day--012').perform(command.js.click)

    # Subjects. Клик по контейнеру, чтобы поле стало активным
    browser.element('.subjects-auto-complete__input').perform(command.js.click)
    # Subjects. Ввести текст через внутренний input
    browser.element('.subjects-auto-complete__input input').type('Python').press_enter()

    # Hobbies
    browser.element('label[for="hobbies-checkbox-1"]').perform(command.js.click)

    # Current Address
    browser.element("#currentAddress").type('Los Angeles').press_enter()
pass