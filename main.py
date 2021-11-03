#!/usr/bin/python
# .------..------..------..------..------.
# |S.--. ||L.--. ||3.--. ||4.--. ||K.--. |
# | :/\: || :/\: || :(): || :/\: || :/\: |
# | :\/: || (__) || ()() || :\/: || :\/: |
# | '--'S|| '--'L|| '--'3|| '--'4|| '--'K|
# `------'`------'`------'`------'`------'
# https://twitter.com/SL34K
# https://github.com/SL34K

import imap_tools
import random
import requests
import string
import time

totalEntries = 0  # Initialise count of entries
startDomain = 'https://slice-of-the-action.pizzaexpress.com/registration'

# Configuration
emailUsername = "mailbox@yourcatchall.co.uk" # your catchall email username
emailPassword = "ABC123"  # catch-all email account pass
imapServer = 'mail.yourcatchall.co.uk'  # imap server for your catchall - google it for gmail etc
catchall = "yourcatchall.co.uk"  # i.e. mycatchall.com (no need to include the @ or anything)
fName = "yourfirst"  # first name
lName = "yourlast"  # last name
dob = "MM/DD/YYYY"  # date of birth MM/DD/YYYY
postcode = "SW21LS"  # enter a random postcode or your own, no space
waitBetweenEntries = 0  # seconds to wait between entries they don't ratelimit so 0 is fine
apikey = "b5987479-d725-49a2-867d-80ee86d69186"  # Pizza Express site api key - inspect element to get this if needed


def main(email):
    session = requests.session()  # Start a fresh session for each entry
    session.headers = {
        "authority": "api.slice-of-the-action.pizzaexpress.com",
        "scheme": "https",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en;q=0.9",
        "origin": "https://slice-of-the-action.pizzaexpress.com",
        "referer": "https://slice-of-the-action.pizzaexpress.com/",
        "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "x-api-key": apikey
    }  # Headers - copied from inspecting requests
    register(session, email)  # Register for competition
    result = results(session, email)  # Spin the wheel
    if result == '{"hasWon":true}':  # Check if Spin = Win :)
        print("Winner")
        verify(session, email) # This verification step forces the link (claim prize email) to be sent instantly
        time.sleep(5)  # Buffer to let the email reach my mail server
        clickLink(session)  # This function collects the email, verifies it and then deletes the email to conserve space
    else:
        print(result)


def register(session, emails):
    payload = {
        "id": "",
        "firstName": fName,
        "lastName": lName,
        "emailAddress": emails,
        "dateOfBirth": dob,
        "postcode": postcode,
        "restaurantLocation": "",
        "tableNumber": "",
        "hasAgreedToOptin": "false",
        "metaData": {}}  # Payload - bare minimum
    session.post("https://api.slice-of-the-action.pizzaexpress.com/players", json=payload)


def results(session,emails):
    payload ={
        'emailAddress': emails
    }
    check = session.post("https://api.slice-of-the-action.pizzaexpress.com/results", json=payload)
    return check.text


def clickLink(session):
    mailbox.folder.set('Verification')  # Open up "Verification" folder I have my mailbox configured to move these mails to.
    current_folder = mailbox.folder.get()  # Get the above mailbox
    for msg in mailbox.fetch('SUBJECT "Almost there {}, please verify your email!"', charset='utf8',).format(fName):  # Search for emails with the specified subject
        print("Got email")
        time.sleep(1)
        link1 = msg.text.split("Please click the link below to verify your email and receive your prize reveal!")[1].split("Ciao")[0][2:-1]  #Extract the required link
        part1,part2 = link1.split("slice")  # Magic to create another required link
        link = part1+"api.slice"+part2  # As above
        rewardlink = link.split("players")[0]+"rewards"+link.split("players")[1].split("/verify")[0]   # Create the final required link
        session.post(rewardlink)  # Post the reward link - acts as a verification confirmation
        cemail = msg.to[0]  # Checks the email the link was sent to incase of coss-over
        print("Claiming for: "+cemail)  # confirms which email it's claiming for
        rewardStatus = claimPrize(session, cemail)  # Claims the prize for the correct email
        if rewardStatus == '{"message":"success"}':  # Checking response
            print("Claimed! Prize should arrive within 2 hours")
            try:
                mailbox.delete(msg.uid)  # Deletes the email to save space
                time.sleep(1)
            except:
                print("Error deleting email")
        else:
            print("Error sending email, you may be blocked")


def claimPrize(session,emails):
    payload = {
        'emailAddress': emails
    }
    check = session.post("https://api.slice-of-the-action.pizzaexpress.com/rewards/email", json=payload)
    return check.text


def verify(session,emails):
    payload = {
        'emailAddress': emails
    }
    check = session.post("https://api.slice-of-the-action.pizzaexpress.com/players/verify", json=payload)


def stringGen():  # Random string function based off code on google
    chars=string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range (8))


if __name__ == '__main__':
    mailbox = imap_tools.MailBox(imapServer).login(emailUsername, emailPassword)  # Connect to mailserver
    while True:  # Keep looping
        try:
            time.sleep(waitBetweenEntries)  # If a wait time is entered it will pause/wait
            email = (stringGen()) + str("@") + str(catchall)  # Generate a 'random' email
            print(email)  # Print the above 'random' email
            main(email)  # Trigger main process i.e. enter, check emails, claim prize
            totalEntries = totalEntries + 1  # Count entries
            print(totalEntries)
            print("Total entries: " + str(totalEntries))  # Show the current attempts/entries
        except:  # Fail-safe
            print("Unknown error - waiting 20 seconds")
            time.sleep(20)  # Wait incase of block etc.