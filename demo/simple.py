import wcv2

app = wcv2.WebApplication() # or wcv2.Flask()

@app.transform('Edge Detection')
def edge_detection(img, frame):
    return wcv2.transforms.edge_detection(img, frame)

if __name__ == "__main__":
    app.run()