import io
import pyqrcode
from base64 import b64encode
#QR Cide till here



import cryptography
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import eel

eel.init('web')

@eel.expose
def generate_qr(data):
    password = data.encode() # Convert to type bytes
    salt = b'\x8f\x9f3\xf1V\\\n:\xa5\x87h\x9e*\xd1\xc4\xda\xa9.\x96\xfc/\xa9\xb4\x0e\xc8wD\x9d\xee\xeb\xb1E'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    main_key = key

@eel.expose
def get_message(message):
    f=Fernet(key)
    encrypted = f.encrypt (message)

#QR Code starts here
    img = pyqrcode.create(encrypted)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR code generation successful.")
    return "data:image/png;base64, " + encoded

eel.start('main.html',size=(1000,600))
