from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Rute utama untuk menampilkan halaman chatbox
@app.route('/')
def index():
    return render_template('index.html')

# Rute untuk mendapatkan respons dari bot
@app.route('/get_response')
def get_response():
    user_message = request.args.get('msg').lower()  # Dapatkan pesan dari pengguna dan ubah menjadi huruf kecil

    # Tentukan respons berdasarkan kata kunci
    if "hello" in user_message:
        response = "Hi Ram!"
    elif "aku nak tanya sesuatu" in user_message:
        response = "apa itu?"
    elif "bagaimana kita berdua menikah" in user_message:
        response = "Eh?! Apa yang kamu bicarakan, tiba-tiba begitu?! S-seperti aku akan langsung bilang iya begitu saja...!! Jangan salah paham, ya! Bukannya aku mau atau apa, aku hanya... hanya... ehm... ah sudahlah, pokoknya, siapa juga yang mau menikah sama kamu, dasar bodoh! ...tapi kalau kamu benar-benar serius... mungkin aku akan... mempertimbangkannya, mungkin!"
    elif "help" in user_message:
        response = "I'm here to assist you! Ask me anything."
    else:
        response = "I'm not sure how to respond to that, but I'm here to listen!"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
