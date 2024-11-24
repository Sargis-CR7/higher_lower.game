
# from game_data import data
# import random
# import os

# def get_random_account():
#     """patahakan veradarcnuma akauntneric meky """
#     return random.choice(data)

# def format(account):
#     name=account["name"]
#     description=account["description"]
#     country=account["country"]
#     print(f"{name} is {description} from {country}")

# def chek_answer(guess,a_followers,b_followers):
#     """stugum e guessov a uni aveli shat followerner te b"""

#     if a_followers>b_followers:
#         return guess=="a"
#     else:
#         return guess=="B"


# def game():
#     score=0
#     game_should_cantinue=True
#     account_a=get_random_account()
#     account_b=get_random_account()

#     while game_should_cantinue:
#         account_a=account_b
#         account_b=get_random_account()

#         while account_a==account_b:
#             account_b=get_random_account()

#         print(f"Compare A:{format(account_a)}.")
#         print("vs")
#         print(f"Againist B: {format(account_b)}.")

#         guess=input("ov aveli shat folower uni A te B").lower
#         a_follower_count=account_a["follower_count"]
#         b_follower_count=account_b["follower_count"]
#         is_correct=chek_answer(guess,a_follower_count,b_follower_count)

#         os.system("cls")

#         if is_correct:
#             score+=1
#             print(f"du chisht es current score:{score}")

# game()


