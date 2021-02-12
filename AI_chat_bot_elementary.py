"""
This is a AI elementary level chat bot prg
"""
words = input("Please say something : ").lower()

if "hello" in words:
    print("Hello to you too !!")
elif "how are you" in words:
    print("I an great , Thank you!")
elif "goodbye" in words:
    print("Goodbye to you too !!")
else:
    print("huh ??")