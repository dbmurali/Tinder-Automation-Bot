# Tinder-Automation-Bot
The Tinder Automation Bot, This script automates Tinder using Selenium WebDriver, allowing you to log in with Facebook, handle CAPTCHA manually, and swipe right continuously with ease.

## ✨ Features

✅ Automated Tinder Login via Facebook.✅ Seamless Window Switching between Tinder & Facebook.✅ Handles CAPTCHA Manually (User Input Required).✅ Continuous Right Swiping for hands-free operation.

## 📌 Prerequisites

  🔹 1. Install Dependencies
  
  Make sure Python is installed, then install Selenium:
  
  pip install selenium

  🔹 2. Download WebDriver
  
  Get Chrome WebDriver from:
  🔗 Download ChromeDriverEnsure the version matches your Chrome browser.
  
  🔹 3. Set Up Environment Variables
  
  Keep your credentials secure by setting them as environment variables:
  
  Windows (Command Prompt):
  
  set EMAIL=your_email@example.com
  set PASSWORD=your_facebook_password
  
  Linux/macOS (Terminal):
  
  export EMAIL=your_email@example.com
  export PASSWORD=your_facebook_password

## 🚀 How to Run the Script

  1️⃣ Open a terminal or command prompt.2️⃣ Run the script:
  
  python tinder_bot.py
  
  3️⃣ Manually complete CAPTCHA when prompted.4️⃣ Watch as the bot swipes left continuously! 🎉

## 🛠 Code Workflow

  📌 Opens Tinder & clicks the login button.📌 Chooses Facebook Login & switches to the Facebook window.📌 Enters Credentials & submits the login form.📌 Waits for Manual CAPTCHA Completion.📌 Handles Pop-ups (Location & Notifications).📌 Starts Swiping Right Continuously! 🔄
  
  ### Common Issues & Fixes

  ❌ selenium.common.exceptions.NoSuchElementException
  
  ✅ XPath may have changed, update it in find_element(By.XPATH, value='...').
  
  ❌ CAPTCHA Handling
  
  ✅ The script pauses and waits for manual CAPTCHA solving.
  
  ❌ ChromeDriver Compatibility Issue
  
  ✅ Ensure ChromeDriver version matches your Chrome browser version.

## ⚠️ Disclaimer

  This project is for educational purposes only. Use responsibly. ❤️
