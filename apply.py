"""
Usage: ./apply.py [--email=<email>] [--password=<password>] [--search-url=<search-url>]

Automatic job applications.

Options:
  -h --help
"""
from docopt import docopt


import time

from selenium.webdriver.support.ui import Select

from selenium_helpers import start_browser, find

LOGIN_URL = 'https://www.jobserve.com/gb/en/Candidate/Login.aspx'
ELEMENTS = {
    'login_input_email': '#txbEmail',
    'login_input_pass': '#txbPassword',
    'login_submit': '#btnlogin',
    'btn_allow_cookies': '#PolicyOptInLink',
    'btn_open_apply_modal': '#JobDetailPanel #td_apply_btn',
    'btn_already_applied': '#JobDetailPanel #td_applied_btn',
    'drop_down_cv': 'select[name=ddlCV]',
    'drop_down_cv_options': 'select[name=ddlCV] option',
    'btn_submit_application': '.AppButton',
}


def _email_suggest_open(browser):
    try:
        find(browser, '#EmailAlertPrompt')
    except LookupError:
        return False
    else:
        time.sleep(5)
        return True


def _apply_to_all_jobs(browser, search_url):
    browser.get(search_url)

    job_links = browser.find_elements_by_class_name('jobItem')

    for job_link in job_links:
        job_title = job_link.find_element_by_css_selector(
            '.jobResultsTitle').get_attribute('innerHTML')

        while _email_suggest_open(browser):
            # Waiting for email spam popup to go away...
            pass

        job_link.click()

        already_applied = None
        try:
            find(browser, ELEMENTS['btn_open_apply_modal']).click()
        except LookupError:
            already_applied = find(browser, ELEMENTS['btn_already_applied'])
            if already_applied:
                print(f'ALREADY_APPLIED: {job_title}')

        if not already_applied:
            time.sleep(2)
            try:
                browser.switch_to.frame(browser.find_element_by_css_selector('iframe'))
            # try:
                select = Select(find(browser, ELEMENTS['drop_down_cv']))
            except Exception:
                browser.switch_to.frame(
                    browser.find_element_by_css_selector('iframe'))
                select = Select(find(browser, ELEMENTS['drop_down_cv']))

            value = browser.find_elements_by_css_selector(
                ELEMENTS['drop_down_cv_options'])[1].get_attribute('value')
            select.select_by_value(value)

            find(browser, ELEMENTS['btn_submit_application']).click()
            browser.switch_to.default_content()
            print(f'***APPLIED TO: {job_title} ***')
            browser.find_element_by_link_text('close').click()
            time.sleep(2)


def _login(browser, email, password):
    browser.get(LOGIN_URL)

    find(browser, ELEMENTS['btn_allow_cookies']).click()
    find(browser, ELEMENTS['login_input_email']).send_keys(email)
    find(browser, ELEMENTS['login_input_pass']).send_keys(password)
    find(browser, ELEMENTS['login_submit']).click()


def main():
    arguments = docopt(__doc__)
    search_url = arguments['--search-url']
    email = arguments['--email']
    password = arguments['--password']

    browser = start_browser()
    _login(browser, email=email, password=password)

    while True:
        _apply_to_all_jobs(browser, search_url=search_url)


if __name__ == '__main__':
    main()
