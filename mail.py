import smtplib

class Mail:

    def __init__(self, mail, pwd) -> None:
        self.user = mail 
        self.pwd = pwd 
    
    def sendEmail(self, rcp, rec, content):


        mail_text = \
    f"""
{content}
    """

        subject = f"Ihr taegliches Bibelzitat"

        MAIL_FROM = f"Benedict's Weisheiten<{self.user}>"
        RCPT_TO = rec
        DATA = "From:%s\nTo:%s\nSubject:%s\n\n%s" % (MAIL_FROM, RCPT_TO, subject, mail_text)
        RCP = rcp

        server = smtplib.SMTP_SSL("mail.gmx.net")
        server.ehlo()
        server.login(self.user, self.pwd)
        server.sendmail(MAIL_FROM, RCP, DATA)

        server.quit()
        return "MAIL SEND"
