from Base import BasePage
from selenium.webdriver.common.by import By

class TagesMainLocators:

    LOCATOR_TAGES_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_TAGES_ABOUT_FIELD = (By.XPATH, "//a[contains(text(),'О компании')]")
    LOCATOR_TAGES_ACADEMY_FIELD = (By.XPATH, "//a[contains(text(),'Академия')]")
    LOCATOR_TAGES_EVENTS_FIELD = (By.XPATH, "//a[contains(text(),'Мероприятия')]")
    LOCATOR_TAGES_BLOG_FIELD = (By.XPATH, "//a[contains(text(),'Блог')]")
    LOCATOR_TAGES_VACANCIES_FIELD = (By.XPATH, "//a[contains(text(),'Вакансии')]")
    LOCATOR_TAGES_CONTACTS_FIELD = (By.XPATH, "//a[contains(text(),'Контакты')]")
    LOCATOR_TAGES_TITLE_FIELD = (By.CLASS_NAME, "main")
    LOCATOR_TAGES_EMAIL_FIELD = (By.LINK_TEXT, "jump@tages.ru")
    LOCATOR_TAGES_PHONE_FIELD = (By.LINK_TEXT, "+7 (495) 640-23-94")
    LOCATOR_TAGES_FORM_INPUT = (By.CLASS_NAME, "form__input")
    LOCATOR_TAGES_INPUT_NAME_FIELD = (By.CSS_SELECTOR, ".form__input:nth-child(1)")
    LOCATOR_TAGES_PARTNERS_FIELD = (By.CLASS_NAME, "partners__list")
    LOCATOR_TAGES_CONFIDENTIAL_FIELD = (By.LINK_TEXT, "Политика конфиденциальности")
    LOCATOR_TAGES_TELEGRAM_LINK_FIELD = (By.CLASS_NAME, "social-list__item")
    LOCATOR_TAGES_SEND_BUTTON = (By.CLASS_NAME, "form__button-container")
    LOCATOR_TAGES_SEND_CONFIRMED_TEXT = (By.XPATH, "//a[contains(text(),'Ваше обращение получено')]")

class MainPage(BasePage):

    def click_about_button(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_ABOUT_FIELD).click()

    def click_academy_button(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_ACADEMY_FIELD).click()

    def click_events_button(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_EVENTS_FIELD).click()

    def click_blog_button(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_BLOG_FIELD).click()

    def click_vacancies_button(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_VACANCIES_FIELD).click()

    def click_contacts_button(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_CONTACTS_FIELD).click()

    def check_title(self):
        title_field = self.find_element(TagesMainLocators.LOCATOR_TAGES_TITLE_FIELD)
        return title_field

    def click_phone_field(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_PHONE_FIELD).click()

    def click_mail_field(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_EMAIL_FIELD).click()

    def click_partners_field(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_PARTNERS_FIELD).click()

    def click_confident_field(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_CONFIDENTIAL_FIELD).click()

    def click_telegram_link_field(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_TELEGRAM_LINK_FIELD).click()

    def click_send_button(self):
        return self.find_element(TagesMainLocators.LOCATOR_TAGES_SEND_BUTTON).click()

    def paste_name(self, name):
        name_field = self.find_element(TagesMainLocators.LOCATOR_TAGES_INPUT_NAME_FIELD)
        name_field.click()
        name_field.send_keys(name)
        return name_field

    def paste_form_input(self, word, index):
        return self.paste_word (word, TagesMainLocators.LOCATOR_TAGES_FORM_INPUT, index)

    def paste_word(self, word, locator, index):
        word_field = self.find_elements(locator)
        word_field[index].click()
        word_field[index].send_keys(word)
        return word_field

    def check_visible_confirmation(self):
        return self.element_visible(TagesMainLocators.LOCATOR_TAGES_SEND_CONFIRMED_TEXT)

    def check_invisible_confirmation(self):
        return self.element_invisible(TagesMainLocators.LOCATOR_TAGES_SEND_CONFIRMED_TEXT)