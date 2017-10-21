"""
    Send Email
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from stock_common.conf.config import Config

CONFIGS = Config.get_configs()


class Gmail():
    """
        Send Email Using Gmail
    """

    def __init__(self, user=CONFIGS.GMAIL_USER, password=CONFIGS.GMAIL_PASS):
        self.user = user
        self.password = password

    def send(self, to, subject, body):
        """
        Send Email

        Args:
            to (list like)
            subject (str)
            body (str): text or html
        """
        msg = self._create_message(to, subject, body)

        mailer = smtplib.SMTP('smtp.gmail.com', 587)
        mailer.ehlo()
        mailer.starttls()
        mailer.ehlo()
        mailer.login(self.user, self.password)
        mailer.sendmail(self.user, to, msg.as_string())
        mailer.close()
        print('Sent email to %s' % (', '.join(to)))

    def _create_message(self, to, subject, body):
        """
            Create Message
        """
        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = ', '.join(to)
        msg['Subject'] = subject
        msg.attach(MIMEText(body))
        return msg


if __name__ == '__main__':

    # test sending a real email
    to = ['iamzjk@gmail.com', 'aelkner@gmail.com']
    subject = 'TEST GMAIL'
    body = 'TEST GMAIL BODY'
    gmail = Gmail()
    gmail.send(to, subject, body)
