def calculate_score(text, skills):

```
score = 0

text = text.lower()

# Skills

if len(skills) >= 5:
    score += 20

if len(skills) >= 10:
    score += 20

if len(skills) >= 15:
    score += 10

# Resume Sections

if "education" in text:
    score += 10

if "experience" in text:
    score += 15

if "project" in text:
    score += 15

if "certification" in text:
    score += 10

if "internship" in text:
    score += 10

# Resume Length

word_count = len(text.split())

if word_count >= 300:
    score += 10

return min(score, 100)
```
