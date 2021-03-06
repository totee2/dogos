from pymongo import MongoClient
import time
import datetime
import graphlab
from graphlab import SFrame
import argparse

path = ''


def get_images_from_ids(query_result, images):
    return images.filter_by(query_result['reference_label'], 'id')


def query_model(dogo, model, images):
    neighbours = get_images_from_ids(model.query(dogo, k=20), images)

    image_list = SFrame(data=None)

    shown_dogs = {dogo['images'][0][0]}

    for i in range(0, len(neighbours)):
        if len(shown_dogs) < 6:
            if neighbours[i]['images'][0] not in shown_dogs:
                # neighbours[i]['image'].show()
                dogo_clone = neighbours[i:i+1].copy()
                image_list = image_list.append(SFrame(dogo_clone))
                shown_dogs.add(neighbours[i]['images'][0])
        else:
            break

    return image_list


def make_json(dog_data, dog_id):
    response = {"query": dog_id}
    response['timestamp'] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    dog_json = {}
    for i in range(0, len(dog_data)):
        dog_info = {}
        dog_info['id'] = dog_data[i]['id']
        dog_info['dpt'] = dog_data[i]['refuge_name'][:2]
        dog_info['image_filename'] = dog_data[i]['image_filename']
        dog_info['name'] = dog_data[i]['name']
        dog_info['url'] = dog_data[i]['url']
        dog_json['dog' + str(i)] = dog_info
    response['response'] = dog_json

    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Name of database')
    parser.add_argument('db_name')
    args = parser.parse_args()

    images = graphlab.load_sframe(path + 'my_images')
    model = graphlab.load_model(path + 'my_model')
    client = MongoClient("localhost")
    db = client.dogos
    db.dogos_temp.drop()

    # Issue the serverStatus command and print the results
    # serverStatusResult=db.command("serverStatus")
    # pprint(serverStatusResult)

    num_images = len(images)

    for dog_id in xrange(num_images):
        print "Query %d in %d" % (dog_id, num_images)
        dogo = images[dog_id: dog_id + 1]
        neighbours = query_model(dogo, model, images)
        resp = db.dogos_temp.insert_one(make_json(dogo.append(neighbours), dog_id))

    if args.db_name == 'dogos':
        db.dogos.drop()
        db.dogos_temp.rename(args.db_name)
        db.dogos.create_index('query')
    else:
        db.gatos.drop()
        db.dogos_temp.rename(args.db_name)
        db.gatos.create_index('query')
