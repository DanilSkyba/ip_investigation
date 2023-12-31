'''
Doesn't work in AWS App Runner
from flask import Flask, request, render_template, redirect, url_for
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    try:
        if request.method == 'POST':
            user_input = request.form["inputs"]

            # Build URLs based on user input
            urls = [
                "https://www.talosintelligence.com/reputation_center/lookup?search={0}".format(user_input),
                "https://www.virustotal.com/gui/search/{0}".format(user_input),
                "https://www.abuseipdb.com/check/{0}".format(user_input),
                "https://otx.alienvault.com/browse/global/pulses?q={0}&include_inactive=0&sort=-modified&page=1&limit=10&indicatorsSearch={0}".format(user_input)
            ]

            # Open the URLs in the web browser
            open_browser_for_investigation(urls)

            # Redirect to the home page after submitting the form
            return redirect(url_for('home'))

        return render_template('index.html')
    except Exception as e:
        print("Error:", str(e))
        return "Internal Server Error", 500

def open_browser_for_investigation(ip_domain_url):
    for x in ip_domain_url:
        webbrowser.open(x)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
'''
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    try:
        if request.method == 'POST':
            user_input = request.form["inputs"]

            # Build URLs based on user input
            urls = [
                {"name": "Talos Intelligence", "url": f"https://www.talosintelligence.com/reputation_center/lookup?search={user_input}"},
                {"name": "VirusTotal", "url": f"https://www.virustotal.com/gui/search/{user_input}"},
                {"name": "AbuseIPDB", "url": f"https://www.abuseipdb.com/check/{user_input}"},
                {"name": "AlienVault OTX", "url": f"https://otx.alienvault.com/browse/global/pulses?q={user_input}&include_inactive=0&sort=-modified&page=1&limit=10&indicatorsSearch={user_input}"}
            ]

            return render_template('index.html', urls=urls)

        return render_template('index.html')
    except Exception as e:
        print("Error:", str(e))
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
