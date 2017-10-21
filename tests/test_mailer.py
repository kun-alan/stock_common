"""
    Unittest for Gmail class in lib/mailer.py
"""

from smtplib import SMTPAuthenticationError
from stock_common.lib.mailer import Gmail


def test_gmail():
    """
        Test sending email with gmail
    """

    user = 'test_fake'
    password = 'test_fake_no_way_can_be_right'
    to = ['test_email@whatever_a_fake_domain.com']
    subject = 'test email'
    body = 'test email'

    gmail = Gmail(user, password)

    get_err = None
    try:
        gmail.send(to, subject, body)
    except Exception as err:
        get_err = err

    assert type(get_err) is SMTPAuthenticationError
