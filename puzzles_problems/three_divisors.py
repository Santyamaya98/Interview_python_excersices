
class Solution:
	@staticmethod
	def threeDivisors(query, q):
		"""
		You are given a list of q queries, and for each query, 
		an integer n is provided. The task is to find how many
		numbers less than or equal to n have exactly 3 divisors.
		"""
		divisors=[]
		count = 0
		for i, num in enumerate(query):
			while count <= 3 or numb == 0:
				numb = query[i]
				if numb % q == 0:
					divisors.append(query[i])
					count = 0
					break
				else:
					numb -= 1
		return len(divisors)
            

print(Solution.threeDivisors([10, 6], 2))

print(Solution.threeDivisors([6], 2))