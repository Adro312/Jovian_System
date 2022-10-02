# Import all libraries
# cv2 is used for cognitive visual, and allow us to read images as arrays
# numpy is excellent to process big data in a short period of time

import cv2
import numpy

def giveColor(redImgPath, greenImgPath, blueImgPath, lastId):

    blue_path = redImgPath
    green_path = greenImgPath
    red_path = blueImgPath

    blue = cv2.imread(f'{blue_path}')
    green = cv2.imread(f'{green_path}')
    red = cv2.imread(f'{red_path}')

    ###################################################################

    blue = cv2.resize(blue, (400, 320))
    green = cv2.resize(green, (400, 320))
    red = cv2.resize(red, (400, 320))

    img_merged = cv2.merge([blue[:,:,0], green[:,:,1], red[:,:,2]])

    ###################################################################

    cv2.imwrite(f'./images/galery/image{lastId}.png', img_merged)

    return f'./images/galery/image{lastId}.png'
