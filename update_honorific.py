honorifics = [
    "The Immortal Lord of Heaven and Earth for Blessings",
    "The Sky Lord of Heaven and Earth for Blessings",
    "The Exalted Thearch of Heaven and Earth for Blessings",
    "The Celestial Worthy of Heaven and Earth for Blessings"
]

# Read README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Find which honorific is currently in the README
current_honorific = None
for h in honorifics:
    if h in content:
        current_honorific = h
        break

# Decide next honorific
if current_honorific:
    index = honorifics.index(current_honorific)
    next_honorific = honorifics[(index + 1) % len(honorifics)]
else:
    next_honorific = honorifics[0]

# Replace old honorific (or placeholder) with the new one
if current_honorific:
    content = content.replace(current_honorific, next_honorific)
else:
    content = content.replace("<HONORIFIC>", next_honorific)

# Write back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
