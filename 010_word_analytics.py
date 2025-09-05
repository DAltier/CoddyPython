def analyze_text(text):
    # Your solution here
    
    # 1. Split the text into words and normalize them
    # (make lowercase and remove punctuation)
    punctuation = '.,!?:;"()'
    translator = str.maketrans('', '', punctuation)
    words = [w.translate(translator).lower() for w in text.split()]
    
    # 2. Count the occurrences of each word
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    
    # 3. Find the number of unique words
    unique_count = len(counts)
    
    # 4. Identify repeated words (appearing more than once)
    repeated_words = sorted([w for w, c in counts.items() if c > 1])
    
    # 5. Find palindrome words
    palindromes = sorted([w for w in counts if w == w[::-1]])
    
    # 6. Return the results in a dictionary with sorted lists
    return {
        'unique_count': unique_count,
        'repeated_words': repeated_words,
        'palindromes': palindromes
    }