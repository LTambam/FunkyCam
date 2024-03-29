# FunkyCam

This is a simple package with one class, Funk, that recolors images to a smaller number of colors based on luminance of each pixel. It also extracts and thickens edges. Its fast enough it can even be used in real-time video!
The final product is a cartoon-like version of the original image or video. Like this:

![Image](./climb.png)

and this:

![Alt Text](./funkykillbill.gif)

## Getting Started

To install this package use the following command:

```bash
pip install funkycam
```

Examples are given in the "examples" folder to demonstrate how to use this package with a webcam, image files, and video files. But, to use this class all you need to do is:

```python
import cv2
from funkycam.funkycam import Funk

img = cv2.imread('example.jpg')

funk = Funk()
funky_img = funk.funkify(img)
```

**Note**: The code expects images that are read using cv2 which means they are in BGR format. If you read with other packages, images are often in RGB format. It may still work fine, but the calculations will be incorrect. You will probably want to flip the R and B channels. 
This can be accomplished on numpy array with array slicing:

```python
img_flipped = img[:,:,::-1] # flips third dim
```

## Customizing the Output 
To select colors, there are 3 options:
1. Use the seaborn color_palettes or matplotlib colormaps (https://matplotlib.org/stable/tutorials/colors/colormaps.html).
2. Manually input RGB colors in a list of lists. Resolution is 8 bits: 0-255 each color.
3. Specify "random_colors=True".

If you can't find colors you like, I recommend randomly generating colors and recording the colors that look good. The colors are printed every time it runs, but you can also access them from the Funk object with "funk.colors".

You can also specify the block size and blur value for finding edges, and blur value when finding colors. Increasing the block size seems to increase the thickness of the edges. Increasing blur values will reduce detail in the edges and colors, i.e. fewer edges and larger splotches of colors. These values depend a lot on the resolution of the image or video. **NOTE: The block size and blur values must be odd numbers**. 

## Other Notes
The luminance calculation is not real luminance, it is simplified so that it can recolor video in "real-time" (depends on image quality and number of colors chosen). To my understanding, actual luminance would require linearizing the image colors. this takes too long with Numpy. With GPU processing, I imagine this would be simple to implement. 

Turns out this method is a little bit like "cel-shading", a commonly used shader algorithm.
