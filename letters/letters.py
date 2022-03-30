import string
import random
import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw, ImageOps


def swap_random(seq):
    idx = range(len(seq))
    i1, i2 = random.sample(idx, 2)
    seq[i1], seq[i2] = seq[i2], seq[i1]
    return seq


def letters_a(letter_mat):
    for i, letters in enumerate(letter_mat):
        for _ in range(i):
            swap_random(letters)


def letters_b(letter_mat):
    for i in range(len(letter_mat)):
        if i > 0:
            letter_mat[i] = [i for i in letter_mat[i - 1]]

        for j in range(i):
            letter_mat[i] = swap_random(letter_mat[i])


def letters_c(letter_mat):
    for i in range(len(letter_mat)):

        p = (1 / (100 * (i + 1)))
        for j in range(i + i // 2):
            r = random.random()

            letter_mat[i][np.random.randint(0, len(letter_mat[i]))] = random.choice(string.ascii_lowercase)


abc = string.ascii_lowercase

w = 40
h = 40

letter_mat = [['o' for _ in range(w)] for _ in range(h)]
letters_c(letter_mat)


img_w = w * 20
img_h = h * 20

img = Image.new("RGB", (img_w, img_h), (255, 255, 255))

img_edit = ImageDraw.Draw(img)

noise = PerlinNoise()

for r, letters in enumerate(letter_mat):
    for c, letter in enumerate(letters):
        # font_size = max(5, r+c + np.random.randint(-20, 20))
        # font_size = max(5, (r-c)*4 + np.random.randint(-20, 20))
        font_size = max(10 + np.random.randint(-5, 5), r + np.random.randint(-20, 20)) + 0.3 * np.interp(
            noise([5 * c / w, 5 * r / h]), [-0.7, 0.7], [5, 50])
        # font_size = max(5, np.linalg.norm([c - w // 2, r - h // 2]) * 2.5 + np.random.randint(-20, 20))
        # font_size = np.interp(noise([5 * c / w, 5 * r / h]), [-0.7, 0.7], [5, 50])
        # letter = abc[int(np.interp(font_size, [5, 50], [0,len(abc)]))]
        font_size = int(font_size)
        x = img.width / w * c
        y = img.height / h * r - font_size / 2 + 5

        font = ImageFont.truetype("1942.ttf", font_size)

        img_edit.text((x, y), letter, (0, 0, 0, 255), font=font)

img = ImageOps.expand(img, border=(250, 250), fill=(255, 255, 255))


img.show()
