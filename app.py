from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("me.html")  # Strona startowa ustawiona na 'me.html'

@app.route("/mypage/me")
def me():
    return render_template("me.html")

@app.route("/mypage/contact", methods=["GET", "POST"])
def contact_form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        print(f"Otrzymano wiadomość od {name} : {message}")  # Testowy zapis do konsoli
        return redirect(url_for("me"))  # Przekierowanie po wysłaniu formularza
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
