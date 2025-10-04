import requests
import os

api_key='your_api_key_here'

sender_name='Whole Cloud'

sender_email='help@wholecloud.icu'

subject='Your new letter has been dispatched to address'

receiver_mail='reciever@gmail.com'

message='This is to inform you about your new order of letter has been dispatched and will reach you shortly<br> Thank you'

reply_mail='support@wholecloud.icu' # optional

attachment_path='C:/Capture.png' # optional


def dns_mail(api_key, sender_name, sender_email, subject, receiver, message, reply, attachment_path):
    try:
        form_data = {
            'license': api_key,
            'senderName': sender_name,
            'senderEmail': sender_email,
            'subject': subject,
            'reciever': receiver,
            'message': message,
            'reply': sender_email if reply == '' else reply,
            
        }
        
        headers = {
            'Authorization': f'Bearer {api_key}',
        }
        files = None
        
        if os.path.isfile(attachment_path):
            attachment = open(attachment_path, 'rb')
            files = {'attachment': (os.path.basename(attachment_path), attachment, 'application/octet-stream')}  
        else:
            files = {'attachment': None}
        response = requests.post(url='https://emailspoofing.org/api/v1/mail/send', data=form_data, headers=headers, files= files)
        if files['attachment']:
            attachment.close()
        if response.status_code == 200 and response.json().get('status') == 'success':
            print('Email Sent Successfully!')
        else:
            print('Error:', response.json())

    except Exception as err:
        print('Request failed:', str(err))

dns_mail(api_key, sender_name, sender_email, subject, receiver_mail, message, reply_mail, attachment_path)
