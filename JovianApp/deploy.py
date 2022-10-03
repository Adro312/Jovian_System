# Import all libraries
# cv2 is used for cognitive visual, and allow us to read images as arrays
# numpy is excellent to process big data in a short period of time

import cv2
import numpy as np
from PIL import Image as PilImage
from matplotlib.animation import PillowWriter
from wand.image import Image

def giveColor(redImgPath, greenImgPath, blueImgPath, mapProjected, lastId):

    blue_path = blueImgPath
    green_path = greenImgPath
    red_path = redImgPath 
    mapprojected = mapProjected

    blue = cv2.imread(f'{blue_path}')
    green = cv2.imread(f'{green_path}')
    red = cv2.imread(f'{red_path}')

    ###################################################################

    # Este código es para dar un cero perfecto y que la imagen filtrada no presente graves daños

    zero_channel_blue = np.zeros(blue.shape[0:2], dtype="uint8")
    zero_channel_green = np.zeros(green.shape[0:2], dtype="uint8")
    zero_channel_red = np.zeros(red.shape[0:2], dtype="uint8")

    # Aquí es donde se cargan en su respectivo canal para aplicar la máscara de color

    blue = cv2.merge([blue[:,:,2], zero_channel_blue, zero_channel_blue])
    green = cv2.merge([zero_channel_green, green[:,:,2], zero_channel_green])
    red = cv2.merge([zero_channel_red, zero_channel_red, red[:,:,2]])

    # Se crea una nueva imagen que contendrá la imagen ya con la máscara de color, se tiene qué guardar a fuerzas
    # debido a que en el siguiente paso deberá cargar un archivo

    cv2.imwrite("images/deploy/b.png", blue)
    cv2.imwrite("images/deploy/g.png", green)
    cv2.imwrite("images/deploy/r.png", red)

    # Este with image viene por parte de la librería wand
    # Se le aplica un filtro hsl con valores predeterminados que ayudarán al proceso de la imagen

    with Image(filename ='images/deploy/b.png') as image:
        with image.clone() as modulate:
            modulate.modulate(50, 120, -100)
            modulate.save(filename ='images/deploy/modulated-blue.jpg')

    with Image(filename ='images/deploy/g.png') as image:
        with image.clone() as modulate:
            modulate.modulate(60, 110, -100)
            modulate.save(filename ='images/deploy/modulated-green.jpg')

    with Image(filename ='images/deploy/r.png') as image:
        with image.clone() as modulate:
            modulate.modulate(75, 75, -100)
            modulate.save(filename ='images/deploy/modulated-red.jpg')

    # Se abren las imágenes en su respectiva variable
    # Se parten las imágenes para recibir su respectivo canal de color
    # En este caso B = Blue, G = Green, R = Red (BGR)

    blue = PilImage.open(r"images/deploy/modulated-blue.jpg")
    blue.load()
    _, _, blueb = blue.split()

    green = PilImage.open(r"images/deploy/modulated-green.jpg")
    green.load()
    _, greeng, _ = green.split()

    red = PilImage.open(r"images/deploy/modulated-red.jpg")
    red.load()
    redr, _, _ = red.split()

    # Se crea una imagen totalmente transparente que nos ayudará a rellenar los canales de los cuales no tengamos el color

    empty = PilImage.new('L',blue.size)

    # Primero se combinan los canales rojos y verdes, nos darán de resultado una imagen amarilla

    mix1 = PilImage.merge('RGB', (redr, greeng, empty))

    # Esa misma imagen creada se dividirá para obtener sus canales de color

    mix1r, mix1g, _ = mix1.split()

    # Ahora se crea una segunda imagen y se le aplica el filtro de color azul

    mix2 = PilImage.merge('RGB', (mix1r, mix1g, blueb))

    # Una vez que tengamos este resultado, haremos un último paso
    # Tomaremos la imagen con el resultado esperado y la convertimos a RGBA

    mapJpg = PilImage.open(f'{mapprojected}').convert("RGBA")

    datas = mapJpg.getdata()

    newData = []

    # Se hicieron pruebas y a cada pixel se le agregó un valor en alpha de 150, lo cual se hará un poco transparente

    for item in datas:
        newData.append((item[0], item[1], item[2], 150))

    mapJpg.putdata(newData)

    # Una vez que la imagen fue creada, solamente se encimará con la otra imagen, y listo
    # Ahora nuestra imagen está llena de color

    mix2.paste(mapJpg, (0, 0), mapJpg)

    ###################################################################

    mix2.save(f'./images/gallery/image{lastId}.png')

    return f'./images/gallery/image{lastId}.png'
