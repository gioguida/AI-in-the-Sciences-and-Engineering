#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace star emojis with LaTeX bigstar symbols"""

files = [
    'chapters/chapter03.tex',
    'chapters/chapter04.tex',
    'chapters/chapter05.tex',
    'chapters/chapter06.tex',
    'chapters/chapter05_to_end.tex'
]

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace star emoji with LaTeX bigstar
        new_content = content.replace('⭐', r'$\bigstar$')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ Processed {filepath}")
    except Exception as e:
        print(f"✗ Error with {filepath}: {e}")

print("\nDone!")
