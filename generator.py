from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import randint

i = 0
with open("./ran.data", "r") as f:
	i = int(f.readlines()[0])

font_size = int(input("font size? "))
text = input("text? ")
person = input("person? ")
date = str(int(input("year? ")))

img = Image.open("person" + str(randint(1, i)) + ".jpg")

I1 = ImageDraw.Draw(img)
font = ImageFont.truetype("./font.ttf", font_size)

y = ""
if (img.size[0] / 3) + I1.textsize(text, font=font)[0] > img.size[0]:
	cont = True
	s = text
	s1 = text
	while cont:
		cont = False
		l = s.split(" ")
		s = ""
		for j in range(0, int(len(l) / 2)):
			s += l[j] + " "
		l = text.split(" ")
		s1 = ""
		for j in range(int(len(l) / 2), len(l)):
			s1 += l[j] + " "
		if (img.size[0] / 3) + I1.textsize(s, font=font)[0] < img.size[0]:
			y += s + "\n"
		else:
			cont = True
	cont = True
	while cont:
		cont = False
		l = text.split(" ")
		s1 = ""
		for j in range(int(len(l) / 2), len(l)):
			s1 += l[j] + " "
		if (img.size[0] / 3) + I1.textsize(s1, font=font)[0] < img.size[0]:
			y += s1 + "\n"
		else:
			cont = True
y += "\n-" + person + " " + date
I1.text((img.size[0] / 3, img.size[1] / 2), y, fill=(150, 150, 150), font=font, align="left")

img.show()
img.save("quote.png")