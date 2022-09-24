from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image 
import string 

with open("alice.txt", "r") as f:

    text = f.read()
    words = text.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
python_mask = np.array(PIL.Image.open("Snapchat-1414327952.jpg"))

colormap = ImageColorGenerator(python_mask)



wc = WordCloud(stopwords= STOPWORDS,
                mask= python_mask, 
                background_color= "white",
                contour_color= "black",
                contour_width=3,
                min_font_size= 3,
                max_words=400)
wc.generate(assembled)

wc.recolor(color_func= colormap)
plt.imshow(wc, interpolation = "bilinear")
plt.axis("off")
plt.show()