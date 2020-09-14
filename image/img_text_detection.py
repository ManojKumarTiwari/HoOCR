# import necessary packages
import pytesseract
import cv2

class Detect():
    def __init__(self):
        print("Welcome to detecting text from an image")
        try:
            # initialize our installed tesseract executable
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        except Exception as e:
            print(e)

    def detect_charaters(self, img, disp_exctd_char=True):
        """
        detects individual characters from an image
        :param img: path to image file
        :param disp_exctd_char: if you want to display extracted characters on the image, set the value to "True" otherwise set to "False"
        :return: displays image in a new window
        """

        try:
            # read the image
            img = cv2.imread(img)
        except Exception as e:
            print(e)
        try:
            # cv2 reads in BGR format but tesseract works in RGB format
            # hence we need to covert
            img = cv2.cvtColor(img,
                               cv2.COLOR_BGR2RGBA)

            # # print the extracted text in image
            # print(pytesseract.image_to_string(img))

            # # print (x, y) co-ordinates, w (width) and h (height) of each extracted character
            # print(pytesseract.image_to_boxes(img))

            # DETECTING CHARACTERS
            # draw boxes around characters
            # get the height and width of original image
            hImg, wImg, _ = img.shape
            boxes = pytesseract.image_to_boxes(img)
            for b in boxes.splitlines():
                b = b.split(" ")
                x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
                # Note: pytesseract calculates height from bottom for this function and cv2 expects it from the top
                # Hence we need to substarct y co-ordinate and height from the original image height
                cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)
                if disp_exctd_char == True:
                    cv2.putText(img, b[0], (x, hImg -y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

            # show the image
            cv2.imshow("image", img)

            # wait untill any key is pressed
            cv2.waitKey(0)

        except Exception as e:
            print(e)

    def detect_words(self, img, disp_exctd_words=True):
        """
        detects individual words from an image
        :param img: path to image file
        :param disp_exctd_words: if you want to display extracted characters on the image, set the value to "True" otherwise set to "False"
        :return: displays image in a new window
        """

        try:
            # read the image
            img = cv2.imread(img)
        except Exception as e:
            print(e)

        try:
            # DETECTING WORDS
            boxes = pytesseract.image_to_data(img)
            for x, b in enumerate(boxes.splitlines()):
                # 0th index is header and we don't want
                if x != 0:
                    b = b.split()
                    # if any word is detected the lenght of b will be 12
                    if len(b) == 12:
                        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
                        if disp_exctd_words == True:
                            cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

            # show the image
            cv2.imshow("image", img)

            # wait untill any key is pressed
            cv2.waitKey(0)

        except Exception as e:
            print(e)



    # NOTE: THIS IS NOT WORKING
    # # DETECTING ONLY NUMBERS
    # conf = "--oem 3 --psm 6 outputbase digits"
    # # See documentation to get more things to do!!
    # boxes = pytesseract.image_to_data(img, config=conf)
    # for x, b in enumerate(boxes.splitlines()):
    #     # 0th index is header and we don't want
    #     if x != 0:
    #         b = b.split()
    #         # if any word is detected the lenght of b will be 12
    #         if len(b) == 12:
    #             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
    #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
    #             cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

    # # show the image
    # cv2.imshow("image", img)
    #
    # # wait untill any key is pressed
    # cv2.waitKey(0)






