import graphlab
from graphlab import SArray,SFrame



def train_model(filename):

    image_train = graphlab.SFrame(filename)

    loaded_model = graphlab.load_model('model/')
    image_train['deep_features'] = loaded_model.extract_features(SFrame(image_train))
    ids = SArray(list(range(0,len(image_train))))
    print ids
    image_train.add_column(ids, name='id')
    print image_train.head()
    knn_model = graphlab.nearest_neighbors.create(image_train, features=['deep_features'], label='id')
    return (knn_model, image_train)


def get_images_from_ids(query_result, images):
    return images.filter_by(query_result['reference_label'],'id')


def query_model(dogo, model):
    neighbours = get_images_from_ids(model.query(dogo), images)
    

if __name__ == "__main__":
    model, images = train_model('prepared_data/')
    print images
    print model
    dogo = images[7:8]
    print dogo
    print model.query(dogo)
    neighbours = get_images_from_ids(model.query(dogo), images)
    print neighbours
    for neighbour in neighbours:
        neighbour['image'].show()
