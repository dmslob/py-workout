users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j])  # add i as a friend of j
    users[j]["friends"].append(users[i])  # add j as a friend of i

print(users)


def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"])


friends_of_user = [number_of_friends(user) for user in users]
print(type(friends_of_user))

total_connections = sum(friends_of_user)
print(total_connections)

num_users = len(users)
print(num_users)

avg_connections = total_connections / num_users
print(avg_connections)


# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)

