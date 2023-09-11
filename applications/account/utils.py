from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        "Bookstore",
        f"Привет перейди по этой ссылке чтобы активировать аккаунт: \n\nhttp://localhost:8000/api/account/activate/{code}",
        "aitievnurgazy@gmail.com",
        [email]
    )
