#! prints all the words in descending order but bottom pyramid has all 6 words, in the right direction though
# def decode(message_file):
#     # Read the lines from the file
#     with open(message_file, 'r') as file:
#         lines = file.readlines()

#     # Create a list of tuples containing the words and their corresponding numbers
#     words_numbers = [(int(line.split()[0]), line.split()[1]) for line in lines]

#     # Find the maximum level of the pyramid
#     max_level = max([pair[0] for pair in words_numbers])

#     # Create a dictionary to store words at each level
#     pyramid = {level: [] for level in range(1, max_level + 1)}

#     # Populate the dictionary with words at their respective levels
#     for pair in words_numbers:
#         pyramid[pair[0]].append(pair[1])

#     # Print the pyramid
#     for level in range(1, max_level + 1):
#         print(" " * (max_level - level) * 4, end="")
#         for word_level in range(1, max_level + 1):
#             if word_level <= level:
#                 for word in pyramid[word_level]:
#                     print(f"{word_level} {word}", end="    ")
#             else:
#                 print(" " * (len(pyramid[max_level][-1]) + 4), end="")
#         print()

# # Example usage
# decode("message.txt")


# def full_pyramid_from_file(message_file):
#     with open(message_file, 'r') as file:
#         sorted_file = sorted(file)
#         lines = sorted_file.readlines()
#         n = len(lines)
        
#         for i, line in enumerate(lines, start=1):
#             # Print leading spaces
#             for _ in range(n - i):
#                 print(" ", end="")
            
#             # Print the content from the file
#             print(line.rstrip())

# Example usage
# full_pyramid_from_file("message.txt")

# Function to print full pyramid pattern
# def full_pyramid(message_file):
#     text_file = open(message_file, 'r')
#     for i in range(1, text_file + 1):
#         # Print leading spaces
#         for j in range(text_file - i):
#             print(" ", end="")
         
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print(text_file, end="")

def full_pyramid(words):
    n = len(words)
    max_length = max(len(word) for word in words)
    
    for i, word in enumerate(words, start=1):
        # Print leading spaces
        spaces = " " * (max_length - len(word))
        print(" " * (n - i) * (max_length + 1), end="")
        
        # Print the word
        print(f"{spaces}{word}{spaces}", end="")
        
        # Move to the next line after printing each row
        print()

def decode_file(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
        words = [line.split()[1] for line in lines]
        full_pyramid(words)

# Example usage
decode_file("message.txt")








