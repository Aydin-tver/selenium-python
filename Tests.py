from MainPage import MainPage

def test_about(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_about_button()
    title = tages_main_page.check_title()
    assert "ВАШ ТЕХНОЛОГИЧЕСКИЙ ПАРТНЕР" in title.text

def test_academy(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_academy_button()
    title = tages_main_page.check_title()
    assert "TAGES ACADEMY" in title.text

def test_events(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_events_button()
    title = tages_main_page.check_title()
    assert "TAGES МЕРОПРИЯТИЯ" in title.text

def test_blog(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_blog_button()
    title = tages_main_page.check_title()
    assert "Блог" in title.text

def test_vacancies(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_vacancies_button()
    title = tages_main_page.check_title()
    assert "#ДАВАЙСРАБОТАЕМСЯ" in title.text

def test_contacts(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_contacts_button()
    title = tages_main_page.check_title()
    assert "Контакты" in title.text

def test_tages_phone(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_phone_field()

def test_tages_mail(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_mail_field()

def test_tages_partners(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_partners_field()

def test_click_confidential(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_confident_field()

def test_tages_telegram_link(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.click_telegram_link_field()

def test_mail_check(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.paste_name("Константин")
    tages_main_page.paste_form_input("999 999 99 99", 1)
    tages_main_page.paste_form_input("КомпанияТест", 2)
    tages_main_page.paste_form_input("test", 3)
    tages_main_page.paste_form_input("КомментарийТест", 4)    
    assert tages_main_page.check_invisible_confirmation()

def test_mail_check(browser):
    tages_main_page = MainPage(browser)
    tages_main_page.open_site()
    tages_main_page.paste_name("Константин")
    tages_main_page.paste_form_input("999 999 99 99", 1)
    tages_main_page.paste_form_input("КомпанияТест", 2)
    tages_main_page.paste_form_input("test@gmail.com", 3)
    tages_main_page.paste_form_input("КомментарийТест", 4)
    tages_main_page.click_send_button()

