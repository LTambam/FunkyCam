import cv2
from funkycam.funkycam import Funk

# specify Seaborn color_palette https://matplotlib.org/stable/tutorials/colors/colormaps.html
funk = Funk(n_colors=8, sns_color_palette='inferno', line_size=11, edge_blur_val=5, color_blur_val=7)

# manually choose colors
# colors = [[128, 0, 64],[255,255,255],[164,73,163],[39,127,255],[36,28,237],[201,174,255],[234,217,153]]
# funk = Funk(color_list=colors, line_size=11, edge_blur_val=5, color_blur_val=7)

# generate random colors
# funk = Funk(n_colors=7, random_colors=True, line_size=11, edge_blur_val=5, color_blur_val=7)

vid_capture = cv2.VideoCapture('./example/resources/KillBill.mp4')

frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)
fps = vid_capture.get(cv2.CAP_PROP_FPS)

output = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (frame_width, frame_height))

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    
    if ret == True:
        # Write the frame to the output files
        funky_img = funk.funkify(frame)
        output.write(funky_img)
    else:
        print('Stream disconnected')
        break
    
vid_capture.release()
output.release()
