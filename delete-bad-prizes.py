import imap_tools
import time
emailUsername = "mailbox@yourcatchall.co.uk"  # username for your mailbox
emailPassword = "ABC123"  # catch-all email account pass
imapServer = 'mail.yourcatchall.co.uk'  # imap server for your catchall - google it for gmail etc
catchall = "yourcatchall.co.uk"  # i.e. mycatchall.com (no need to include the @ or anything)


def main():
    mailbox.folder.set(
        'Prizes')  # Set the name of the mailbox your messages are in - I had a rule created to move prizes to a specific folder
    current_folder = mailbox.folder.get()  # Get the above mailbox
    for msg in mailbox.fetch('SUBJECT "won a slice of the action!" (UNSEEN)',
                             charset='utf8'):  # Search for emails with the winning subject
        if msg.attachments[0].size == 126693:  # this is the filesize of the doughballs image
            mailbox.delete(msg.uid)
            print("Doughballs - deleted")
        else:
            if msg.attachments[0].size == 111931:  # this is the filesize of the desserts image
                mailbox.delete(msg.uid)
                print("Desserts - deleted")
            else:
                if msg.attachments[0].size == 112111:  # this is the filesize of the drinks image
                    mailbox.delete(msg.uid)
                    print("Drinks - deleted")
                else:
                    mailbox.move(msg.uid, 'Good')  # I had a folder called Good to move good prizes into
                    print("POTENTIALLY GOOD PRIZE MOVED TO GOOD FOLDER!!!")


if __name__ == '__main__':
    while True:
        try:
            mailbox = imap_tools.MailBox(imapServer).login(emailUsername, emailPassword)  # Connect to mailserver
            # it might be wise to move the above line outside of the while statement, your choice
            main()
            print("waiting to avoid spam")
            time.sleep(300)
        except:
            print("Exception - sleeping for 60 seconds")
            time.sleep(60)