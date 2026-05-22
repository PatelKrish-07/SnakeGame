# Retro Snake Game 🐍

A classic arcade-style Snake Game built with Python using the native `turtle` graphics library. The project features full 4-way movement, dynamic food consumption, tail/wall collision mechanics, and a persistent high-score management system using local file storage.

---

## 🎮 Game Features

- **Classic Core Mechanics**: Guide the snake to eat the blue food tokens, growing longer with each item consumed.
- **Persistent High Scores**: High scores are automatically cached and saved locally in a `data.txt` file, preserving your best record across gaming sessions.
- **Collision Detection**: Real-time collision monitoring checks for boundaries (walls) and self-intersection (biting the tail), resetting the snake seamlessly when game-over triggers.
- **Smooth Animations**: Leverages custom screen tracer updates to disable frame flickering, presenting a smooth 10Hz screen refresh rate.

---

## 🛠️ Project Structure

The codebase is modularly designed and split across five key source files:

- **`Smain.py`**: The entry point and primary engine of the game loop. It handles window initialization, event listening for keypresses, synchronization, and collision resolutions.
- **`snake.py`**: Contains the encapsulation of the `Snake` class, governing snake segment allocations, head orientation logic, position transformations, and length extensions.
- **`food.py`**: Implements the `Food` class, a custom sub-classed `Turtle` object that randomly re-allocates itself on a $600 \times 600$ grid matrix when eaten.
- **`scoreboard.py`**: Contains the `Score` tracker class. It handles string writing to the screen frame and handles automated local I/O interactions.
- **`data.txt`**: A light-weight flat-file datastore storing the single persistent integer high-score value.

---

## 🕹️ Controls

Control the direction of the snake using your keyboard's standard arrow keys:

- **🔼 Up Arrow**: Directs the snake upwards (blocked if currently moving downwards).
- **🔽 Down Arrow**: Directs the snake downwards (blocked if currently moving upwards).
- **◀️ Left Arrow**: Directs the snake to the left (blocked if currently moving to the right).
- **▶️ Right Arrow**: Directs the snake to the right (blocked if currently moving to the left).

---
