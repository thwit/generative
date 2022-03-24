from PIL import Image
import random
import numpy as np
from perlin_numpy import generate_fractal_noise_2d

dark = (78, 77, 68)
light = (228, 211, 207)

def normalize(val, minn, maxx):
	if val < minn:
		return 0
	if val > maxx:
		return 1
	return (val - minn) / (maxx - minn)

def normalize_range(val, val_min, val_max, t_min, t_max):
	return (val - val_min) / (val_max - val_min) * (t_max - t_min) + t_min

def dist_sq(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return dx*dx + dy*dy


class Tree:
	def __init__(self, w, h):
		self.x = random.randint(0, w)
		self.y = random.randint(h // 2, h)
		self.w = random.randint(max(5, int(normalize(self.y, 0, h) * 25)), max(5, int(normalize(self.y, 0, h) * 35)))
		self.h = self.y + 1
		self.base = (self.x + self.w // 2, self.y)
		self.base_radius = random.randint(self.w * 15, self.w * 30)

	def tree_collide(self, x, y):
		return self.x < x < (self.x + self.w) and (self.y - self.h) < y < self.y

	def base_collide(self, x, y):
		return dist_sq(x,y, self.base[0], self.base[1]) <= self.base_radius

	def collide_point(self, x, y):
		return self.tree_collide(x, y) or self.base_collide(x, y)

	def get_color(self, x, y):
		if self.tree_collide(x, y):
			# probability that no color is chosen
			p = normalize(x, self.x, self.x + self.w)
			p /= 3
		else:
			p = normalize(dist_sq(x, y, self.base[0], self.base[1]), 0, self.base_radius)

		p_sky = normalize(self.h - y, 0, self.h)
		p_sky = normalize_range(p_sky, 0, 1, 0, 0.35)
		p_sky = 0
		color = random.choices([dark, light, light], [1-p, p, p_sky], k=1)
		return color[0]

	def draw(self, image):
		width, height = image.size
		for x in range(self.w):
			for y in range(self.y):
				ix, iy = self.x + x, self.y - y
				if 0 < ix < width and 0 < iy < height:
					image.putpixel((ix, iy), self.get_color(ix, iy))
					

class Grass:
	def __init__(self, w, h):
		self.w = w
		self.h = h
		self.noise = generate_fractal_noise_2d((w,h),(10, 10), 5)

	def get_color(self, x, y):
		p = normalize(self.noise[x][y], -np.sqrt(2)/2, np.sqrt(2)/2)
		color = random.choices([dark, False], [p, 1-p], k=1)
		return color[0]

def colorize(image, objects, grass):
	for obj in objects:
		obj.draw(image)

w, h = 640, 480
objects = [Tree(w, h) for _ in range(45)]
objects.sort(key=lambda obj: obj.y)
grass = Grass(w, h)

image = Image.new('RGB', (w, h), (228, 211, 207))
colorize(image, objects, grass)

image.show()