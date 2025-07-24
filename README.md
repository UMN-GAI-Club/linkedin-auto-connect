# LinkedIn Auto Connect

This Python script automates sending connection requests on LinkedIn by simulating keyboard actions (Tab + Enter) using Selenium. It’s designed to work with the "People you may know" modal in the **My Network** section of LinkedIn.

---

## Setup
```
git clone https://github.com/UMN-GAI-Club/linkedin-auto-connect.git
cd linkedin-auto-connect
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py --delay 1000 --max-connection 20
```
Now, type your usrname and password in the console/terminal. Or if you know how to get linkedin cookie, get the cookie and put it in a `.env` file: `LINKEDIN_COOKIE="{ACTUAL_COOKIE}"`

<details>
<summary>Finding your LinkedIn Token</summary>

- Open Chrome 
- Go to developer tools
- In thee tab with `Element, Console, Sources, ... ` find `Application` (Click on the `>>` button if not present) 
- Under `Cookies/https://www.linkedin.com` find the cookie with Name `li_at`. This is your LinkedIn Cookie!
</details>


## Demo

![gif](assets/linkedin-connect-demo.gif)

---

## 🚀 Features

- Automatically sends connection requests using simulated keypresses.
- Supports login with cookie or email/password.
- Customizable delay and number of connections.
- CLI interface for flexibility.
