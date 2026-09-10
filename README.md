
# 🗣️ BhashaQuest

### Learn Languages. Play Adventures. Speak With Confidence.

**BhashaQuest** is an AI-powered, gamified language-learning platform that helps users learn languages through **interactive games, real-life situations, AI guidance, and voice-based challenges**.

Instead of memorizing vocabulary from a traditional language-learning app, users enter a virtual world where they interact with characters and complete everyday missions by actually **speaking the language**.

> 🎮 **Explore → Learn → Speak → Complete Missions → Earn XP → Unlock Levels**

---

## 🌟 The Problem

Learning a new language can often feel repetitive and disconnected from real-life communication.

Users may know individual words but still struggle when they actually need to:

* Greet someone
* Introduce themselves
* Order food or drinks
* Ask for directions
* Have a simple conversation

Most importantly, learners often hesitate to **speak** because they are afraid of making mistakes.

---

## 💡 Our Solution

BhashaQuest turns language learning into an **interactive adventure**.

The user enters a virtual environment and encounters real-world situations.

For example:

> You are walking through a garden and want to make a new friend.

The game asks:

> **“How would you greet this person in Hindi?”**

If the player doesn't know what to say, they can ask the built-in **AI Language Mentor**.

The AI doesn't simply provide the answer. It guides the player with hints, explanations, pronunciation and meaning.

The player then uses the microphone to speak the phrase.

The speech is converted into text, evaluated, and the player receives feedback.

If successful:

> 🎉 Mission Complete! +20 XP

The player can then continue to the next challenge.

---

# 🎮 Core Gameplay

```text
Explore
   ↓
Meet NPC
   ↓
Receive Mission
   ↓
Don't know what to say?
   ↓
Ask AI Mentor
   ↓
Learn Phrase
   ↓
Listen to Pronunciation
   ↓
Speak
   ↓
Speech Recognition
   ↓
Evaluate Answer
   ↓
Receive Feedback
   ↓
Complete Mission
   ↓
Earn XP
   ↓
Unlock Next Level
```

---

# 🤖 AI Language Mentor

The AI chatbot is available beside the game as a **personal language mentor**.

It understands the current game context and helps the player learn what they need for the current situation.

### Example

**Player:**

> How do I greet someone in Hindi?

**AI Mentor:**

> You can use a respectful greeting. I'll teach you how to say it and help you practice.

The mentor can provide:

* 📝 Useful phrases
* 🔊 Pronunciation
* 🌐 Meaning
* 💡 Hints
* 📚 Grammar explanations
* ❌ Mistake explanations
* 💬 Conversation examples

### Progressive Hint System

The AI should avoid making the game too easy.

Instead of immediately giving the answer:

```text
Hint 1
Think about what you normally say when meeting someone.

        ↓

Hint 2
Start with a respectful greeting.

        ↓

Hint 3
Here is the phrase. Listen and try saying it.
```

This allows the player to **learn rather than simply copy answers**.

---

# 🎤 Voice-Based Learning

One of the main features of BhashaQuest is **speaking practice**.

The player can press:

```text
🎤 TAP TO SPEAK
```

The application listens to the user's voice and converts it into text.

Example:

```text
User speaks
     ↓
Speech Recognition
     ↓
"You said: Namaste"
     ↓
Answer Evaluation
     ↓
Score + Feedback
```

The system should tolerate minor speech-recognition differences rather than requiring an exact string match.

### Example Scoring

| Score   | Feedback        |
| ------- | --------------- |
| 90–100% | ⭐ Excellent     |
| 70–89%  | 👍 Good         |
| 50–69%  | 🟡 Almost there |
| < 50%   | 🔄 Try again    |

---

# 🌳 Game Levels

## Level 1 — Garden 🌳

### Mission: Make a New Friend

The player enters a public garden and encounters an NPC.

The objective is to:

* Greet the person
* Introduce yourself
* Ask their name
* Have a basic conversation

The player can ask the AI mentor for help and then practice speaking.

### Reward

**+10 XP**

🏅 First Conversation Badge

---

## Level 2 — Chai Stall ☕

### Mission: Order Tea

The player reaches a local tea stall.

The objective is to communicate with the chai vendor.

The player needs to:

