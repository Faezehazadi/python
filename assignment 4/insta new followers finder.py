import instaloader
import getpass 


file = open("followers.txt" , "r")

oldfollowers=[]
for line in file :
    oldfollowers.append(line)
file.close()

L = instaloader.Instaloader()

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

L.login(username , password)
print("sucessfully login ✌️ 🌝 ✌️ ")

profile = instaloader.Profile.from_username(L.context , "faezeazd")

newfollowers = []
for follower in profile.get_followers():
    newfollowers.append(follower)

for new_follower in newfollowers:
    if new_follower not in old_followers:
        print(new_follower)


f = open("followers.txt" , "w")        
for follower in newfollowers:
    file.write(follower + "\n")
    file.close()