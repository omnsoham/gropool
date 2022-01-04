import random
from PIL import Image
import webbrowser
def randomfood():
    image1 = r'c:\Users\omk00\OneDrive\Desktop\gropool\Profile\profilepics\melon.png'
    image2 = r'C:\Users\omk00\OneDrive\Desktop\gropool\Profile\profilepics\_apples.png'
    image3 = r'C:\Users\omk00\OneDrive\Desktop\gropool\Profile\profilepics\_banana.png'
    image4 = r'C:\Users\omk00\OneDrive\Desktop\gropool\Profile\profilepics\_blueberries.png'
    image5 = r'C:\Users\omk00\OneDrive\Desktop\gropool\Profile\profilepics\mango.png'
    image6 = r'C:\Users\omk00\OneDrive\Desktop\gropool\Profile\profilepics\strawberry.png'
    i = random.choice([image1, image2, image3, image4, image5, image6])
    return i

