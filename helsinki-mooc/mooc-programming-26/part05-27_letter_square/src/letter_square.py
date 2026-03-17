# Write your solution here
import string

#grid size
layers = int(input("Layers: "))
alphabet = string.ascii_uppercase
size = (2 * layers) - 1

for row in range(size):
    row_str = ""
    for column in range(size):
    
    dist_top = row
    dist_left = column
    dist_bottom = (size - 1)- row
    dist_right = (size -1) - column

    min_dist = min(dist_top,dist_bottom, dist_left, dist_right)
    
    letter_index = layers - 1 - m
    
    row_str += alphabet[letter_index]
    
    print(row_str)