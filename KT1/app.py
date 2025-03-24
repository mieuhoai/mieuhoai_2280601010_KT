from flask import Flask, request, json, render_template
from cipher.vigenere import VigenereCipher

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = (request.form['inputKeyPlain'])
    Vigenere = VigenereCipher()
    encrypted_text = vigenere.encrypt_text(text,key)
    return f"text: {text}<br/>key: {key} <br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = (request.form['inputKeyCipher'])
    Vigenere = VigenereCipher()
    decrypted_text = vigenere.decrypt_text(text,key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text: {decrypted_text}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)