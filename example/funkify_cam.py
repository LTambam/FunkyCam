import cv2
from funkycam.funkycam import Funk

# Note: better lighting may improve results 

# default values
funk = Funk()

# specify Seaborn color_palette
# funk = Funk(n_colors = 7, sns_color_palette="ocean")

# manually choose colors
# colors = [[128, 0, 64],[255,255,255],[164,73,163],[39,127,255],[36,28,237],[201,174,255],[234,217,153]]
# funk = Funk(n_colors=7, color_list=colors)

# generate random colors
# funk = Funk(random_colors=True)

# choose the line_size, and blur values
# funk = Funk(line_size=19, line_blur_val=13, color_blur_val=9)

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not vid.isOpened():
    raise IOError("Cannot open webcam")

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 960)  # set new dimensionns to cam object (not cap)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
cv2.namedWindow("a", cv2.WINDOW_NORMAL)          
cv2.resizeWindow("a", 960, 540)
cv2.namedWindow("b", cv2.WINDOW_NORMAL)
cv2.resizeWindow("b", 960, 540)

while(True):
    ret, frame = vid.read()
    cartoon = funk.funkify(frame)

    cv2.imshow('a', cartoon)
    cv2.imshow('b', frame)
    if cv2.waitKey(1) & 0xFF == 27: # use esc to stop running
        break

vid.release()
cv2.destroyAllWindows()