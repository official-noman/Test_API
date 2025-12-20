# test_gemini.py
from gemini_client import ask_gemini

if __name__ == "__main__":
    prompt = "write 2 lines love poem"
    answer = ask_gemini(prompt)
    print(answer)
