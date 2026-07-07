class TextAnalyzer:
    def __init__(self, text):
        self.text = text
    
    def count_characters(self):
        text_length = len(self.text)
        return text_length
    
    def count_words(self):
        words = self.text.split()
        word_count = len(words)
        return word_count
    
    def count_sentences(self):
        sentences = self.text.split('.|!|?')
        sentence_count = len(sentences)
        return sentence_count
    
    def avg_word_length(self):
        words = self.text.split()
        
        if len(words) == 0:
            return 0
        
   
        total_length = 0
        for word in words:
            # Ausgabe hinzugefügt zum Testen der Wortlänge
            print(f"Word: {word}, Length: {len(word)}")
            total_length = total_length + len(word)
        
        average = total_length / len(words)
        return average
   
    def most_common_word(self):
        words = self.text.lower()
        remove_punctuation = words.replace('.', '').replace('-', '').replace('!', '').replace('?', '')
        print(remove_punctuation)
        word_frequency = {}

        # Die Wörter müssen einzeln gezählt werden und in die Dictionary gespeichert werden
        for word in remove_punctuation.split():
            if word in word_frequency:
                word_frequency[word] = word_frequency[word] + 1
            else:
                word_frequency[word] = 1
        
        result = "--- Top 10 Words ---\n"
        counter = 1

        print(word_frequency.items())
        
        # Wiederhole bis zu 10 mal
        for i in range(10):
            # Finde das häufigste Wort
            max_word = None
            max_count = 0
            
            for word, count in word_frequency.items():
                if count > max_count:
                    max_word = word
                    max_count = count
            
            if max_word is None:
                break
            
            result += f"{counter}. {max_word:15s} {max_count}x\n"
            word_frequency[max_word] = 0
            counter = counter + 1
        
        return result

if __name__ == "__main__":
    file_path = "C:\\Users\\richa\\Desktop\\Weiterbildung_DeveloperAkademie\\Python\\developerAkademie.txt"
    results_file = "C:\\Users\\richa\\Desktop\\Weiterbildung_DeveloperAkademie\\Python\\results.txt"

    try:
        print(f"Versuche zu öffnen: {file_path}")
        
        with open(file_path, 'r') as file:
            text_content = file.read()
            
        # Ergebnisse alle in einer Variable sammeln
        output = ""
        output += "Datei erfolgreich gelesen!\n\n"
        output += f"Text: {text_content}\n"
        
        text_file = TextAnalyzer(text_content)
        
        output += f"Character count: {text_file.count_characters()}\n"
        output += f"Word count: {text_file.count_words()}\n"
        output += f"Sentence count: {text_file.count_sentences()}\n"
        output += f"Average word length: {text_file.avg_word_length():.2f}\n\n"
        output += text_file.most_common_word()
        
        # output der Konsole ausgeben
        print(output)
        
        # Speichere in Datei
        with open(results_file, 'w') as file:
            file.write(output)
        
        print(f"\nErgebnisse gespeichert in: {results_file}")

    except Exception as e:
        print(f"❌ Fehler beim Lesen: {e}")
