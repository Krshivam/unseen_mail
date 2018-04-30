import imapclient
import pprint
import pyzmail
imapObj = imapclient.IMAPClient("imap.gmail.com",ssl=True)
user_name = raw_input()
passwd = raw_input()
imapObj.login(user_name,passwd)
#to see all  folders type  pprint.pprint(imapObj.list_folders())
#i am searching for inbox
imapObj.select_folder("INBOX",readonly=True)
#here XXX should be your preferred begining Date eg - 30-Apr-2018
#and YYY should be your date upto you want to see
#eg - imapObj.search('SINCE 30-Apr-2018','BEFORE 02-May-2018','UNSEEN')
UIDs = imapObj.search('SINCE XXX','BEFORE YYY','UNSEEN')
UIDs
#index which you want to see
rawMessages = imapObj.fetch(UIDs[index],['BODY[]','FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessages[index]['BODY[]'])
message.get_subject()
message.get_adresses('from')
message.get_adresses('to')
message.get_adresses('bcc')
message.get_adresses('cc')
message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)
imapObj.logout()


