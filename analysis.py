import re
from collections import Counter

def count_words(text):
    """Count total words in text"""
    words = text.split()
    return len(words)

def count_characters(text):
    """Count total characters in text"""
    return len(text)

def count_sentences(text):
    """Count sentences using punctuation marks"""
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def count_syllables(text):
    """Count syllables using vowel groups (basic estimation)"""
    words = text.split()
    syllable_count = 0
    for word in words:
        word = word.lower()
        vowel_pattern = re.compile(r'[aeiou]+')
        syllable_count += len(vowel_pattern.findall(word))
    return syllable_count

def count_unique_words(text):
    """Count unique words in text"""
    words = text.split()
    return len(set(words))

def find_repeated_words(text):
    """Find words that appear more than once"""
    words = text.lower().split()
    word_count = Counter(words)
    return {word: count for word, count in word_count.items() if count > 1}

def average_word_length(text):
    """Calculate average word length"""
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)

def find_longest_words(text, count=5):
    """Find the longest words in text"""
    words = text.split()
    if not words:
        return []
    sorted_words = sorted(set(words), key=len, reverse=True)
    return sorted_words[:count]

def count_special_characters(text):
    """Count special characters (non-alphanumeric)"""
    special_chars = re.findall(r'[^a-zA-Z0-9\s]', text)
    return len(special_chars)

def extract_nouns(text):
    """Basic noun extraction (words starting with capital letter)"""
    words = text.split()
    nouns = [word for word in words if word[0].isupper() and word not in ['I', 'You', 'He', 'She', 'We', 'They']]
    return nouns if nouns else ["No nouns detected"]

def extract_verbs(text):
    """Basic verb extraction (words ending in -ing, -ed, -es)"""
    words = text.split()
    verbs = [word for word in words if word.lower().endswith(('ing', 'ed', 'es', 'en'))]
    return verbs if verbs else ["No verbs detected"]

def extract_adjectives(text):
    """Basic adjective extraction (words ending in -ous, -ful, -able)"""
    words = text.split()
    adjectives = [word for word in words if word.lower().endswith(('ous', 'ful', 'able', 'ible', 'al', 'y'))]
    return adjectives if adjectives else ["No adjectives detected"]

def extract_adverbs(text):
    """Basic adverb extraction (words ending in -ly)"""
    words = text.split()
    adverbs = [word for word in words if word.lower().endswith('ly')]
    return adverbs if adverbs else ["No adverbs detected"]

def readability_score(text):
    """Calculate Flesch Reading Ease score (basic)"""
    words = text.split()
    sentences = count_sentences(text)
    syllables = count_syllables(text)
    
    if not words or sentences == 0:
        return 0
    
    # Flesch Reading Ease formula
    score = 206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syllables / len(words))
    return round(score, 2)

def full_analysis(text):
    """Comprehensive analysis of the text"""
    analysis = {
        "Word Count": count_words(text),
        "Character Count": count_characters(text),
        "Sentence Count": count_sentences(text),
        "Syllable Count": count_syllables(text),
        "Unique Words": count_unique_words(text),
        "Average Word Length": average_word_length(text),
        "Special Characters": count_special_characters(text),
        "Repeated Words": find_repeated_words(text),
        "Longest Words": find_longest_words(text, 5),
        "Nouns": extract_nouns(text),
        "Verbs": extract_verbs(text),
        "Adjectives": extract_adjectives(text),
        "Adverbs": extract_adverbs(text),
        "Readability Score": readability_score(text),
    }
    return analysis
