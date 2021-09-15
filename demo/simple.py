import webopencv as wcv

app = wcv.WebApplication(framerate=5)

@app.transform('Edge Detection', default=True)
def edge_detection(img, frame):
    return wcv.transforms.edge_detection(img, frame)

if __name__ == "__main__":
    app.run()