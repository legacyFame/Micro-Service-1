from face_recognition import load_image_file, face_encodings, compare_faces

def compare(img1, img2):
    known = load_image_file(img1)
    unknown = load_image_file(img2)
    known_encoding = face_encodings(known)[0]
    unknown_encoding = face_encodings(unknown)[0]
    results = compare_faces([known_encoding], unknown_encoding)
    return results[0]
    # face_distances = face_distance(known_encoding, unknown_encoding)
    # print(face_distances)

