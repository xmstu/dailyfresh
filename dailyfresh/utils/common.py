from django.core.mail import send_mail
from dailyfresh import settings


# utils/common.py
def send_active_email(username, receiver, token):
    """封装发送邮件方法"""

    subject = '天天生鲜用户激活'        # 标题
    message = ""                      # 邮件正文
    sender = settings.EMAIL_FROM      # 发件人
    receivers = [receiver]            # 接受人,需要的是列表

    # 邮件正文(带html样式)
    html_message = '<h2>尊敬的 %s, 感谢注册天天生鲜</h2>' \
                   '<p>请点击此链接激活您的帐号: ' \
                   '<a href="http://127.0.0.1:8000/users/active/%s">' \
                   'http://127.0.0.1:8000/users/active/%s</a>' \
                   % (username, token, token)
    send_mail(subject, message, sender, receivers, html_message=html_message)