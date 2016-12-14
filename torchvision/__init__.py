from torchvision import models
from torchvision import datasets
from torchvision import transforms
from torchvision import utils


image_backend = 'PIL'
"""
Specifies the package used to load images.

Options are 'PIL' and 'accimage'. The :mod:`accimage` package uses the
Intel IPP library. It is generally faster than PIL, but does not support as
many operations.
"""


def get_image_backend():
    return image_backend
