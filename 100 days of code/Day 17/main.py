from self_class import User

user_1 = User("001", "Neymar")
user_2 = User("002", "Messi")

print(f"{user_1.name}:- following: {user_1.followings}, followers: {user_1.followers}")
print(f"{user_2.name}:- following: {user_2.followings}, followers: {user_2.followers}\n")
user_1.follow(user_2)
print(f"{user_1.name}:- following: {user_1.followings}, followers: {user_1.followers}")
print(f"{user_2.name}:- following: {user_2.followings}, followers: {user_2.followers}\n")
user_2.follow(user_1)
print(f"{user_1.name}:- following: {user_1.followings}, followers: {user_1.followers}")
print(f"{user_2.name}:- following: {user_2.followings}, followers: {user_2.followers}\n")