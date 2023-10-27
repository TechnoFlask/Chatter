from customtkinter import CTkScrollableFrame, CTkButton
from tkinter import StringVar
from textwrap import wrap


class ChatViewModel:
    def __init__(self):
        self.chat_message: StringVar = StringVar()
        self.chats_list: list[CTkButton] = []

    def add_chat_client(self, chats_frame: CTkScrollableFrame):
        chat_text = self.chat_message.get()
        if len(chat_text) == 0:
            return
        chat_text = '\n'.join(wrap(chat_text, 50))
        chat: CTkButton = CTkButton(chats_frame, width=350, text=chat_text,
                                    font=('Century Gothic', 14), height=60, fg_color='#fbc531', hover_color='#e1b12c',
                                    text_color='#2f3640')
        chat.pack(padx=10, pady=10, anchor='e')
        self.chats_list.append(chat)

        self.chat_message.set('')

    def receive_chat_client(self, chats_frame: CTkScrollableFrame):
        chat_text = 'Sample Text'
        chat_text = '\n'.join(wrap(chat_text, 50))
        chat: CTkButton = CTkButton(chats_frame, width=350, text=chat_text,
                                    font=('Century Gothic', 14), height=60, fg_color='#f5f6fa', hover_color='#dcdde1',
                                    text_color='#2f3640')
        chat.pack(padx=10, pady=10, anchor='w')
        self.chats_list.append(chat)

        self.chat_message.set('')
