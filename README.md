# FunkyCam

This is a simple package with one class, Funky, that allows you to recolor images by brightness of each pixel and extract edges and thicken edges. 
The final product is a cartoon-like version of the original image. Like this:

![Image](./photo.png)

To install this package just run this command:

```bash
pip install funkycam
```

Simple examples are given in the "examples" folder to demonstrate how to use this package with a webcam, image files, and video files.

The luminance calculation is simplified so that it can recolor video in "realtime" (depends on image quality and number of colors chosen). 
To select colors, there are 3 options:
1. Use the seaborn color_palettes or matplotlib colormaps (https://matplotlib.org/stable/tutorials/colors/colormaps.html).
2. Manually input RGB colors in a list of lists. Resolution is 8 bits: 0-255 each color.
3. Specify "random_colors=True".

You can also specify the line size, blur value when finding edges, and blur value when finding colors. Generally, increasing blur values will reduce detail in the edges and colors, i.e. fewer edges and larger splotches of colors.

Turns out this is a little bit like "cel-shading", a commonly used shader algorithm.
