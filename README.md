This is a project to facilitate the adoption of dogs in public shelters. The idea is that the breed description of shelter dogs is frequently not very accurate, or sometimes people might want to have a dog that looks like the previous mutt they had, which does not fit any breed description. A Machine Learning algorithm provides the possiblity to see all available dogs that 'look like' a selected dog. By being able to always select the dog that comes closest to the wanted looks, the dog can be identified that fits the wishes most.

The files in this project do all the data preparation so that the website just needs to read and show them.

First, the data is prepared such that it is usable by the the Machine Learning algorithm. A table containing all the pictures and the descriptions of all available dogs is formatted and filled in the necessary way.

Then, the ML algorithm is trained on the given data.

Finally, the query script provides the possibility to query the model with a given input: Given an image of any dog, the query algorithm returns 5 images of different dogs that look most like the dog on the given picture.

All those scripts run independently, as long as the necessary data are provided (e.g. a model and data have to be provided for the query stage).
