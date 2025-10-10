import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings


def convert_to_base62(num):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    if num == 0:
        return characters[0]

    result = ""
    while num > 0:
        num, rem = divmod(num, base)
        result = characters[rem] + result
    return result


def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    url = f"{settings.PROTOCOL}://{settings.DOMAIN_NAME}/{link.short_code}"
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    filename = f"{link.short_code}_qr.png"
    link.qr_code.save(filename, File(buffer), save=False)
    link.save()
