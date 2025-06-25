def mood_tracker():
    mood = input("How are you feeling today? (happy/sad/stressed/lazy/bored): ").lower()
    if mood == "happy":
        print("That's awesome! Keep spreading the joy! 😊")
    elif mood == "sad":
        print("It's okay to feel sad. Tomorrow will be better. 🌈")
    elif mood == "stressed":
        print("Take a deep breath. You’re stronger than your stress. 💪")
    elif mood == "lazy":
        print("Even lazy days can be productive. Take small steps! 🐢")
    elif mood == "bored":
        print("Try learning something new or calling a friend! 📞")
    else:
        print("Thanks for sharing your mood.")

    quote = input("Want a motivational quote? (yes/no): ").lower()
    if quote == "yes":
        print("“The only way to do great work is to love what you do.” – Steve Jobs")

mood_tracker()
