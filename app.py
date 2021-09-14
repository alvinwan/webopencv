import wcv2


def on_image(frame):
    return frame


if __name__ == '__main__':
    cap = wcv2.VideoCapture(on_image=on_image)
    cap.launch()