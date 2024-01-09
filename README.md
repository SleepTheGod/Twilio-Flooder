Twilio Flooder
This repository contains a script that integrates Python and Node.js functionalities to flood Twilio with calls to a specific number.

Overview
The script combines Python and Node.js functionalities. The Python part handles Twilio calls and initiates the Node.js subprocess for concurrent calling.

Prerequisites
Python 3.x
Node.js
twilio package for Python (pip install twilio)
twilio package for Node.js (npm install twilio)
Ensure environment variables are set for Twilio authentication (TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN)
Setup
Clone this repository to your local machine:

git clone https://github.com/SleepTheGod/Twilio-Flooder.git

Install the required Python dependencies:
pip install twilio

Install the required Node.js dependencies:
npm install twilio

Set environment variables for Twilio authentication:
export TWILIO_ACCOUNT_SID=your_account_sid
export TWILIO_AUTH_TOKEN=your_auth_token
export TARGET_PHONE_NUMBER=target_number_to_flood
export SOURCE_PHONE_NUMBER=your_twilio_number
export TWIML_URL=https://handler.twilio.com/twiml/EH83ede6e13d3f59c05a260b6b72dc407f
export MAX_CALLS=10  # Set the number of calls to be made (Set to 0 for infinite calls)

Usage
Run the Python script:
python twilio_flooder.py

The script will prompt for your Twilio number, the number you want to flood, and confirmation to start the flooder.

Upon confirmation, the script initiates a flood of calls using the Node.js subprocess.

Contributions
Contributions to improve the script's efficiency, add new features, or resolve issues are welcome. Feel free to fork this repository and create a pull request.

License
This project is licensed under the MIT License.
