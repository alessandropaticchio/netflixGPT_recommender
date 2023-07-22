from input import process_input
import gradio as gr

demo = gr.Interface(
    fn=process_input,
    inputs=gr.Textbox(lines=2, label='Your emotions...', placeholder="How are you feeling today? 😊",
                      style="font-size: 18px;"),
    outputs=[gr.Image(label='Cover', height=200, width=100), gr.Text(label="Title"), gr.Text(label="Description"),
             gr.Text(label="Genres"), gr.Text(label="Emojis")],
    title="NetflixGPT Recommender",
    description="This is an application that recommends something to watch on Netflix based on how you feel today 😊! \n"
                "Just fill the input form explaining how you're feeling and the algorithm behind will select the best movie or TV"
                " series to watch for you 🍿! \n\n"
                "This application is built with LangChain 🔗, that interacts with OpenAI GPT3.5 🧠, and Milvus, a vector database 💽. \n"
                "It parses your input by summarizing with a set of emotions, and then searches the database looking for items"
                "that give out the same vibes.\n"
                "Bonus point: it also summarizes the plot of the movie/TV series with emojis... enjoy 🤗!",
    live=False,
    allow_flagging="never"
)

demo.launch(share=True, server_name="0.0.0.0", server_port=9999)
