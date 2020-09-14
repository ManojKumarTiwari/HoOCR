# from image import text_detection
from cam import cam_text_detection

# td = text_detection.Detect()
# td.detect_words(img=r"data\1.png", disp_exctd_words=True)

td = cam_text_detection.Detect()
td.detect_charaters()
