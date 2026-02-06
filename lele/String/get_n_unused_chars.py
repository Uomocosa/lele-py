from loguru import logger

def get_n_unused_chars(text, n=1):
	assert n >= 1
	chars = [None]*n
	i = 0
	for j in range(129, 205743):  # Iterate through ASCII escluding the most common one
		char_to_check = chr(i)
		if char_to_check not in text:
			chars[i] = char_to_check
			i += 1
			if i >= n: return chars
	return None  # Return None if no unused char is found in the range


def test_():
    logger.debug(chr(205743)) #last char found
    assert get_n_unused_chars("HELLO WORLD!", n=1) == ['\x00']
