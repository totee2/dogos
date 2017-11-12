import numpy
import graphlab
from graphlab import SFrame, SArray

path='/home/dogo/spa-scrapper/spa/'
images_path = '/home/dogo/spa-scrapper/spa/images/'
def append_images(json_file):
    # we fill an SFrame with all the given metadata of the dogs
    meta = SFrame.read_json(json_file, orient='records')
    # this is the SFrame that we will fill with the data plus the image, which will be saved in the final file
    image_list = SFrame(data=None)
    # for each image in the images column in the meta SFrame, we add one line in the final SF with one image per line
    for i in range(0,len(meta)-1):
        dogo = meta[i:i+1]
        for image in dogo['images'][0]:
            #print image
            dogo_clone = dogo.copy()
            dogo_clone.add_column(SArray([(graphlab.Image(images_path + image))]), name='image')
            dogo_clone.add_column(SArray([image]), name='image_filename')
            image_list = image_list.append(SFrame(dogo_clone))
    print '=========================='
    #print image_list
    image_list.save(filename='prepared_data/')


if __name__ == "__main__":
    # transmit the json file from which the dogo images are taken
    append_images(path + 'output.json')
