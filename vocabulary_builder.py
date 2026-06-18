# vocabulary_builder.py

vocab = {}

def add_word():
    word = input("Enter the word: ").strip().lower()
    meaning = input("Enter its meaning: ").strip()
    vocab[word] = meaning
    print(f"✅ '{word}' added successfully.\n")

def show_all():
    if not vocab:
        print("📭 No words yet. Add some!\n")
        return
    print("\n📚 Your Vocabulary:")
    for w, m in vocab.items():
        print(f"  {w} → {m}")
    print()

def search_word():
    word = input("Enter word to search: ").strip().lower()
    if word in vocab:
        print(f"🔍 {word} → {vocab[word]}\n")
    else:
        print(f"❌ '{word}' not found.\n")

def save_to_file():
    with open("vocabulary.txt", "w", encoding="utf-8") as f:
        for w, m in vocab.items():
            f.write(f"{w}: {m}\n")
    print("💾 Saved to vocabulary.txt\n")

def load_from_file():
    try:
        with open("vocabulary.txt", "r", encoding="utf-8") as f:
            for line in f:
                if ": " in line:
                    w, m = line.strip().split(": ", 1)
                    vocab[w] = m
        print("📂 Loaded vocabulary from file.\n")
    except FileNotFoundError:
        print("⚠️ No saved file found. Start fresh.\n")

def main():
    load_from_file()
    while True:
        print("\n=== 📖 Smart Vocabulary Builder ===")
        print("1. Add word")
        print("2. Show all words")
        print("3. Search word")
        print("4. Save and exit")
        choice = input("Choose (1-4): ").strip()
        if choice == "1":
            add_word()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search_word()
        elif choice == "4":
            save_to_file()
            print("👋 Goodbye! Keep learning.")
            break
        else:
            print("❌ Invalid choice.\n")

if __name__ == "__main__":
    main()