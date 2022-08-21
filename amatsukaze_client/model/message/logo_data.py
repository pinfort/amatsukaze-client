from dataclasses import dataclass


@dataclass
class LogoData():
    service_id: int
    file_name: str
    image_width: int
    image_height: int

    # image: BitmapFrame どうするか考える
