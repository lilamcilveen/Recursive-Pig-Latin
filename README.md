### Recursive-Pig-Latin
This project explores the functional programming paradigm. The idea behind it is to describe "what" each component is to solve the problem, rather than "how" a result may be computed.

The idea behind the functional programming:
 - We start by asking: "What data do I have?" and "How do I want to transform that data to solve the problem at hand?".
 - Functions are the most important part of the program. Instead of telling that data to do something, pass it to a function to do something. 
 - The function doesn't modify the original data, although it may return a modified copy of it. Recursion is awesome!
 - We avoid changing-state and mutable data.
 
How to run:
 - On Windows, input:
         python piggypoo.py
 - On Linux, input:
         python3 piggypoo.py
         
 - Once it is running you can enter in a "Snake Case". 
 - For example, "iqra_is_really_old"
 
 - Each word should be seperated by underscores
 - Each word should be lowercase
    
 

Example:

    Enter a snake case: hey_i_like_pigs_a_lot!
    
    ('eyhay', 'iay', 'ikelay', 'igspay', 'aay', 'ot!lay')
    
What is Pig Latin?
 - A language game where English words are altered.
 - All initial consonants are moved to the end of the word.
 - All words start with their first vowel.
 - All words end with an "ay"!
 - For example: bbbbbbahellothere -> turns into -> ahellotherebbbbbbay
    

Created on January 6, 2019.
