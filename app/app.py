from fastai.vision.all import *
import gradio as gr


waste_labels=['Electronic waste',
              'Glass waste',
              'Medical waste',
              'Metal waste',
              'Organic waste',
              'Paper waste',
              'Plastic waste',
              'Shoes Waste',
              'Textile waste',
              'Wood waste']

model=load_learner('models/waste-recognizer-v1.pkl')

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(waste_labels, map(float, probs)))


image = gr.Image()
label = gr.Label()

# Example images
examples = [
    'test_images/unknown1.jpg',
    'test_images/unknown2.jpg',
    'test_images/unknown3.jpeg',
    'test_images/unknown4.jpg'
]

# Define the interface
iface = gr.Interface(
    fn=recognize_image,  # Your function to recognize images
    inputs=image,
    outputs=label,
    examples=examples
)

# Launch the interface
iface.launch(inline=False)