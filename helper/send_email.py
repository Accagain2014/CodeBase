#!/usr/bin/env python
#coding=utf-8

# @Date:    2018/11/07 10:19
# @File:    send_email.py

# @Content:

# python -m SimpleHTTPServer python 搭建文件服务器

import smtplib

from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from os.path import basename


parser = OptionParser()
parser.add_option("-f", "--from", dest="sender", help="sender email address", default="from email")
parser.add_option("-t", "--to", dest="recipient", help="to email address", default="to email")
parser.add_option("-s", "--subject", dest="subject", help="email subject", default="Send pics test")
parser.add_option("-i", "--image", dest="image", help="image attachment", default=None)
parser.add_option("-c", "--content", dest="content_file", help="send html file", default=None)
parser.add_option("-a", "--attachment", dest="a_files", help="attachment_file", default=None)

(args, _) = parser.parse_args()

# print args.subject, args.sender, args.recipient
# Create message container.
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = args.subject
msgRoot['From'] = args.sender
msgRoot['To'] = args.recipient.strip()

images = []
if args.image is not None:
    images = args.image.strip().split(",")
msgImages = []
# Create the body of the message.
html = '<p>'
if args.content_file is not None:
    with open(args.content_file, "r") as fr:
        content = fr.read()
        html += content

for i in range(len(images)):
    html += '<br/><img src="cid:image%s">' % str(i)
    with open(images[i], "rb") as fr:
        msgImg = MIMEImage(fr.read(), images[i].split(".")[1])
        msgImg.add_header('Content-ID', '<image%s>' % str(i))
        msgImg.add_header('Content-Disposition', 'inline', filename=args.image)
        msgImages.append(msgImg)
html += '</p>'

# print html
# Record the MIME types.
msgHtml = MIMEText(html, 'html')
msgRoot.attach(msgHtml)
for msgImg in msgImages:
    msgRoot.attach(msgImg)

if args.a_files is not None:
    a_files = args.a_files.strip().split(",")
    for one_a_file in a_files:
        with open(one_a_file, "rb") as fr:
            atta_file = MIMEApplication(fr.read(), Name=basename(one_a_file))
        atta_file['Content-Disposition'] = 'attachment; filename="%s"' % basename(one_a_file)
        msgRoot.attach(atta_file)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')

s.sendmail(args.sender, args.recipient.strip().split(","), msgRoot.as_string())
s.quit()