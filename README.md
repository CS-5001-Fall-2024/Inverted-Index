# Inverted Index

This project requires the following concepts:

- Dictionaries
- File I/O
- Complex Logic

## Project Setup

The repository for this assignment includes the following:

- `full_texts`: a directory containing four large text files that will be used for
  one of the auto-graded test cases. 
- `full_texts_expected`: the expected output of your program if the -input
  directory is `full_texts`.
- `short_texts`: a directory containing two small text files that will be used for
  one of the auto-graded test cases. 
- `short_texts_expected`: the expected output of your program if the -input
  directory is `short_texts`.


## Overview

[Information retrieval](https://en.wikipedia.org/wiki/Information_retrieval) is
the broad area of computer science that focuses on identifying relevant
information in a collection of documents. 

Search engines like Google are one application of information retrieval.

For this project, you will implement a program that builds three data
structures relevant to an information retrieval task: an index, an inverted
index, and a map of term frequency-inverse document frequency (tf-idf) scores for words in a collection of documents.

For the examples below, consider the following collection of two documents:

```
file1.txt
=========
one two
three four two five
two six

file2.txt
=========
two four! Six
two four sixty-eight.
```

### Index
An [index](https://en.wikipedia.org/wiki/Index_(publishing)), for example at the
back of a book, is a list of the words in a text and the locations where the
words appear. For a collection of documents, for instance a list of all text
documents in a given directory, an index consists of a mapping from the document
to the words in that document to a list of locations where those words appear.

Given the two documents above, the index would look as follows:
```
file1.txt
	five 6 
	four 4 
	one 1 
	six 8 
	three 3 
	two 2 5 7 
file2.txt
	four 2 5 
	six 3 
	sixtyeight 6 
	two 1 4 
```

### Inverted Index

An *[inverted index](https://en.wikipedia.org/wiki/Inverted_index)* is a list of
words and the texts where those words appear. The inverted index may also store
the list of locations where the words are found in the documents.  

 Given the two documents above, the inverted index would look as follows:
```
five
	file1.txt - 6 
four
	file1.txt - 4 
	file2.txt - 2 5 
one
	file1.txt - 1 
six
	file1.txt - 8 
	file2.txt - 3 
sixtyeight
	file2.txt - 6 
three
	file1.txt - 3 
two
	file1.txt - 2 5 7 
	file2.txt - 1 4 
```

### TF-IDF Score

The [term frequency–inverse document
frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) score is a measure of
how important a word is in a collection of documents. The idea of tf-idf is that
even though a word appears frequently in a document it may not be very important. A
word like "the" or "and", for example, may appear a large number of times, but
it appears a large number of times in all documents.

The tf-idf score for a word in a document is calculated by multiplying the
number of times the word appears in the document by the log of the total number
of documents in your collection divided by the number of documents in your
collection with the word.

Given a collection of three documents, suppose the following is true:

- The word *tomorrow* appears in document 1 four times.
- The word *tomorrow* appears in document 3 one time.

The tf-idf score for tomorrow in document 1 would be as follows:  `4 * math.log(3 / 2)`

The word appears 4 times in document 1, there are 3 documents in the
collection, and 2 of them have the word *tomorrow*.

Given the documents above, the scores generated would look as follows:

```
five
	file1.txt - 0.69
four
	file1.txt - 0.00
	file2.txt - 0.00
one
	file1.txt - 0.69
six
	file1.txt - 0.00
	file2.txt - 0.00
sixtyeight
	file2.txt - 0.69
three
	file1.txt - 0.69
two
	file1.txt - 0.00
	file2.txt - 0.00
```

## Requirements

1. There are no required design elements for this project, but your solution must
   be appropriately decomposed into functions.
2. Your solution will build an index, inverted index, and set of tf-idf scores
   from a set of text documents in a directory specified when the program is
   run.
3. After building the data structures, your solution will save each data
   structure to a separate file in a directory that is specified when the program is
   run. The index will be saved in a file `index.txt`, the inverted index will
   be saved in a file `inverted_index.txt`, and the set of tf-idf scores will be
   saved in a file `scores.txt`. The auto-graded test cases for this project
   will compare your output to the output expected for the given set of files.
4. The required format of the output is shown in the examples above and in the
   text files in the *expected directories in your repository.
5. To match the expected output you will need to process the documents in the
   following way:
     * Read in each file a line at a time
     * Split each line on whitespace
     * Lowercase each word
     * Remove any characters other than 0-9, a-z, and A-Z. It is recommended you
      use the python regular expression package
      [re](https://www.w3schools.com/python/python_regex.asp).
     * **Skip** any tokens that are only whitespace after you have performed the
       above cleaning of the word. *Do not increment your word count* for any
       tokens that are only whitespace.
6. When writing your index output you will sort first by file name and then by
   word in the file. When writing your inverted index output you will sort first
   by word and then by filename. Your tf-idf output will be sorted by word and
   then by filename.
7. The tf-idf scores will have two digits of precision. See
   [https://www.w3schools.com/python/python_string_formatting.asp](https://www.w3schools.com/python/python_string_formatting.asp)
   for some hints about precision in f-strings.
8. Your program will accept [command line
   arguments](https://www.geeksforgeeks.org/command-line-arguments-in-python/).
   The first argument will be a flag `-input` followed by the input directory,
   for example short_texts. The second argument will be a flag `-output`
   followed by an output directory, for example short_texts_actual. The program
   will be executed from the command line as follows: ` python inverted_index.py
   -input short_texts -output short_texts_actual` where short_texts and
   short_texts_actual could be replaced by other directory paths.

## Assignment Submission

To earn credit for this assignment you must commit all of your changes to your GitHub repository prior to the deadline. It is strongly recommended that you commit your changes regularly. Do not wait until you complete all four parts of the assignment to upload your (partial) solution.

Step 1 - *Stage Changes*: Select the Source Control icon in the VSCode left menu. In the Changes section, click the + to *Stage All Changes*.

Step 2 - Commit Message: In the text box that says Message enter a meaningful message that describes the change you just completed.

Step 3 - *Commit & Push*: Select the down arrow in the blue box that says Commit. Choose *Commit & Push*.

Step 4 - Verify: Visit the repository on GitHub to confirm that your changes were uploaded successfully.