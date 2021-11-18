"""BONUS : analyser les images d'une pochette d'album pour en extraire les objets.

@author: Djamel BOUSFIRA
"""

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Prairie63-e2fd7c261c82.json"


class IA_Vision(object):
    """Detect objects from a given image.

    Args:
        object (image): image to analyze

    """

    def __init__(self, img):
        """Initialize the image and detect the objects inside via Google Vision API.

        Args:
            img (str): image path

        """
        self.img = img
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        # The name of the image file to annotate
        file_name = os.path.abspath(img)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)

        print('Labels:')
        self._labels = {}
        for label in response.label_annotations:
            self._labels[label.description] = "{:.0%}".format(label.score)

    @property
    def labels(self):
        """Get labels.

        Returns:
            Dict[Label, Score]

        """
        return self._labels
