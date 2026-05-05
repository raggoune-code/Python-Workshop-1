import sys
import time

def slow_print(text, delay=0.03):
    """
    Python makes doing cool things easy! 
    This function prints text one character at a time.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Python code is designed to be highly readable.
    slow_print("🚀 Booting up Python Workshop Environment...", dela_y=0.04)
    time.sleep(0.5)
    
    # We can use f-strings to easily insert variables into text
    python_version = sys.version.split(' ')[0]
    slow_print(f"✅ Python Version {python_version} detected!")
    time.sleep(0.5)

    print("\n" + "=" * 50)
    slow_print("   Welcome to Workshop 1: Intro to Python & Git!")
    print("=" * 50 + "\n")
    
    # Looping over lists is incredibly straightforward
    topics = ["Setting up Git", "Writing Clean Python", "Collaborating via GitHub"]
    
    slow_print("In our sessions, we will conquer:")
    for index, topic in enumerate(topics, start=1):
        slow_print(f"  {index}. {topic}", delay=0.05)
        time.sleep(0.2)
        
    print("\n✨ You are ready! Proceed to Step 5 in README.md to continue. ✨\n")

if __name__ == "__main__":
    main()