* Get the vendor's attention
* Order tea
* Specify what they want
* Say thank you

The player learns the required phrases from the AI mentor and then speaks them to the vendor.

### Reward

**+20 XP**

🏅 Chai Master Badge

---

## Level 3 — City 🏙️

### Mission: Ask for Directions

The player is exploring an unfamiliar city and needs to find a railway station.

The objective is to:

* Approach someone
* Ask for directions
* Understand the response
* Thank the person

The NPC reacts according to the player's response.

### Reward

**+30 XP**

🏅 Explorer Badge

---

# 🏆 Gamification

BhashaQuest uses game mechanics to keep users motivated.

### XP System

| Action                   |       XP |
| ------------------------ | -------: |
| Complete challenge       |      +10 |
| Excellent pronunciation  |      +20 |
| Complete level           |      +50 |
| Complete without hints   | Bonus XP |
| Complete daily challenge | Bonus XP |

### Progression

```text
🌱 Beginner
      ↓
🌿 Explorer
      ↓
🌳 Communicator
      ↓
🏆 Language Master
```

Users can unlock:

* XP
* Badges
* Levels
* Streaks
* Vocabulary
* Pronunciation scores
* Achievements

---

# 📚 Learning Progress

The application tracks the user's learning journey.

Example:

```text
Words Learned:        42
Phrases Learned:      18
Levels Completed:      3
Pronunciation Score:  87%
Current Streak:        5 days
Total XP:             420
```

After every level, the user receives a summary:

### What You Learned

* New vocabulary
* Useful phrases
* Pronunciation feedback
* Mistakes
* Score
* XP earned

---

# 🌎 Supported Languages

The first version focuses on **Hindi**, but the application is designed to support multiple languages.

Planned languages:

* 🇮🇳 Hindi
* 🇮🇳 Bengali
* 🇮🇳 Tamil
* 🇮🇳 Telugu
* 🇮🇳 Marathi
* 🇮🇳 Gujarati
* 🇮🇳 Punjabi
* 🇮🇳 Kannada
* 🇮🇳 Malayalam
* 🇮🇳 Odia

The language system should be modular so new languages can be added without rewriting the game.

---

# 🖥️ User Interface

The website is designed as a game rather than a traditional educational platform.

### Desktop

```text
┌────────────────────────────────────────────────────┐
│ BhashaQuest     Progress      XP       Profile     │
├────────────────────────────────────────────────────┤
│                                                    │
│                GAME ENVIRONMENT                    │
│                                                    │
│         🧑 Player              🧑 NPC              │
│                                                    │
│                                                    │
├───────────────────────────────┬────────────────────┤
│       GAME OBJECTIVE          │   🤖 AI MENTOR     │
│                               │                    │
│                               │   Chat interface   │
│                               │                    │
│                               │   🎤 Speak         │
└───────────────────────────────┴────────────────────┘
```

On mobile, the AI mentor becomes a collapsible bottom panel so that the game remains the primary focus.

---

# 🏗️ System Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │  React Frontend │
                  │                 │
                  │ Game + Chat UI  │
                  └────────┬────────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
      Speech Recognition            AI Chatbot
             │                           │
             ▼                           ▼
      Speech Evaluation          FastAPI Backend
             │                           │
             │                           ▼
             │                       LLM API
             │
             ▼
       Game Progress
             │
             ▼
        XP / Badges
