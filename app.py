# from flask import Flask, render_template, request, jsonify
# import os
# import subprocess
# from datetime import datetime

# app = Flask(__name__)

# # Public variable to store all emergency messages
# emergency_messages = []
# contact_number = "+919790559885"  # Set a common contact number

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/send_alert', methods=['POST'])
# def send_alert():
#     try:
#         name = request.form['name']
#         latitude = request.form['latitude']
#         longitude = request.form['longitude']
#         flood_height = request.form['flood_height']
        
#         current_time = datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p")
#         message = (f"[ALERT] Name: {name}, Lat: {latitude}, Long: {longitude}, "
#                    f"Time: {current_time}, Flood Height: {flood_height}.")
        
#         # Append to the public emergency_messages list
#         emergency_messages.append(message)
        
#         # Combine all messages into one
#         full_message = "\n".join(emergency_messages)
#         escaped_message = full_message.replace(" ", "%20").replace("\n", "%0A")
        
#         # Create batch script content
#         bat_content = f"""@echo off
# adb shell am start -a android.intent.action.VIEW -d "sms:{contact_number}?body={escaped_message}"
# timeout /t 2 >nul
# adb shell input tap 633 1421
# """
        
#         # Define batch file name
#         bat_file = "emergency_alert.bat"
        
#         # Write the batch script
#         with open(bat_file, "w") as file:
#             file.write(bat_content)
        
#         # Execute the batch script
#         subprocess.run([bat_file], shell=True)
        
#         return jsonify({"status": "success", "message": "Emergency alert added and sent!"})
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)})
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


from flask import Flask, render_template, request, jsonify
import os
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_alert', methods=['POST'])
def send_alert():
    try:
        name = request.form['name']
        contact = request.form['contact']  # Collected for reference only
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        flood_height = request.form['flood_height']
        
        current_time = datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p")
        emergency_message = (
            f"EMERGENCY ALERT! Name: {name}, Contact: {contact}, "
            f"Location: Unknown, Lat: {latitude}, Long: {longitude}, "
            f"Time: {current_time}, Flood Height: {flood_height}."
        )

        # Encode spaces and special characters for URL
        escaped_message = emergency_message.replace(" ", "%20")

        # Hardcoded emergency number
        emergency_number = "919790559885"

        # Build the one-line ADB command
        bat_content = f'@echo off\nadb shell am start -a android.intent.action.VIEW -d "sms:{emergency_number}?body={escaped_message}"\ntimeout /t 2 >nul\nadb shell input tap 633 1421\n'

        # Write and run batch file
        bat_file = "emergency_alert.bat"
        with open(bat_file, "w") as file:
            file.write(bat_content)

        subprocess.run([bat_file], shell=True)

        return jsonify({"status": "success", "message": "Emergency alert sent!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
#& "C:\Users\admin\Desktop\projects\alert\alert\mads\ngrok.exe" http 5000                                
#& "C:\Users\admin\Desktop\projects\alert\alert\mads\ngrok.exe" config add-authtoken 2ygAcCmTxnXVRpr3XxkCemk96C1_4TwsYjhR6XL9Nm489nutq