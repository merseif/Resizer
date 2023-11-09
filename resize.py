from abc import ABC, abstractmethod  
class Resize(ABC):
    def __init__(self, height, width, image_path):
        self.height = int(height)
        self.width = int(width)
        self.image_path = image_path

    @abstractmethod
    def resize(self):
        pass