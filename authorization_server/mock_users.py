class MockUsers:

    _users = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3'
    }

    @property
    def users(self):
        return self._users
