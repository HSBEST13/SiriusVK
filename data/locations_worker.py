import sqlite3


class LocationsDb:
    def __init__(self):
        self.con = sqlite3.connect("data//locations.db")
        self.cur = self.con.cursor()

    def select_category(self, category):
        returned = []
        result = self.cur.execute(f"""SELECT name, coords, address FROM locations 
        WHERE type = '{category}'""").fetchall()
        for name, coordinates, address in result:
            lat, lon = float(coordinates.split(",")[0]), float(coordinates.split(",")[1])
            returned.append([name, lat, lon, address])
        return returned


def select_best_location(lat1, lon1, array):
    new_array = []
    for name, lat, lon, address in array:
        new_array.append([(abs(lat1 - lat) + abs(lon1 - lon)) / 2, name, address])
    print(sorted(new_array))
    return sorted(new_array)[0]