```

---

# 🛠️ Tech Stack

## Frontend

* React.js
* JavaScript
* HTML5
* CSS3
* React Router
* Web Speech API
* Framer Motion

## Backend

* Python
* FastAPI

## AI

* LLM API
* Context-aware AI Language Mentor

## Speech

* Browser Speech Recognition
* Speech-to-Text
* Pronunciation/answer evaluation

## Storage

For the initial MVP:

* LocalStorage

For production:

* Database
* User authentication
* Persistent learning progress

---

# 📁 Project Structure

```text
BhashaQuest/
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Chatbot.jsx
│   │   │   ├── ChatMessage.jsx
│   │   │   ├── VoiceButton.jsx
│   │   │   ├── GameScene.jsx
│   │   │   ├── Player.jsx
│   │   │   ├── NPC.jsx
│   │   │   ├── ObjectiveCard.jsx
│   │   │   ├── ProgressBar.jsx
│   │   │   ├── XPDisplay.jsx
│   │   │   ├── Badge.jsx
│   │   │   └── LevelComplete.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── LanguageSelection.jsx
│   │   │   ├── Game.jsx
│   │   │   └── Profile.jsx
│   │   │
│   │   ├── data/
│   │   │   ├── languages.js
│   │   │   ├── levels.js
│   │   │   └── vocabulary.js
│   │   │
│   │   ├── services/
│   │   │   ├── speechService.js
│   │   │   ├── chatbotService.js
│   │   │   └── gameService.js
│   │   │
│   │   └── context/
│   │       └── GameContext.jsx
│   │
│   └── package.json
│
├── backend/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── chatbot.py
│   │   ├── game.py
│   │   └── speech.py
│   │
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── evaluation_service.py
│   │   └── language_service.py
│   │
│   └── models/
│       └── schemas.py
│
└── README.md
```

---

# 🔌 API Design

### Chatbot

```http
POST /api/chat
```

Request:

```json
{
  "message": "How do I greet someone?",
  "targetLanguage": "Hindi",
  "nativeLanguage": "English",
  "level": 1,
  "location": "garden",
  "objective": "Greet a new person"
}
```

---

### Speech Evaluation

```http
POST /api/evaluate-speech
```

Request:

```json
{
  "expectedPhrase": "Namaste",
  "recognizedSpeech": "Namastay",
  "targetLanguage": "Hindi"
}
```

Response:

```json
{
  "score": 92,
  "correct": true,
  "feedback": "Great job!",
  "mistakes": []
}
```

---

### Game Progress

```http
POST /api/progress
GET /api/progress/{user_id}
```

---

# 🔐 Security

AI API keys must **never** be stored in the React frontend.

Use:

```text
React
  ↓
FastAPI
  ↓
AI API
```

Environment variables should be used for secrets:

```text
.env
```

Example:

```text
AI_API_KEY=your_api_key
```

Never commit `.env` to GitHub.

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone <repository-url>
cd BhashaQuest
```

## 2. Install frontend dependencies

```bash
cd frontend
npm install
```

## 3. Start the frontend

```bash
npm run dev
```

## 4. Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

## 5. Start FastAPI

```bash
uvicorn main:app --reload
```

---

# 🎯 MVP Roadmap

### Phase 1 — Frontend

* [ ] Landing page
* [ ] Language selection
* [ ] Game interface
* [ ] Garden environment
* [ ] NPC interaction
* [ ] Chatbot UI

### Phase 2 — Voice

* [ ] Microphone button
* [ ] Speech recognition
* [ ] Speech-to-text
* [ ] Answer matching
* [ ] Score system

### Phase 3 — Game

* [ ] Garden level
* [ ] Chai stall level
* [ ] Directions level
* [ ] Level completion
* [ ] XP system
* [ ] Badges

### Phase 4 — AI

* [ ] FastAPI backend
* [ ] LLM integration
* [ ] Context-aware chatbot
* [ ] Progressive hints
* [ ] Mistake explanations

### Phase 5 — Expansion

* [ ] More languages
* [ ] User accounts
* [ ] Database
* [ ] Leaderboard
* [ ] Daily challenges
* [ ] Advanced pronunciation evaluation

---

# 🌟 Future Vision

BhashaQuest can eventually become a platform where users learn languages by **living through virtual situations**.

Future scenarios could include:

```text
🌳 Garden
      ↓
☕ Chai Stall
      ↓
🛍️ Market
      ↓
🚆 Railway Station
      ↓
🏥 Hospital
      ↓
🏨 Hotel
      ↓
🍽️ Restaurant
      ↓
🏠 Neighborhood
```

Instead of learning:

> “Here are 50 words you need to memorize.”

BhashaQuest focuses on:

> **“You are in this situation. What do you want to say?”**

The AI helps you learn it, and the game makes you **actually speak it**.

---

# 💭 Vision

Our vision is to make language learning feel less like studying and more like **going on an adventure**.

### Learn the language.

### Enter the world.

### Talk to people.

### Complete the mission.

### Become a better communicator.

---

## ❤️ BhashaQuest

**Learn Languages. Play Adventures. Speak With Confidence.**

> **Don't just learn a language. Experience it.**
