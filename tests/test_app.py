from src import compare
import  os

def test_compare():
    img1 = "./tests/data/biden.jpg"
    img2 = "./tests/data/unknown.jpeg"
    assert compare(img1, img2) == True
