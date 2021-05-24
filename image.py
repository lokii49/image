class Image:
    "Holds all key values pairs"
    def __init__(self, image_id, image_name, x_coordinate, y_coordinate, image_type):
        self.image_id = image_id
        self.image_name = image_name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.image_type = image_type

    def apply_filter(self, filterpercentage):
        self.filterpercentage = filterpercentage
        self.x_coordinate += (self.x_coordinate*self.filterpercentage/100)
        self.y_coordinate += (self.y_coordinate*self.filterpercentage/100)

class Album:
    "Details of album and its attributes"
    def __init__(self, album_name, img_list):
        self.album_name = album_name
        self.img_list = img_list

    def calculate_coordinates(self, filterpercent, imagetype):
        self.filterpercent = filterpercent
        self.imagetype = imagetype
        details = []
        for item in self.img_list:
            if self.imagetype == item.image_type:
                item.x_coordinate += (item.x_coordinate * self.filterpercent / 100)
                item.y_coordinate += (item.y_coordinate * self.filterpercent / 100)
                details.append(item.image_name)
                details.append(item.x_coordinate)
                details.append(item.y_coordinate)
        return details

if __name__ == '__main__':
    num = int(input())
    img_list = []
    for i in range(num):
        image_id = int(input())
        image_name = input()
        x_coordinate = int(input())
        y_coordinate = int(input())
        image_type = input()
        img_list.append(Image(image_id, image_name, x_coordinate, y_coordinate, image_type))
    album_name = None
    imagetype = input()
    filterpercent = int(input())
    obj = Album(album_name, img_list)
    result = obj.calculate_coordinates(filterpercent, imagetype)
    print(' '.join(map(str, result)))