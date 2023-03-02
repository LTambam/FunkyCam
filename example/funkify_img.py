import cv2
from funkycam.funkycam import Funk

# manually choose colors
colors = [[128, 0, 64],[255,255,255],[164,73,163],[39,127,255],[36,28,237],[201,174,255],[234,217,153]]
funk = Funk(color_list=colors, line_size=15, edge_blur_val=7, color_blur_val=11)

# specify Seaborn color_palette
# funk = Funk(n_colors=6, sns_color_palette='inferno', line_size=13, edge_blur_val=7, color_blur_val=11)

# generate random colors
# funk = Funk(random_colors=True)

# choose the line_size, and blur values
# funk = Funk(line_size=19, line_blur_val=13, color_blur_val=9)

img = cv2.imread('./resources/willem.jpg')

funky_img = funk.funkify(img)

cv2.imwrite('./willemout.jpg', funky_img)