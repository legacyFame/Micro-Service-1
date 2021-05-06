import os
from base64 import b64decode

from flask import Flask, request

from src import compare

app = Flask(__name__)


def image_process(f_name, im_b64):
    img_data = b64decode(im_b64)
    f_name = "data/" + f_name
    with open(f_name, 'wb') as f:
        f.write(img_data)
    return f_name


@app.route('/')
def home():
    return "Micro-Service 1 is running"


@app.route('/face', methods=['POST'])
def face():
    print(request.data)
    data = request.form.to_dict(flat=False)
    print(data)
    images = data["files"]
    # print(images)
    files = [(data["img1"][0], images[0]), (data["img2"][0], images[1])]
    # print(files[0])
    img1, img2 = image_process(*files[0]), image_process(*files[1])
    res = compare(img1, img2)
    os.remove(img1)
    os.remove(img2)
    return str(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=40544)
