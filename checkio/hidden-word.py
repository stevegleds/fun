__author__ = 'Steve'
Nicola has solved this puzzle (and I am sure that you will do equally well). To be prepared for more such puzzles, Nicola wants to invent a method to search for words inside poetry. You can help him create a function to search for certain words.
You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n). Casing does not matter for your search, but whitespaces should be removed before your search. You should find the word inside the rhyme in the horizontal (from left to right) or vertical (from up to down) lines. For this you need envision the rhyme as a matrix (2D array). Find the coordinates of the word in the cut rhyme (without whitespaces).
The result must be represented as a list -- [row_start,column_start,row_end,column_end], where
row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the line number for the last letter of the word.
Counting of the rows and columns start from 1.
rhymes
Input: Two arguments. A rhyme (a string) and a word (a string).
Output: The coordinates of the word.
def checkio(text, word):
    return [1, 1, 1, 4]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]