from skimage import io, img_as_float
import numpy as np
import glob
import os
import pickle
from PIL import Image, ImageDraw
from perlin_noise import PerlinNoise
import bisect
from random import shuffle

# https://stackoverflow.com/questions/56335315/in-a-python-list-which-is-sorted-find-the-closest-value-to-target-value-and-its
# returns index, value
# takes list, target
def find_closest_index(a, x):
    i = bisect.bisect_left(a, x)
    if i >= len(a):
        i = len(a) - 1
    elif i and a[i] - x > x - a[i - 1]:
        i = i - 1
    return (i, a[i])


folder = 'Q:/sizz-rip/reddit_sub_sizz/'
img_paths = [os.path.normpath(i) for i in glob.glob(folder + '*.jpg')]

intensities = dict()

load_locally = True
overwrite_locally = False

if not load_locally:
    for i, img_path in enumerate(img_paths):
        try:
            image = io.imread(img_path)
            image = img_as_float(image)
            intensities[img_path] = np.mean(image)
        except Exception as e:
            print(e)
            pass

        print(i, len(img_paths))


    if overwrite_locally:
        with open('intensities.pkl', 'wb') as f:
            pickle.dump(intensities, f)


if load_locally:
    with open('intensities.pkl', 'rb') as f:
        intensities = pickle.load(f)

n = len(intensities)
img_width = 100
rows = n // 27
cols = 27

w = cols * img_width
h = rows * img_width

img = Image.new('RGB', (w, h))
draw = ImageDraw.Draw(img)

x = 0
y = 0
j = 0

intensities = {k: v for k, v in sorted(intensities.items(), key=lambda item: item[1], reverse=False)}
img_paths = np.asarray(list(intensities.keys()))
intensities = np.asarray(list(intensities.values()))
print(intensities)

noise = PerlinNoise()

rand_rows = list(range(rows))
rand_cols = list(range(cols))
shuffle(rand_rows)
shuffle(rand_cols)

for r in rand_rows:
    for c in rand_cols:
        x = c * img_width
        y = r * img_width

        noise_intensity = np.interp(noise([r / rows, c / cols]), [-0.7, 0.7], [0, 1])

        idx, _ = find_closest_index(intensities, noise_intensity)
        i, intensities = intensities[idx], np.delete(intensities, idx)
        path, img_paths = img_paths[idx], np.delete(img_paths, idx)

        try:
            sizz = Image.open(path)




            maxwidth = 150 + np.random.randint(-50, 50)
            maxheight = 150 + np.random.randint(-50, 50)

            ratio = min(maxwidth/sizz.width, maxheight/sizz.height)


            sizz = sizz.resize((int(sizz.width * ratio), int(sizz.height * ratio)), Image.ANTIALIAS)
            img.paste(sizz, (x, y))
            print(j+1, rows*cols, noise_intensity, i)
        except Exception as e:
            print(e)
            pass

        j += 1 


img.show()