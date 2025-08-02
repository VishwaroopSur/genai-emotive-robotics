from emotion_detection.detect_emotion import detect_emotion
from genai_expression.generate_poem import generate_poem
from robot_interface.express_emotion import express

# Simulate user input
user_input = "I just lost my job and I feel terrible."

# Step 1: Detect emotion
emotion = detect_emotion(user_input)
print(f"Detected Emotion: {emotion}")

# Step 2: Generate creative expression
poem = generate_poem(emotion)
print("\nGenerated Poem:\n", poem)

# Step 3: Robot expression (mock output)
express(emotion)
