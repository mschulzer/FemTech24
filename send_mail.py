import umail
import network

ssid = 'replace_with_your_ssid'
password = 'replace_with_your_password'

sender_email = 'write_senders_email'
sender_name = 'Mail Client'
sender_app_password = 'write_senders_app_password'
recipient_email ='write_receivers_email'
email_subject ='Test Email'

def connect_wifi(ssid, password):
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())
    
# Forbind til WiFi
connect_wifi(ssid, password)

# Send en mail
smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)
smtp.login(sender_email, sender_app_password)
smtp.to(recipient_email)
# Skriv email header
smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
smtp.write("Subject:" + email_subject + "\n")
# Skriv email body
smtp.write("Test Email from Raspberry Pi Pico W")
# Send mailen
smtp.send()
# Afslut mail-session
smtp.quit()
