n = int(input())



votes = {}



for _ in range(n):

    candidate = input()

    votes[candidate] = votes.get(candidate, 0) + 1



max_votes = max(votes.values())

max_candidates = [candidate for candidate, count in votes.items() if count == max_votes]



print(min(max_candidates))
