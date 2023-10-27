from customtkinter import CTkToplevel, CTkLabel, CTkFrame, CTkScrollableFrame, CTkEntry, CTkButton
from src.services.navigation_service import NavigationService
from src.pages.view_models.chat_view_model import ChatViewModel

lorem_ipsum = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt '
               'ut labore et dolore magna aliqua.')


class ChatView(CTkToplevel):
    def __init__(self, navigation_service: NavigationService):
        super().__init__()
        self.title('Chat')
        self.geometry('1280x720')
        self.resizable(False, False)
        self.configure(fg_color='#dcdde1')
        self.protocol('WM_DELETE_WINDOW', lambda: navigation_service.destroy_route('login'))

        self.view_mddel: ChatViewModel = ChatViewModel()

        self.add_contact_frame: CTkFrame = CTkFrame(self, corner_radius=0, fg_color='#7f8fa6')
        self.add_contact_frame.place(relx=0.01, rely=0.02, relwidth=0.3, relheight=0.2, anchor='nw')

        self.add_contact_label: CTkLabel = CTkLabel(self.add_contact_frame, text='Add Contact',
                                                    font=('Century Gothic', 24), text_color='#f5f6fa')
        self.add_contact_label.place(relx=0.5, rely=0.15, anchor='center')

        self.add_contact_entry: CTkEntry = CTkEntry(self.add_contact_frame, font=('Century Gothic', 12))
        self.add_contact_entry.place(relx=0.5, rely=0.5, relwidth=0.8, anchor='center')

        self.add_contact_button: CTkButton = CTkButton(self.add_contact_frame, text='Add Contact',
                                                       font=('Century Gothic', 12), fg_color='#e1b12c',
                                                       hover_color='#fbc531', text_color='#2f3640')
        self.add_contact_button.place(relx=0.5, rely=0.8, relwidth=0.8, anchor='center')

        self.contacts_frame: CTkScrollableFrame = CTkScrollableFrame(self, corner_radius=0, fg_color='#7f8fa6',
                                                                     scrollbar_button_color='#273c75',
                                                                     scrollbar_button_hover_color='#192a56')
        self.contacts_frame.place(relx=0.01, rely=0.22, relwidth=0.3, relheight=0.76, anchor='nw')

        for i in range(3):
            CTkButton(self.contacts_frame, text=f'Contact {i}', font=('Century Gothic', 16), height=60,
                      corner_radius=0, fg_color='#353b48', hover_color='#2f3640', text_color='#f5f6fa').pack(
                expand=True, fill='x')

        self.contact_info_frame: CTkFrame = CTkFrame(self, corner_radius=0, fg_color='#7f8fa6')
        self.contact_info_frame.place(relx=0.31, rely=0.02, relwidth=0.67, relheight=0.08, anchor='nw')

        self.contact_info_label: CTkLabel = CTkLabel(self.contact_info_frame, text='Contact Info',
                                                     font=('Century Gothic', 24), text_color='#f5f6fa')
        self.contact_info_label.place(relx=0.5, rely=0.5, anchor='center')

        self.chat_frame: CTkScrollableFrame = CTkScrollableFrame(self, corner_radius=0, fg_color='#273c75')
        self.chat_frame.place(relx=0.31, rely=0.1, relwidth=0.669, relheight=0.8, anchor='nw')

        anchor = 'e'
        #for i in range(100):
        #    text = '\n'.join(wrap(lorem_ipsum, 50))
        #    color = '#fbc531' if anchor == 'e' else '#f5f6fa'
        #    CTkButton(self.chat_frame, width=350, text=text, font=('Century Gothic', 14),
        #              height=60, fg_color=color, hover_color=color, text_color='#2f3640').pack(padx=10, pady=10,
        #                                                                                       anchor=anchor)
        #    anchor = 'w' if anchor == 'e' else 'e'

        self.typing_frame: CTkFrame = CTkFrame(self, corner_radius=0, fg_color='#7f8fa6')
        self.typing_frame.place(relx=0.31, rely=0.9, relwidth=0.67, relheight=0.08, anchor='nw')

        self.typing_entry: CTkEntry = CTkEntry(self.typing_frame, font=('Century Gothic', 12), corner_radius=20,
                                               textvariable=self.view_mddel.chat_message)
        self.typing_entry.place(relx=0.01, rely=0.5, relwidth=0.8, relheight=0.8, anchor='w')

        self.send_button: CTkButton = CTkButton(self.typing_frame, text='Send', font=('Century Gothic', 12),
                                                fg_color='#e1b12c', hover_color='#fbc531', text_color='#2f3640',
                                                command=lambda: self.view_mddel.add_chat_client(self.chat_frame))
        self.send_button.place(relx=0.99, rely=0.5, relwidth=0.16, relheight=0.7, anchor='e')

        self.debug_receive_button: CTkButton = CTkButton(self.typing_frame, text='Receive', font=('Century Gothic', 12),
                                                fg_color='#e1b12c', hover_color='#fbc531', text_color='#2f3640',
                                                command=lambda: self.view_mddel.receive_chat_client(self.chat_frame))
        self.debug_receive_button.place(relx=0.8, rely=0.5, relwidth=0.16, relheight=0.7, anchor='e')
