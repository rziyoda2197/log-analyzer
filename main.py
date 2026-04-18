import logging
import re
from collections import Counter

# Log faylini ochish
logging.basicConfig(filename='log.txt', level=logging.ERROR)

# Log fayldan errorlarni o'qish
with open('log.txt', 'r') as f:
    errors = [line.strip() for line in f.readlines()]

# Errorlarni analiz qilish
error_codes = [re.search(r'\d{3}', error).group() for error in errors if re.search(r'\d{3}', error)]
error_messages = [re.search(r'(.*)\d{3}', error).group(1) for error in errors if re.search(r'\d{3}', error)]

# Error kodlarini sanash
error_code_counts = Counter(error_codes)

# Error kodlarini ko'rsatish
for code, count in error_code_counts.most_common():
    print(f"Error code {code}: {count} times")

# Error xabarlarini sanash
error_message_counts = Counter(error_messages)

# Error xabarlarini ko'rsatish
for message, count in error_message_counts.most_common():
    print(f"Error message '{message}': {count} times")
