import webopencv as wcv

app = wcv.WebApplication() # or wcv2.Flask()

@app.transform('Edge Detection')
def edge_detection(img, frame):
    return wcv.transforms.edge_detection(img, frame)

if __name__ == "__main__":
    app.run()