class SimpleWordFormsProvider:
    def get_word_forms(self, word):
        result = []
        lower_word = word.lower()

        # We assume that the input word is in the plural, then we add the singular
        if len(word) > 3 and lower_word.endswith("ies"):
            result.append(word[:-3] + "y")
        if len(word) > 2 and lower_word.endswith("es"):
            result.append(word[:-2])
        if len(word) > 1 and lower_word.endswith("s"):
            result.append(word[:-1])

        # Then we assume that the input word is in the singular, we add the plural
        if len(word) > 1 and lower_word.endswith("y"):
            result.append(word[:-1] + "ies")
        elif lower_word.endswith(("s", "x", "ch", "sh")):
            result.append(word + "es")
        else:
            result.append(word + "s")
        # All rules are implemented in the EnglishWordFormsProvider class

        return result