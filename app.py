from wcv2 import App

app = App()

@app.transform('Swap Faces')
def face_swap(frame):
    return frame

if __name__ == '__main__':
    app.run()