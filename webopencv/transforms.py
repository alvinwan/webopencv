import cv2


_transforms = {}


def add_transform(name, transform):
    _transforms[_normalize_transform_name(name)] = {
        "name": name,
        "func": transform
    }


def remove_transform(name):
    _transforms.pop(_normalize_transform_name(name))


def get_transform_ids():
    return list(map(_normalize_transform_name, _transforms))


def get_transform(name):
    return _transforms[_normalize_transform_name(name)]


def _normalize_transform_name(name):
    return name.lower().replace(" ", "-")


def cartoon(img, frame):
    # prepare color
    img_color = cv2.pyrDown(cv2.pyrDown(img))
    for _ in range(6):
        img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
    img_color = cv2.pyrUp(cv2.pyrUp(img_color))

    # prepare edges
    img_edges = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_edges = cv2.adaptiveThreshold(
        cv2.medianBlur(img_edges, 7),
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        2,
    )
    img_edges = cv2.cvtColor(img_edges, cv2.COLOR_GRAY2RGB)

    # combine color and edges
    img = cv2.bitwise_and(img_color, img_edges)
    return img


def edge_detection(img, frame):
    img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
    return img


def rotate(img, frame):
    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), frame.time * 45, 1)
    img = cv2.warpAffine(img, M, (cols, rows))
    return img