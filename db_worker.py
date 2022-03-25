import sqlite3


class LocationsDb:
    def __init__(self):
        self.con = sqlite3.connect("locations.db")
        self.cur = self.con.cursor()

    def select_category(self, category):
        returned = []
        result = self.cur.execute(f"""SELECT name, coords, address FROM locations 
        WHERE type = '{category}'""").fetchall()
        for name, coordinates, address in result:
            lat, lon = float(coordinates.split(",")[0]), float(coordinates.split(",")[1])
            returned.append([name, lat, lon, address])
        return returned


class PhotoDb:
    def __init__(self):
        self.con = sqlite3.connect("photo.db")
        self.cur = self.con.cursor()

    def set_photo(self, user_id, photo_id, lat, lon):
        self.cur.execute(f"""INSERT INTO photo (photo_id, user_id, lat_lon) VALUES ('{photo_id}', '{user_id}', '{lat}_{lon}')""")
        self.con.commit()


def select_best_location(lat1, lon1, array):
    new_array = []
    for name, lat, lon, address in array:
        new_array.append([(abs(lat1 - lat) + abs(lon1 - lon)) / 2, name, address])
    print(sorted(new_array))
    return sorted(new_array)[0]
