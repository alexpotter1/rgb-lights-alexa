# rgb-lights-alexa
Repository to hold code to allow Amazon Alexa devices to control RGB lighting strips

### Hardware details
 * This project is run on a Raspberry Pi 2 that is connected to a generic 4-pin RGB lighting strip (one wire for Red, Green, Blue and +12V DC)
 * Most likely, you will need three 3.3V MOSFETs that will regulate the voltage to each pin of the strip (we used three IPP060N06N MOSFET transistors by Infineon Technologies)
 * You will also need a generic 12V power supply...we spliced off the kettle plug and crimped the positive and neutral rails into the breadboard power rails
 * Link all three MOSFET ground into one rail, and hook this up to the GND GPIO pin on the Raspberry Pi.

 *I have tested this with the Amazon Alexa assistant with the Sonos One, and it works as intended. I haven't actually tested it on an Amazon Echo device, but similar results should be expected.*

### Software details
 * Raspbian, the Debian-based Linux distribution for the Raspberry Pi includes a Python library for controlling the GPIO pins.
 * The Pi runs a web server, powered by Flask, to accept incoming JSON messages from the Amazon Cloud for specific, defined Alexa intents.
 * Each intent is bound to a function with Flask that directly sets voltages across the lighting pins, to turn each LED on separately, or all at once (or turn them off).
 * The Pi responds with a JSON message to Alexa, confirming if the request was handled successfully, and providing a speech response for feedback to the user.
   - These responses are defined in `templates.yaml`.

 * To aid with port forwarding, the Raspberry Pi also operates a HTTPS tunnel with [ngrok.io](https://ngrok.com/), since Amazon mandates the use of TLS-secured connections for communicating to a custom Alexa Skill backend (or use AWS Lambda)
   - This can be circumvented with *Let's Encrypt*, configuring Flask to use HTTPS and manually forwarding ports on your router/firewall,      but I was too lazy...

### Get up and running
 1. Clone this repository:
 ```
 git clone https://github.com/alexpotter1/rgb-lights-alexa
 ```
 2. Inspect the `app_alexa.py` program, which acts as the main server.
   * Here, you can change pin numbers for each LED, and define custom behaviours.

 3. Run the Python script *(may need to `chmod` as executable)*
 4. In another terminal/tmux/screen, run the following to setup ngrok:
 ```
   sudo ./ngrok http 5000
 ```
 Make a note of the HTTPS address, ending in *ngrok.io*.

 5. Log in (or sign up) to your Amazon Developer account at [developer.amazon.com](https://developer.amazon.com/)
 6. Define a custom Alexa skill, and follow the wizard to setup your Skill Name, Invocation Name, your Intent Schema (as JSON), Sample Utterances (what you want to say to Alexa to trigger each intent), and Endpoint (select HTTPS and copy your URL here).
 7. Once you have defined a valid Interaction Model, your skill should be available for testing on your Amazon account. You can link the skill to Alexa by going to the Amazon Alexa app > Skills > Your Skills > Enable Skill (for your new lights skill)

I am trying to work on porting this code to function using the Alexa Smart Home Skill API, as the voice commands to change lights state are less rigid grammatically, and more natural to say.
