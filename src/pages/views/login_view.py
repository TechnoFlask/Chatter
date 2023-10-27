from customtkinter import CTk, CTkLabel, CTkFrame, CTkEntry, CTkButton
from src.services.navigation_service import NavigationService


class LoginView(CTk):
    def __init__(self, navigation_service: NavigationService) -> None:
        super().__init__()
        self.title('Login')
        self.geometry('500x500')
        self.resizable(False, False)
        self.configure(fg_color='#dcdde1')

        self.login_label: CTkLabel = CTkLabel(self, text='Login', font=('Century Gothic', 24))
        self.login_label.place(relx=0.5, rely=0.05, anchor='center')

        self.login_frame: CTkFrame = CTkFrame(self, fg_color='#40739e', corner_radius=10)
        self.login_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor='center')

        self.username_label: CTkLabel = CTkLabel(self.login_frame, text='Username', font=('Century Gothic', 15),
                                                 text_color='#f5f6fa')
        self.username_label.place(relx=0.1, rely=0.1)

        self.username_entry: CTkEntry = CTkEntry(self.login_frame, font=('Century Gothic', 12))
        self.username_entry.place(relx=0.1, rely=0.18, relwidth=0.8)

        self.password_label: CTkLabel = CTkLabel(self.login_frame, text='Password', font=('Century Gothic', 15),
                                                 text_color='#f5f6fa')
        self.password_label.place(relx=0.1, rely=0.3)

        self.password_entry: CTkEntry = CTkEntry(self.login_frame, font=('Century Gothic', 12), show='*')
        self.password_entry.place(relx=0.1, rely=0.38, relwidth=0.8)

        self.confirm_password_label: CTkLabel = CTkLabel(self.login_frame, text='Confirm Password',
                                                         font=('Century Gothic', 15), text_color='#f5f6fa')
        self.confirm_password_label.place(relx=0.1, rely=0.5)

        self.confirm_password_entry: CTkEntry = CTkEntry(self.login_frame, font=('Century Gothic', 12), show='*')
        self.confirm_password_entry.place(relx=0.1, rely=0.58, relwidth=0.8)

        self.login_button: CTkButton = CTkButton(self.login_frame, text='Login', font=('Century Gothic', 14),
                                                 fg_color='#e1b12c', hover_color='#fbc531', text_color='#2f3640',
                                                 command=lambda: navigation_service.navigate_and_withdraw(
                                                     'chat', self))
        self.login_button.place(relx=0.1, rely=0.7, relwidth=0.8)

        self.not_registered_label: CTkLabel = CTkLabel(self.login_frame, text='Not Registered Yet?',
                                                       font=('Century Gothic', 12), text_color='#f5f6fa')
        self.not_registered_label.place(relx=0.1, rely=0.85)

        self.register_button: CTkButton = CTkButton(self.login_frame, text='Register', font=('Century Gothic', 12),
                                                    fg_color='#e1b12c', hover_color='#fbc531', text_color='#2f3640',
                                                    command=lambda: navigation_service.navigate_and_withdraw(
                                                        'registration', self))
        self.register_button.place(relx=0.6, rely=0.85)
