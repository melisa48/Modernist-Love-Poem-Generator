# Modernist Love Poem Generator

A Python-based poetry generator that creates poems in the styles of Rainer Maria Rilke and E.E. Cummings. This project uses Markov chains and custom algorithms to generate unique poems that capture the essence of these two distinctive modernist poets.

## Features

- Generates poems in two distinct styles:
  - Rilke-style: Philosophical, questioning, with metaphysical themes
  - Cummings-style: Experimental formatting, lowercase style, unique punctuation
- Uses Markov chains for natural language generation
- Includes carefully curated vocabulary lists for abstract concepts
- Maintains consistent style characteristics for each poet
- Allows for mixed-style generation

## Installation

1. Ensure you have Python 3.6 or later installed
2. Clone this repository:
```bash
git clone https://github.com/yourusername/modernist-poem-generator.git
cd modernist-poem-generator
```

3. No additional dependencies required - the generator uses only Python standard library modules

## Usage

### Basic Usage

```python
from poem_generator import ModernistPoemGenerator

# Create a new generator instance
generator = ModernistPoemGenerator()

# Train the generator with the provided poems
generator.train(rilke_inspired_poems)
generator.train(cummings_inspired_poems)

# Generate a Rilke-style poem
generator.style = "rilke"
print(generator.generate_poem())

# Generate a Cummings-style poem
generator.style = "cummings"
print(generator.generate_poem())

# Generate both styles
generator.style = "mixed"
print(generator.generate_poem())
```

### Customizing the Generator

You can add your own training data:

```python
custom_poems = [
    """Your custom poem
    with multiple lines
    in the style you prefer""",
    
    """Another custom poem
    to enhance the training data"""
]

generator.train(custom_poems)
```

## Example Output

### Rilke-style Poem
```
Where does love end and the universe begin?

Fleeting moment in time and space,
Soul whispers through eternal light,
In petals soft, a fragile art,
The language spoken by the heart,
Through shadows dance our silent dreams,
While music plays in infinite streams.

How can I keep my heart from echoing yours?
And what musician holds us in their hand?
```

### Cummings-style Poem
```
since feeling is wild
who dreams beyond silence
to dance through light

will never wholly touch truth
gentle to be free
while spring is in the world

my heart believes
and love is better fate
than wisdom

dear i swear by all stars
—the best whispers of soul dance
your eyes which says
we are for each other

for life's not a paragraph
and death i think is no parenthesis
```

## Customization Options

The generator includes several customizable features:

1. Abstract vocabulary lists:
   - Nouns (`abstract_nouns`)
   - Verbs (`abstract_verbs`)
   - Adjectives (`abstract_adjectives`)

2. Philosophical questions for Rilke-style poems
3. Line length and stanza structure
4. Punctuation patterns

## Technical Details

The generator uses:
- Defaultdict for efficient Markov chain storage
- Regular expressions for text cleaning
- Random selection for variety in generation
- Bi-gram model for more coherent text generation

## Contributing

Feel free to contribute to this project by:
1. Adding more training data
2. Improving the generation algorithms
3. Adding new poetic styles
4. Enhancing the vocabulary lists

## Acknowledgments

- Inspired by the works of Rainer Maria Rilke and E.E. Cummings
- Built using Python standard library
- Developed with a love for poetry and programming

## Contributing
- Contributions to improve the Modernist Love Poem Generator are welcome. Please fork the repository and submit a pull request with your changes.
