
from flask import Flask
from Crypto.PublicKey import RSA

private_key = RSA.generate(1024)
app = Flask( __name__ )

app.config['API_KEY'] = '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'
app.config['PRIVATE_KEY'] =  private_key.export_key()
app.config['PUBLIC_KEY'] = private_key.publickey().export_key()

