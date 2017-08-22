import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


from_addr = '274498361@qq.com'
#to_addr   = 'haokangli91@163.com'
to_addr   = '476071322@qq.com'
host_name = 'smtp.qq.com'
host_port = 465
passwd    = 'wufiaoawmfgxbjid'
title     = 'Every day wishes from your dear husband!'
content   = 'I LOVE YOU BABY!'

def mail():
    ret = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(['qq mail', from_addr])
        msg['To']   = formataddr(['163 mail', to_addr])
        msg['Subject'] = title

        server = smtplib.SMTP_SSL(host_name, host_port)
        #server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        #server.set_debuglevel(1)
        server.login(from_addr, passwd)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

ret = mail()
if ret:
    print('Email send successfully!')
else:
    print('Email send failed!')


