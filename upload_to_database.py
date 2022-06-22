import streamlit_authenticator as stauth

import database as db

usernames = ["LLLERENAL", "rmiller","Cardenas", "mgarciab", "jbravob", "amedinav"]
names = ["Luis Llerena Lagunes", "Rebecca Miller", 'Giancarlos Cardenas', "Mauro Arturo Garcia", "John Jairo Bravo", "Alfredo"]
passwords = ["Smnz$1304$La", "def456", "cardenas10", "Gaddiel$14", "48557917", "Gaddiel$14"]
hashed_passwords = stauth.Hasher(passwords).generate()


for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)