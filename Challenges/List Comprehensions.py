if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print ([ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j + k ) != n )])

#Let's learn about list comprehensions! You are given three integers 'X,Y,Z'  and  representing the dimensions of a cuboid along with an integer 'N. Print a list of all possible coordinates given by '(i,j,k)' on a 3D grid where the sum of 'i+j+k' is not equal to 'N'. Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
#Sample Input 1
#2
#2
#2
#2
#Sample Output 1
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]