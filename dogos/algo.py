import graphlab
from graphlab import SArray,SFrame


def train_model(filename):
    # load already prepared data in form of an SFrame
    image_train = graphlab.SFrame(filename)
    # load the pre-trained model
    loaded_model = graphlab.load_model('model/')
    # extract features of the model on the given pictures
    image_train['deep_features'] = loaded_model.extract_features(SFrame(image_train))
    # add ids to the SFrame to be able to find the closest images
    ids = SArray(list(range(0,len(image_train))))
    image_train.add_column(ids, name='id')
    # print image_train.head()
    # train the NN model on the extracted features
    knn_model = graphlab.nearest_neighbors.create(image_train, features=['deep_features'], label='id')
    return knn_model, image_train


if __name__ == "__main__":
    # for training a model and saving it, execute the following 3 lines
    model_to_save, images_to_save = train_model('prepared_data/')
    model_to_save.save('my_model')
    images_to_save.save('my_images')
