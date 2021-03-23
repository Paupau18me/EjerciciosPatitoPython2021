while True:
      try:
            nums = input()
            sum=0
            for n in nums:
                if int(n)%2 == 0:
                    sum = sum + int(n)
            print(sum)
      except EOFError:
            break