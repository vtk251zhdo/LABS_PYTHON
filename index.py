import re

def is_ukrainian_word(word):
	return re.fullmatch(r"[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+", word) is not None

def main():
	# ===== Task 1 =====
	text = input("Введіть текст українською (до 1000 слів): ").strip()
	if not text:
		print("Помилка: текст не може бути порожнім.")
		return

	words_raw = re.findall(r"[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+", text)
	if len(words_raw) > 1000:
		print("Помилка: текст містить більше 1000 слів.")
		return

	search_word = input("Введіть слово для пошуку: ").strip()
	if not search_word:
		print("Помилка: слово для пошуку не може бути порожнім.")
		return
	if not is_ukrainian_word(search_word):
		print("Помилка: некоректне українське слово для пошуку.")
		return

	words = re.findall(r"[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+", text)
	search_word_lower = search_word.lower()
	count = 0
	for w in words:
		if w.lower().startswith(search_word_lower):
			count += 1

	print(f"Кількість слів, що починаються з '{search_word}': {count}")

	# ===== Task 2 =====
	replaced_text = text.replace('a', 'A')
	num_replacements = text.count('a')
	num_characters = len(text)
	num_letters = len(re.findall(r'[а-щА-ЩЬьЮюЯяЇїІіЄєҐґa-zA-Z]', text))

	print(f"\nТекст після заміни 'a' на 'A':\n{replaced_text}")
	print(f"Кількість замін: {num_replacements}")
	print(f"Кількість символів у рядку: {num_characters}")
	print(f"Кількість літер у рядку: {num_letters}")

	# ===== Task 3 =====
	count_word = input("Введіть слово для підрахунку кількості входжень: ").strip()
	if not count_word:
		print("Помилка: слово для підрахунку не може бути порожнім.")
		return
	if not is_ukrainian_word(count_word):
		print("Помилка: некоректне українське слово для підрахунку.")
		return

	words_for_count = re.findall(r"[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+", text)
	count_occurrences = sum(1 for w in words_for_count if w.lower() == count_word.lower())
	print(f"Кількість входжень слова '{count_word}': {count_occurrences}")

	# ===== Task 4 =====
	tokens = re.findall(r"[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+|[^а-щА-ЩЬьЮюЯяЇїІіЄєҐґ'\s]", text)

	word_indices = [i for i, t in enumerate(tokens) if re.fullmatch(r"[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+", t)]
	num_words = len(word_indices)
	half = num_words // 2
	result_tokens = []
	word_count = 0
	for i, t in enumerate(tokens):
		if re.fullmatch(r"[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+", t):
			word_count += 1
			if word_count <= half:
				result_tokens.append(t.capitalize())
			else:
				result_tokens.append(t.lower() + ' *')
		else:

			result_tokens.append(t)

		if word_count == half and '|' not in result_tokens:
			result_tokens.append('|')

	transformed_line = ' '.join(result_tokens).replace(' | ', ' | ')
	print(f"\nТрансформований рядок для завдання 4:\n{transformed_line}")

	# ===== Task 5 =====
	eng_text = input("\nEnter English text (up to 1000 words): ").strip()
	if not eng_text:
		print("Error: Text cannot be empty.")
		return
	eng_words_raw = re.findall(r"[a-zA-Z']+", eng_text)
	if len(eng_words_raw) > 1000:
		print("Error: Text contains more than 1000 words.")
		return

	letter_n = input("Enter the letter for words starting with it (N): ").strip()
	letter_p = input("Enter the letter for words ending with it (P): ").strip()
	if not (len(letter_n) == 1 and letter_n.isalpha() and letter_n.lower() in 'abcdefghijklmnopqrstuvwxyz'):
		print("Error: The first letter must be a single English letter.")
		return
	if not (len(letter_p) == 1 and letter_p.isalpha() and letter_p.lower() in 'abcdefghijklmnopqrstuvwxyz'):
		print("Error: The second letter must be a single English letter.")
		return
	
	eng_words = re.findall(r"[a-zA-Z']+", eng_text)
	n_lower = letter_n.lower()
	p_lower = letter_p.lower()
	words_start_n = [w for w in eng_words if w.lower().startswith(n_lower)]
	words_end_p = [w for w in eng_words if w.lower().endswith(p_lower)]

	print(f"Words starting with '{letter_n}': {', '.join(words_start_n) if words_start_n else 'None'}")

	print(f"Words ending with '{letter_p}': {', '.join(words_end_p) if words_end_p else 'None'}")

	# ===== Task 6 =====
	eng_text_vowels = input("\nEnter English text (up to 100 words): ").strip()
	if not eng_text_vowels:
		print("Error: Text cannot be empty.")
		return
	eng_words_vowels = re.findall(r"[a-zA-Z']+", eng_text_vowels)
	if len(eng_words_vowels) > 100:
		print("Error: Text contains more than 100 words.")
		return
	vowels = 'aeiouy'
	num_vowels = sum(1 for c in eng_text_vowels.lower() if c in vowels)
	print(f"Number of vowels in the text: {num_vowels}")

	# ===== Task 7 =====
	eng_text_names = input("\nEnter English text (up to 1000 words): ").strip()
	if not eng_text_names:
		print("Error: Text cannot be empty.")
		return
	eng_words_names = re.findall(r"[a-zA-Z']+", eng_text_names)
	if len(eng_words_names) > 1000:
		print("Error: Text contains more than 1000 words.")
		return

	capitalized_words = [w for w in eng_words_names if re.fullmatch(r"[A-Z][a-z']*", w)]
	print(f"List of names and proper nouns: {capitalized_words if capitalized_words else 'None found'}")

if __name__ == "__main__":
	main()
