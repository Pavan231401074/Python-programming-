def coinChange(amount):

    # Available coin denominations

    coins = [1, 2, 3, 4]

    # Initialize a list to store the minimum number of coins for each amount from 0 to the target amount

    dp = [float('inf')] * (amount + 1)

    dp[0] = 0  # Base case: 0 coins needed to make amount 0

   

    # Iterate through all amounts from 1 to the target amount

    for i in range(1, amount + 1):

        # Iterate through all available coin denominations

        for coin in coins:

        	# If the current coin denomination is less than or equal to the current amount

        	if coin <= i:

            	# Update dp[i] to be the minimum between its current value and dp[i - coin] + 1

            	dp[i] = min(dp[i], dp[i - coin] + 1)

   

    # The result is stored at dp[amount]

    return dp[amount]

    amount = int(input())

    print(coinChange(amount))
