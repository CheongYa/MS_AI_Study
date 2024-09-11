import gradio as gr

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    input_text = gr.Textbox(label="메시지 입력")
    send_button = gr.Button("전송")

demo.launch(server_name="127.0.0.1", server_port=7860)