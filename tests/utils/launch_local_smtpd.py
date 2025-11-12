from aiosmtpd.controller import Controller
from aiosmtpd.smtp import SMTP
import email
import time

class TestSMTPHandler:
    async def handle_DATA(self, server: SMTP, session, envelope) -> str:
        """Handle incoming email data"""
        message = email.message_from_bytes(envelope.content)
        print(message)
        return '250 Message accepted for delivery'


if __name__ == '__main__':
    controller = Controller(TestSMTPHandler(), hostname='localhost', port=8025)
    controller.start()
    print("SMTP server running at localhost:8025")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping SMTP server")
        controller.stop()