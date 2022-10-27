from datetime import date


class ProfileConnections:
    def __init__(self, friends) -> None:
        today_date = date.today()

        self._friends = []
        for friend in friends:
            friend_data = {"name": friend, "date_affed": today_date}
            self._friends.append(friend_data)
