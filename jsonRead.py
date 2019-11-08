import json


class read_json_data:

    def json_Reads(self, str):
        with open('data.json') as json_file:
            data = json.load(json_file)
            for p in data['paths']:
                pass
        return p[str]