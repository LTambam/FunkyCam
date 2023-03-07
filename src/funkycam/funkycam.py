import os
import random
import cv2
import numpy as np
import seaborn as sns
from PIL import Image

class Funk(object):
    def __init__( self, n_colors:int = 7, sns_color_palette:str = "rainbow",
                    random_colors:bool = False, color_list:list = [],
                    line_size:int = 17, edge_blur_val:int = 9, color_blur_val:int = 27 ):
        self.n_colors = n_colors
        assert n_colors > 1, f"Number of colors must be greater than 1. Input was {n_colors}"

        self.color_palette = sns_color_palette
        self.random_colors = random_colors
        self.color_list = color_list
        if len(color_list) > 0:
            self.n_colors = len(color_list)

        self.line_size = line_size
        self.edge_blur_val = edge_blur_val
        self.color_blur_val = color_blur_val

        self.luminance_mult = [0.114, 0.587, 0.299]
        # self.luminance_mult = [0.0722, 0.7152, 0.2126] # alternative luminance formula

        self.colors, self.lightness = self._color_lightness()

    def _color_lightness(self):
        if(self.random_colors):
            colors = np.random.randint(0, 255, size=(self.n_colors,3))
        elif(len(self.color_list) == self.n_colors):
            color_pal = np.uint8(np.array(self.color_list))
            colors = color_pal[:,::-1] # get bgr
        else:
            palette = sns.color_palette(self.color_palette, self.n_colors)
            color_pal = np.uint8(np.multiply(np.array(palette), 255))
            colors = color_pal.copy()
            colors = color_pal[:,::-1] # get bgr

        lightness = np.uint8(np.sum(np.multiply(colors, self.luminance_mult), axis=1))
        colors = colors[np.argsort(lightness)]
        lightness = np.sort(lightness)

        print("Colors:\n", colors)

        return colors, lightness

    def edge_mask(self, img):
        # get the edges of the image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (self.edge_blur_val, self.edge_blur_val), -1)
        edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, self.line_size, self.edge_blur_val)
        return edges

    def pick_color(self, img, colorsums, num_colors):
        # reassigning pixels based on brightness
        # adjusting the colors based on how brightness is visually seen by humans
        sumX = np.sum(np.multiply(img, self.luminance_mult), axis=1)

        condlist = []
        choicelist = []
        for i in range(num_colors):
            choicelist.append(i)
            if i < num_colors-1:
                condlist.append(sumX<colorsums[i])
            else:
                condlist.append(sumX>colorsums[i])

        inds = np.select(condlist, choicelist)

        return inds

    def funkify(self, img):

        # Read in foreground image from the 'examples/resources' folder
        background_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        background_img = Image.fromarray(background_img)
        foreground_img_path = '../../example/resources/pic.jpeg'
        foreground_img = Image.open(foreground_img_path)

        # Convert image to RGBA because we need to control the alpha parameter when making the image
        # transparent
        foreground_img = foreground_img.convert("RGBA")
        background_img = background_img.convert("RGBA")

        # Blend foreground image with the background image
        # The random number between 0 and 1 controls how transparent the foreground image is on the
        # background
        background_img = background_img.resize(foreground_img.size)
        img_blend = Image.blend(background_img, foreground_img, random.uniform(0, 1))

        # Save image before funkifying (to check it out)
        img_blend.save("new.png","PNG")
        img_blend = cv2.imread('new.png')

        edges = self.edge_mask(img_blend)
        blur = cv2.GaussianBlur(img_blend,(self.color_blur_val, self.color_blur_val), sigmaX=0, sigmaY=0)
        indices = self.pick_color(blur.reshape((-1, 3)), self.lightness, self.n_colors)
        recolored = np.uint8(self.colors[indices].reshape(blur.shape))

        cartoon = cv2.bitwise_and(recolored, recolored, mask=edges)

        return cartoon
