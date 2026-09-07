from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

j = jikan.anime(54595, extension='episodes')
s = jikan.seasons()

@app.route('/')
def home():
    a = str()
    for episode in j["data"]: 
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"

    a += "<h1>Аніме поточного сезону</h1>"

    for anime in s["data"]:
        title = anime.get("title", "Невідома назва")
        score = anime.get("score")
        
        if score is None:
            score_text = "немає оцінки"
        else:
            score_text = str(score)
        
        a += f"<p>{title} — оцінка: {score_text}</p>"
    return a

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
    