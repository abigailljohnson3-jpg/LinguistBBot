from analysis import *
import telebot
import os
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

def get_text_from_message(message):
    if message.reply_to_message and message.reply_to_message.text:
        return message.reply_to_message.text
    elif message.text and len(message.text.split()) > 1:
        return message.text.split(' ', 1)[1]
    elif message.text and not message.text.startswith('/'):
        return message.text
    else:
        return None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
📝 **Text Analyzer Bot** 📝

Send me any text and I'll analyze it!

**Available Commands:**
/start - Show this message
/help - Show this message
/full_analysis - Complete text analysis
/word_count - Count words
/character_count - Count characters
/sentence_count - Count sentences
/syllable_count - Count syllables
/unique_word_count - Count unique words
/repeated_words - Find repeated words
/longest_words - Show longest words
/nouns - Extract nouns
/verbs - Extract verbs
/adjectives - Extract adjectives
/adverbs - Extract adverbs
/readability - Flesch Reading Ease score

**How to use:**
Just send me text or use /command followed by text
Example: /word_count This is a sample text

Made with ❤️
"""
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['word_count'])
def word_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"📊 **Word Count:** {count_words(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/word_count Hello world`", parse_mode='Markdown')

@bot.message_handler(commands=['character_count'])
def character_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"📊 **Character Count:** {count_characters(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['sentence_count'])
def sentence_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"📊 **Sentence Count:** {count_sentences(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['syllable_count'])
def syllable_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"📊 **Syllable Count:** {count_syllables(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['unique_word_count'])
def unique_word_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"📊 **Unique Words:** {count_unique_words(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['repeated_words'])
def repeated_words_command(message):
    text = get_text_from_message(message)
    if text:
        repeated = find_repeated_words(text)
        if repeated:
            response = "**Repeated Words:**\n" + "\n".join([f"- {word}: {count} times" for word, count in repeated.items()])
            bot.reply_to(message, response, parse_mode='Markdown')
        else:
            bot.reply_to(message, "✅ No repeated words found.", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['longest_words'])
def longest_words_command(message):
    text = get_text_from_message(message)
    if text:
        longest = find_longest_words(text, 5)
        if longest:
            response = "**Longest Words:**\n" + "\n".join([f"- {word} ({len(word)} letters)" for word in longest])
            bot.reply_to(message, response, parse_mode='Markdown')
        else:
            bot.reply_to(message, "No words found.", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['nouns'])
def nouns_command(message):
    text = get_text_from_message(message)
    if text:
        nouns = extract_nouns(text)
        response = f"**Nouns:** {', '.join(nouns)}"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['verbs'])
def verbs_command(message):
    text = get_text_from_message(message)
    if text:
        verbs = extract_verbs(text)
        response = f"**Verbs:** {', '.join(verbs)}"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['adjectives'])
def adjectives_command(message):
    text = get_text_from_message(message)
    if text:
        adjectives = extract_adjectives(text)
        response = f"**Adjectives:** {', '.join(adjectives)}"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['adverbs'])
def adverbs_command(message):
    text = get_text_from_message(message)
    if text:
        adverbs = extract_adverbs(text)
        response = f"**Adverbs:** {', '.join(adverbs)}"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['readability'])
def readability_command(message):
    text = get_text_from_message(message)
    if text:
        score = readability_score(text)
        if score >= 90:
            level = "Very Easy (5th grade level)"
        elif score >= 80:
            level = "Easy (6th grade level)"
        elif score >= 70:
            level = "Fairly Easy (7th grade level)"
        elif score >= 60:
            level = "Standard (8th-9th grade level)"
        elif score >= 50:
            level = "Fairly Difficult (10th-12th grade level)"
        elif score >= 30:
            level = "Difficult (College level)"
        else:
            level = "Very Difficult (College graduate level)"
        
        response = f"📊 **Readability Score:** {score}/100\n**Level:** {level}"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(commands=['full_analysis'])
def full_analysis_command(message):
    text = get_text_from_message(message)
    if text:
        analysis = full_analysis(text)
        response = f"📝 **Full Text Analysis**\n\n"
        response += f"**Word Count:** {analysis['Word Count']}\n"
        response += f"**Character Count:** {analysis['Character Count']}\n"
        response += f"**Sentence Count:** {analysis['Sentence Count']}\n"
        response += f"**Syllable Count:** {analysis['Syllable Count']}\n"
        response += f"**Unique Words:** {analysis['Unique Words']}\n"
        response += f"**Average Word Length:** {analysis['Average Word Length']}\n"
        response += f"**Special Characters:** {analysis['Special Characters']}\n"
        response += f"**Readability Score:** {analysis['Readability Score']}/100\n\n"
        
        if analysis['Repeated Words']:
            response += "**Repeated Words:**\n"
            for word, count in analysis['Repeated Words'].items():
                response += f"- {word}: {count} times\n"
            response += "\n"
        
        if analysis['Longest Words']:
            response += "**Longest Words:**\n"
            for word in analysis['Longest Words']:
                response += f"- {word}\n"
            response += "\n"
        
        response += f"**Nouns:** {', '.join(analysis['Nouns'][:5])}{'...' if len(analysis['Nouns']) > 5 else ''}\n"
        response += f"**Verbs:** {', '.join(analysis['Verbs'][:5])}{'...' if len(analysis['Verbs']) > 5 else ''}\n"
        response += f"**Adjectives:** {', '.join(analysis['Adjectives'][:5])}{'...' if len(analysis['Adjectives']) > 5 else ''}\n"
        response += f"**Adverbs:** {', '.join(analysis['Adverbs'][:5])}{'...' if len(analysis['Adverbs']) > 5 else ''}\n"
        
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.", parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def auto_analyze(message):
    text = get_text_from_message(message)
    if text and not message.text.startswith('/'):
        words = count_words(text)
        chars = count_characters(text)
        sentences = count_sentences(text)
        
        response = f"📊 **Quick Analysis:**\n"
        response += f"Words: {words}\n"
        response += f"Characters: {chars}\n"
        response += f"Sentences: {sentences}\n\n"
        response += f"Send `/full_analysis` for detailed analysis!"
        
        bot.reply_to(message, response, parse_mode='Markdown')
