def random_img_generation():
    im = Image.new("RGB", (100,100), (255, 255, 255))
    pixmap = im.load()
    for x in range(100):
        for y in range(100):
            pixmap[x, y] = (randint(0, 255), randint(0, 255), randint(0,255))
    im.save("./static/images.png")
