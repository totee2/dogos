import graphlab


def get_images_from_ids(query_result, images):
    return images.filter_by(query_result['reference_label'],'id')


def query_model(dogo, model, images):
    neighbours = get_images_from_ids(model.query(dogo, k=20), images)
    return neighbours


if __name__ == "__main__":
    # load a pre-trained model and prepared SFrame with images etc
    images = graphlab.load_sframe('my_images')
    model = graphlab.load_model('my_model')
    print images[images['name'] == 'BOOBA']
    #print images
    #print model

    # select a 'starting' dog
    dogo = images[6:7]
    print "printing drogo"
    print model.query(dogo)
    print dogo
    # dogo['image'].show()
    #print dogo
    #print model.query(dogo)
    # print the image of the starting dog
    for dog in dogo:
        dog['image'].show()

    # find the closest dog to the starting dog
    neighbours = query_model(dogo, model, images)

    # create a list with the content of the 'images' column of the shown dogs. This helps to prevent having
    # multiple pictures of the same dog in the output
    print dogo['images'][0][0]
    shown_dogs = {dogo['images'][0][0]}
    print shown_dogs

    # select one picture of the 5 closest dogs and print it
    for i in range (0, len(neighbours)):
        print i
        if len(shown_dogs) < 6:
            print neighbours[i]['images']
            if neighbours[i]['images'][0] not in shown_dogs:
                neighbours[i]['image'].show()
                shown_dogs.add(neighbours[i]['images'][0])
                print shown_dogs
        else:
            break
    #print neighbours
    #print neighbours

    print "printing neighbours"
    #for neighbour in neighbours:
    #    neighbour['image'].show()
        # print neighbour['image'].dtype()