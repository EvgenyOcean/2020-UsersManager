import json

class UserHandler:
    '''
    Handles database interactions.
    '''
    def __init__(self, path='./db.json'):
        self.path = path

    def write_json(self, json_data):
        with open(self.path, 'w') as file_out:
            json.dump(json_data, file_out, indent=4)

    def read_json(self):
        with open(self.path) as file_in:
            try:
                return json.load(file_in)
            except json.decoder.JSONDecodeError:
                return [[], {"next_id": 0}]

    def add_user(self, new_user):
        data = self.read_json()
        # Validating Username
        for user in data[0]:
            if user['username'] == new_user['username']:
                return 'That username already exists' 

        next_id = data[1]['next_id']
        new_user.update({'id': next_id})
        data[0].append(new_user)
        data[1]['next_id'] = next_id + 1
        self.write_json(data)
        return 'Success'

    def delete_user(self, id):
        # What if user does not exist
        data = self.read_json()
        data[0] = [user for user in data[0] if user['id'] != id]
        self.write_json(data)
        return 'User with specified id has been deleted'

    def change_user(self, id, new_user):
        data = self.read_json()
        for user in data[0]:
            if user['id'] == id:
                user['username'] = new_user['username']
                user['age'] = new_user['age']
        self.write_json(data)
        return 'User\'s profile has been updated'

    def get_user(self, id):
        data = self.read_json()
        try:
            user = filter(lambda user: user['id'] == id, data[0]).__next__()
            return user
        except StopIteration: 
            return 'User with such id does not exist'