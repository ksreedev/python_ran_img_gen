from PIL import Image
from flask import Flask, render_template
from random import randint

#functionDeclarations
def random_img_generation():
    im = Image.new("RGB", (500,500), (255, 255, 255))
    pixmap = im.load()
    for x in range(500):
        for y in range(500):
            pixmap[x, y] = (randint(0, 255), randint(0, 255), randint(0,255))
    im.save("./static/images/rand.png")


#ServerFunctions
application = Flask(__name__)
@application.route("/")
def index():
    random_img_generation()
    return render_template("index.html")

if __name__ == '__main__':
    application.run(host="localhost")
