import os
import re

files = ['scenarios_ru.py', 'scenarios_en.py', 'scenarios_el.py']
for filepath in files:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to insert '"image_type": "mario",' right after '"mario_\w+": {\n'
    def replacer(m):
        block = m.group(0)
        # Check if next line already has image_type
        return m.group(1) + m.group(2) + '"image_type": "mario",\n' + m.group(2)
        
    # Replace only if it doesn't already have image_type
    # A bit complex with regex, let's just do a simple string replace
    lines = content.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        if re.search(r'"mario_[\w]+": \{', line):
            # next line might be image_type already
            if i + 1 < len(lines) and '"image_type": "mario"' not in lines[i+1]:
                # get indentation of next line
                indent = len(lines[i+1]) - len(lines[i+1].lstrip())
                new_lines.append(' ' * indent + '"image_type": "mario",')
        i += 1
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
