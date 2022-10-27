from social_network.profile import ProfileConnections


def test_can_use_instance_in_loop():
    friends = ["Rolf", "Jose", "Charlie"]
    profile = ProfileConnections(friends)

    for friend in profile:
        assert friend["name"] in friends
