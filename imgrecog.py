import tkinter as tk
import openai

# OpenAI API key
openai.api_key = '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'

# Create a Tkinter window
window = tk.Tk()
window.title("Image Generator")

# Create a canvas to display the generated images
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Function to generate an image
def generate_image():
    # Generate an image description using OpenAI GPT-3.5 model
    prompt = "Generate an image of a cat"
    response = openai.Completion.create(
        engine="davinci", 
        prompt=prompt, 
        max_tokens=50, 
        n=1,
        stop=None,
        temperature=0.7
    )
    description = response.choices[0].text.strip()

    # Clear the canvas
    canvas.delete("all")

    # Display the generated image description
    canvas.create_text(200, 50, text="Generated Image:", font=("Arial", 14), fill="black")
    canvas.create_text(200, 100, text=description, font=("Arial", 12), fill="black")

    # Display the generated image (placeholder)
    canvas.create_rectangle(100, 150, 300, 350, fill="gray")

# Create a button to generate an image
generate_button = tk.Button(window, text="Generate Image", command=generate_image)
generate_button.pack()

# Run the Tkinter event loop
window.mainloop()
