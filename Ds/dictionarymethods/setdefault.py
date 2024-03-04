students_scores = {'alice':85,'bob':90,'charlie':78}

alice_scores = students_scores.setdefault('alice' , 0)

print(f"alice's score: {alice_scores}")

david_scores = students_scores.setdefault('jazil',100)

print(f"david's score: {david_scores}")

print("modified dictionary:",students_scores)