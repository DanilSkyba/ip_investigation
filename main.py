import webbrowser

user_input=input("Enter Domain name, URL or IP adress:")

urls = [("https://www.talosintelligence.com/reputation_center/lookup?search={0}".format(user_input)), ("https://www.virustotal.com/gui/search/{0}".format(user_input)), ("https://www.abuseipdb.com/check/{0}".format(user_input)), ("https://otx.alienvault.com/browse/global/pulses?q={0}&include_inactive=0&sort=-modified&page=1&limit=10&indicatorsSearch={0}".format(user_input))]

def open_browser_for_investigation(ip_domain_url):
    for x in ip_domain_url:
        webbrowser.open(x)

open_browser_for_investigation(urls)