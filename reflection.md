# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  The first time I ran the game, I saw a black screen with text that told me to guess a number within 7 attempts. Two concrete bugs I noticed at the start were that the hints were backwards--when my number was too low, it told me to go lower, and when my number was too high, it told me to go higher. Another bug that I noticed was that when you try to click on New Game, it does not reset the history, so you are unable to guess if you maxed out in guesses and lost the previous game. A third bug would be that the score only decreases by 5 if you go over the secret number, but not under--I would assume it would decrement by 5 for however many times you guess incorrectly.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used both ChatGPT and GitHub Copilot on this project. One example of an AI suggestion that was correct was the error I was facing with clearing the history. It suggested to change the session state back to playing as well as adding a line to clear the history. I was able to verify results by rerunning the code and testing the changes before applying them. One example of an AI suggestion that was incorrect or misleading was initially with the go higher and go lower hints. After testing changes, I realized that the AI had made lots of changes to my code, but the code was still behaving incorrectly. I had to go back and undo those changes and better articulate what changes I wanted with the AI to get what I wanted. After verifying which lines specifically I needed to change when looking back at the suggested changes, I double checked the AI's work and was able to only make the changes I needed, which I then tested and verified myself.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided that a bug was really fixed when I ran the code and ran several test cases myself to make sure that the code was not breaking anywhere. I also used pytest to run 8 test cases, all of which passed when run. This showed me that the bugs in the code from earlier were no longer appearing and that the code was more likely to behave as expected. AI did help me design and understand the test cases as it told me both what the test was for and what the test catches. Through these descriptions, I was better able to understand what each test cases purpose was.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because Streamlit reruns the whole script every time I clicked a button, so the random number line kept running again. I would explain Streamlit reruns as a refresh, that causes the code to keep running over and over again every time you interact with it. Session state serves as a saved memory that saves when you refresh, so without keeping that updated, variables refresh. We were able to make this fix by storing the secret in st.session_state.secret and only creating it once when "secret" was not already in st.session_state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I definitely want to use AI to create more test cases in future labs and projects. I also am glad that I got the opportunity to become more familiar with Git. One thing that I would do differently next time would be to spend more time on creating good test cases as well as thoroughly understanding what each of my changes do and asking the AI more questions. This project changed the way I think about AI generated code in that it is much more optimized and time efficient than manual code. However, I also realized how powerful it is in the way that it can almost be too aggressive with the changes it makes, which is why it's important to double check the code.