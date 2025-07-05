# adb_web_message
📡 Flood Emergency Alert System using Flask + ADB + ngrok

This project is a lightweight emergency alert web app built with Flask, designed to collect alert information from users and immediately send an SMS to a fixed emergency contact number using ADB (Android Debug Bridge) and a connected Android phone.
🔥 Key Features

    🌐 Web-based alert form accessible from anywhere using ngrok public URL

    📲 SMS automation via ADB: Sends alert messages directly from a connected Android phone

    💬 All alerts are sent to a single predefined emergency number

    🧠 Real-time data like name, contact, location (lat/long), flood height, and timestamp are included

    🔌 No internet or SIM required on the client side — just submit the form

🛠️ Technologies Used

    Flask – Python micro web framework

    ADB – Android Debug Bridge to control the device via terminal

    ngrok – Exposes localhost to the internet via public HTTPS link

    Batch script (.bat) – Automates launching Flask and ngrok

🚀 How It Works

    Host opens the Flask server locally using python app.py

    Run ngrok http 5000 to get a public URL

    Share the public URL with users in remote locations

    When a user submits the alert form:

        Flask receives the data

        A .bat file is triggered to run ADB command

        A connected Android phone sends the emergency SMS to +919790559885

📂 Folder Structure

/mads
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Frontend alert form
├── emergency_alert.bat     # ADB SMS automation
├── launch_alert_app.bat    # Launches both Flask and ngrok
├── ngrok.exe               # ngrok binary (can be excluded from Git)

⚠️ Requirements

    Python 3.x with Flask installed (pip install flask)

    Android phone with USB debugging enabled

    adb installed and working (adb devices)

    ngrok.exe in project folder

    Internet for ngrok to work

🧪 Usage

    Plug in your phone with USB debugging ON

    Double-click launch_alert_app.bat

    Copy and share the ngrok URL

    When someone submits the form, your phone sends the SMS automatically
