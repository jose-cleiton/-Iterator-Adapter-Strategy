from social_network.profile import ProfileConnections


def test_can_use_instance_in_loop():
    friends = ["Rolf", "Jose", "Charlie"]
    profile = ProfileConnections(friends)

    for friend in profile:
        assert friend["name"] in friends


def test_can_interate_over_instance():
    friends = ["Rolf", "Jose", "Charlie"]
    connection = ProfileConnections(friends)

    con_iter = iter(connection)  # connection.__iter__()

    next_friend = next(con_iter)
    assert friends[0] == next_friend["name"]

    next_friend = next(con_iter)
    assert friends[1] == next_friend["name"]
