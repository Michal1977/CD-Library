import json


class CdLibrary:
    def __init__(self):
        try:
            with open("cds.json", "r") as f:
                self.cds = json.load(f)
        except FileNotFoundError:
            self.cds = []

    def all(self):
        return self.cds

    def get(self, id):
        return self.cds[id]

    def create(self, data):
        data.pop('csrf_token')
        self.cds.append(data)

    def save_all(self):
        with open("cds.json", "w") as f:
            json.dump(self.cds, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.cds[id] = data
        self.save_all()

    def delete(self, id):
        cd = self.get(id)
        if cd:
            self.cds.remove(cd)
            self.save_all()
            return True
        return False


cds = CdLibrary()
