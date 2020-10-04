if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    a=max(arr)
    for i in range(n-1,-1,-1):
        if arr[i] != a:
            print(arr[i])
            break

#Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score. You are given 'n' scores. Store them in a list and find the score of the runner-up.
#In this approach the array elements are referenced from the end and the runnerup score is printed. As, there can be duplicates.
#If all the scores are unique then runnerscore can be 'arr[n-2]' after sorting.