import numpy
import graphlab
from graphlab import SFrame, SArray

def appendImages(json_file):
    meta = SFrame.read_json(json_file, orient='records')
    imageList = SFrame(data=None)
    for i in range(0,len(meta)-1):
        dogo = meta[i:i+1]
        print(type(dogo))
        for image in dogo['images'][0]:
            dogo_clone = dogo.copy()
            dogo_clone.add_column(SArray([(graphlab.Image(image))]), name='image')
            imageList = imageList.append(SFrame(dogo_clone))
    print '=========================='
    print imageList
    imageList.save(filename='prepared_data/')






if __name__ == "__main__":
    appendImages('output10.json')