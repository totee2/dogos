import graphlab
from graphlab import SFrame


def resize_images(filename):
    images = graphlab.image_analysis.load_images(filename, format='auto', with_path=False, recursive=False,
                                                 ignore_failure=True, random_order=True)
    # firstImages = images[0:9]['image']
    new_images = list()
    new_images.append(graphlab.image_analysis.resize(images['image'], 32, 32, channels=4, decode=True))
    frame = SFrame(new_images)
    frame.save('mini')


if __name__ == "__main__":
    resize_images('full10')
