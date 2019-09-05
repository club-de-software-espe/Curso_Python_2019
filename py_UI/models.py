class User():
    def __init__(self, ci, name, gender):
        self.ci = ci
        self.name = name
        self.gender = gender

    def __repr__(self):
        return 'Cédula: {}\nNombre: {}\nGénero: {}'.format(self.ci, self.name,
                                                           self.gender)


class UsersGroup():
    def __init__(self):
        self.users = {}

    def add(self, user, update=False):
        if (user.ci in self.users and update) or (user.ci not in self.users):
            self.users.update({user.ci: user})
            return True
        else:
            return False

    def delete(self, ci):
        if ci in self.users:
            self.users.pop(ci)
            return True
        else:
            return False

    def search(self, ci):
        if ci == '':
            return self.__repr__()
        if ci in self.users:
            return self.users.get(ci).__repr__()
        else:
            return False

    def __repr__(self):
        return str(self.users)
