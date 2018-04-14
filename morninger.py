"""Morninger:
 It's a automated process which lets you customize your daily web browsing
 Author : Mohit Narula"""


import webbrowser
import time

url_dict = {
    'google': "https://www.google.com/",
    'gmail': "https://mail.google.com/mail/u/0/#inbox",
    'newstand': "https://newsstand.google.com/",
    'foxnews': "http://fox5sandiego.com/",
    'my_stocks': "https://goo.gl/BwQA9p"
}


def smart_greet():
    return_pm = "Working Late!, Good Evening Mohit"
    return_am = "Good Morning Mohit!!"
    am_or_pm = time.strftime("%p".format(time.localtime()))
    if am_or_pm == "PM":
        return return_pm
    else:
        return return_am


def morninger():
    local_day = time.strftime("%d-%B-%Y".format(time.localtime()))
    local_time = time.strftime("%I:%M %p".format(time.localtime()))
    print("""
          \n{}
          \n
          Today is, {} | Time = {}
          \n
          morninger is opening your daily websites\n""".
          format(smart_greet(), local_day, local_time))
    open_tabs()


def open_tabs():
    chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None,
                        webbrowser.BackgroundBrowser(chrome_path))
    my_browser = webbrowser.get('chrome')
    my_browser.open(url_dict['gmail'])
    my_browser.open(url_dict['google'])
    my_browser.open(url_dict['newstand'])
    my_browser.open(url_dict['foxnews'])
    my_browser.open(url_dict['my_stocks'])


if __name__ == "__main__":
    morninger()
