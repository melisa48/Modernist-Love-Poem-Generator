import random
from collections import defaultdict
import re

class ModernistPoemGenerator:
    def __init__(self, style="mixed"):
        self.markov_chain = defaultdict(list)
        self.starting_phrases = []
        self.style = style
        self.punctuation = ".?!,;—:"
        self.abstract_nouns = ["love", "time", "death", "silence", "dreams", "shadows", "light", "truth", "beauty", "heart", "soul", "mind", "spring", "world", "kiss", "flower", "wisdom", "life", "blood", "fate", "universe", "eternity", "music", "spirit"]
        self.abstract_verbs = ["feel", "know", "see", "hear", "think", "dream", "become", "exist", "dance", "sing", "love", "kiss", "touch", "embrace", "whisper", "remember", "echo", "resonate"]
        self.abstract_adjectives = ["deep", "bright", "silent", "sweet", "gentle", "soft", "wild", "free", "whole", "pure", "true", "wise", "infinite", "eternal", "fleeting", "fragile"]
        
    def clean_text(self, text):
        text = re.sub(r'[^a-zA-Z\s' + self.punctuation + ']', '', text)
        return text

    def train(self, poems):
        for poem in poems:
            lines = poem.split('\n')
            for line in lines:
                cleaned_line = self.clean_text(line)
                words = cleaned_line.split()
                
                if len(words) > 0:
                    self.starting_phrases.append(words[0])
                
                for i in range(len(words) - 2):
                    current_words = (words[i], words[i+1])
                    next_word = words[i + 2]
                    self.markov_chain[current_words].append(next_word)

    def generate_philosophical_question(self):
        questions = [
            "How can we hold the infinite in finite hands?",
            "What melody plays between our silent thoughts?",
            "Where do our souls meet when distance parts us?",
            "How can I keep my heart from echoing yours?",
            "What space exists between two moments of love?",
            "How do we measure the depth of feeling?",
            "Where does love end and the universe begin?",
            "What songs do our combined shadows sing?",
            "How can I keep my soul in me, so that it doesn't touch your soul?",
            "Upon what instrument are we two spanned?"
        ]
        return random.choice(questions)

    def generate_line(self, min_words=3, max_words=6, style="mixed"):
        if not self.starting_phrases:
            return "Error: No training data available"
            
        line_parts = []
        # Start with an abstract word
        line_parts.append(random.choice(self.abstract_nouns + self.abstract_verbs))
        
        line_length = random.randint(min_words, max_words)
        for _ in range(line_length - 1):
            word_choices = self.abstract_nouns + self.abstract_verbs + self.abstract_adjectives
            line_parts.append(random.choice(word_choices))
            
        line = ' '.join(line_parts)
        return line.lower() if style == "cummings" else line

    def generate_rilke_style(self):
        lines = []
        
        # Opening philosophical question
        lines.append(self.generate_philosophical_question())
        lines.append("")
        
        # Body of the poem
        for _ in range(6):
            line = self.generate_line(5, 12, "rilke")
            if random.random() < 0.3:
                line += ","
            lines.append(line)
        
        # Closing questions
        lines.append("")
        lines.append(self.generate_philosophical_question())
        lines.append("And what musician holds us in their hand?")
        
        return '\n'.join(lines)

    def generate_cummings_style(self):
        lines = []
        
        # First stanza (3 lines)
        lines.append("since " + self.generate_line(2, 3, "cummings"))
        lines.append("who " + self.generate_line(3, 4, "cummings"))
        lines.append("to " + self.generate_line(3, 4, "cummings"))
        
        # Second stanza (4 lines)
        lines.append("")
        lines.append("will never " + self.generate_line(2, 3, "cummings"))
        lines.append(random.choice(self.abstract_adjectives).lower() + " to be " + random.choice(self.abstract_nouns).lower())
        lines.append("while " + random.choice(["spring", "love", "time"]) + " is in the world")
        
        # Third stanza (3 lines)
        lines.append("")
        lines.append("my " + random.choice(["heart", "soul", "blood"]) + " " + random.choice(["approves", "believes", "knows"]))
        lines.append("and " + random.choice(self.abstract_nouns) + " is better fate")
        lines.append("than " + random.choice(["wisdom", "silence", "waiting"]))
        
        # Fourth stanza (4 lines)
        lines.append("")
        lines.append(random.choice(["love", "dear", "sweet"]) + " i swear by all " + random.choice(["flowers", "stars", "dreams"]))
        lines.append("—the best " + self.generate_line(3, 4, "cummings"))
        lines.append("your " + random.choice(["eyes", "smile", "touch"]) + " which says")
        lines.append("we are for each other")
        
        # Final lines
        lines.append("")
        lines.append("for life's not a paragraph")
        lines.append("and death i think is no parenthesis")
        
        return '\n'.join(lines)

    def generate_poem(self):
        if self.style == "rilke":
            return self.generate_rilke_style()
        elif self.style == "cummings":
            return self.generate_cummings_style()
        else:
            poems = [self.generate_rilke_style(), "-------------------", self.generate_cummings_style()]
            return '\n'.join(poems)

# Training data
rilke_inspired_poems = [
    """How shall we measure the depths of our souls?
    When every touch creates infinite whole
    Like music played on invisible strings
    That resonates through all living things
    What instrument holds our combined breath?
    What melody survives past death?
    In silence we find our shared voice
    In darkness we make our final choice""",
    
    """The rose unfolds its silent plea,
    A whispered secret for you and me.
    In petals soft, a fragile art,
    The language spoken by the heart.
    How can we capture such a grace?
    A fleeting moment in time and space.
    Yet in its beauty, we can find,
    A mirror to reflect our mind."""
]

cummings_inspired_poems = [
    """since feeling is first
    who pays any attention
    to the syntax of things
    will never wholly kiss you;
    wholly to be a fool
    while Spring is in the world
    my blood approves,
    and kisses are better fate
    than wisdom
    lady i swear by all flowers. Don't cry
    —the best gesture of my brain is less than
    your eyelids' flutter which says
    we are for each other: then
    laugh, leaning back in my arms
    for life's not a paragraph
    And death i think is no parenthesis""",
    
    """love is more true than reason
    who thinks of syntax rules
    when hearts beat wild and free
    spring dances through our veins
    while wisdom sleeps quietly
    my soul knows only this
    that kisses speak more truth
    than all philosophy
    dear one i swear by stars above
    —the deepest thought means less
    than your sweet glance which tells
    we belong to each other
    for rules are not poetry
    and time is no barrier"""
]

# Create and train the generator
generator = ModernistPoemGenerator()
generator.train(rilke_inspired_poems)
generator.train(cummings_inspired_poems)

# Generate both styles
print("Rilke-style Poem:\n")
generator.style = "rilke"
print(generator.generate_poem())
print("\n-------------------\n")
print("Cummings-style Poem:\n")
generator.style = "cummings"
print(generator.generate_poem())