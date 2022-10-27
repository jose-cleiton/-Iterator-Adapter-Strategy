from datetime import date


class ProfileConnections:
    def __init__(self, friends) -> None:
        today_date = date.today()

        self._friends = []
        for friend in friends:
            friend_data = {"name": friend, "date_affed": today_date}
            self._friends.append(friend_data)

    def __iter__(self):
        return ProfilIterator(self._friends)


class ProfilIterator:
    def __init__(self, friends) -> None:
        self._cont = 0
        self.friends = friends

    def __next__(self):
        next = self.friends[self._cont]
        self._cont += 1
        return next
