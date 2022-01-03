from os import waitpid
import tkinter as tk
import smtplib

root = tk.Tk()
root.title("Mail_Sender TK")
root.geometry("350x350")
root.config(bg="#e8e7e3")

def send():
    user_mail = sender_email_ent.get()
    user_mail = str(user_mail)
    user_pwd = sender_pwd_ent.get()
    recev_mail = receiver_email_ent.get()
    subj = subject_ent.get()
    body = body_ent.get()
    try:
        session = smtplib.SMTP('smtp.mail.ru',587) 
        session.ehlo()
        session.starttls()
        session.login(user_mail, user_pwd)
        session.sendmail(user_mail, recev_mail , 'Subject: {}.\n{}'.format(subj, body))
        session.quit()

        res_lbl = tk.Label(root, text="Успешно!", fg="green")
        res_lbl.pack()
        res_lbl.configure(font=("Courier", 16, "bold"))
    except smtplib.SMTPAuthenticationError:
        err_lbl = tk.Label(root, text="Ошибка при авторизации", fg='red', font='20')
        err_lbl.pack()
        err_lbl.configure(font=("Courier", 16, "bold"))

    

sender_email_lbl = tk.Label(text='Ваш e-mail:')
sender_email_lbl.pack()
sender_email_ent = tk.Entry(root, bd=2, bg='black', fg='white', width=50)
sender_email_ent.pack()

sender_pwd = tk.Label(root, text="Ваш пароль:")
sender_pwd.pack()
sender_pwd_ent = tk.Entry(root, bd=2, bg="black", fg="white", width=50)
sender_pwd_ent.pack()

receiver_email_lbl = tk.Label(text="E-mail получателя: ")
receiver_email_lbl.pack()
receiver_email_ent = tk.Entry(root, bd=2, bg='white', fg='black', width=50)
receiver_email_ent.pack()

subject_lbl = tk.Label(root, text="Тема письма: ")
subject_lbl.pack()
subject_ent = tk.Entry(root, bd=2, bg='white', fg='black', width=50)
subject_ent.pack()

body_lbl = tk.Label(root, text="Текст письма: ")
body_lbl.pack()
body_ent = tk.Entry(root, bd=3, bg='white', fg='black', width=50)
body_ent.pack()

but = tk.Button(root, text="Отправить", bg="blue", fg="white", width=20, height=2, command=send).pack(pady=15)


root.mainloop()


