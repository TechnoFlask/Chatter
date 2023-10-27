from customtkinter import CTkToplevel, CTkLabel, CTkFrame, CTkEntry, CTkButton
from src.services.navigation_service import NavigationService


class RegistrationView(CTkToplevel):
    def __init__(self, navigation_service: NavigationService) -> None:
        super().__init__()
        self.title('Registration')
        self.geometry('500x500')
        self.resizable(False, False)
        self.configure(fg_color='#dcdde1')
        self.protocol('WM_DELETE_WINDOW', lambda: navigation_service.destroy_route('login'))

        self.registration_label: CTkLabel = CTkLabel(self, text='Registration', font=('Century Gothic', 24))
        self.registration_label.place(relx=0.5, rely=0.05, anchor='center')

        self.registration_frame: CTkFrame = CTkFrame(self, fg_color='#40739e', corner_radius=10)
        self.registration_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor='center')

        self.username_label: CTkLabel = CTkLabel(self.registration_frame, text='Username', font=('Century Gothic', 15),
                                                 text_color='#f5f6fa')
        self.username_label.place(relx=0.1, rely=0.1)

        self.username_entry: CTkEntry = CTkEntry(self.registration_frame, font=('Century Gothic', 12))
        self.username_entry.place(relx=0.1, rely=0.18, relwidth=0.8)

        self.password_label: CTkLabel = CTkLabel(self.registration_frame, text='Password', font=('Century Gothic', 15),
                                                 text_color='#f5f6fa')
        self.password_label.place(relx=0.1, rely=0.3)

        self.password_entry: CTkEntry = CTkEntry(self.registration_frame, font=('Century Gothic', 12), show='*')
        self.password_entry.place(relx=0.1, rely=0.38, relwidth=0.8)

        self.confirm_password_label: CTkLabel = CTkLabel(self.registration_frame, text='Confirm Password',
                                                         font=('Century Gothic', 15), text_color='#f5f6fa')
        self.confirm_password_label.place(relx=0.1, rely=0.5)

        self.confirm_password_entry: CTkEntry = CTkEntry(self.registration_frame, font=('Century Gothic', 12), show='*')
        self.confirm_password_entry.place(relx=0.1, rely=0.58, relwidth=0.8)

        self.register_button: CTkButton = CTkButton(self.registration_frame, text='Register',
                                                    font=('Century Gothic', 14), fg_color='#e1b12c',
                                                    hover_color='#fbc531', text_color='#2f3640')
        self.register_button.place(relx=0.1, rely=0.7, relwidth=0.8)

        self.already_have_account_label: CTkLabel = CTkLabel(self.registration_frame, text='Already have an account?',
                                                             font=('Century Gothic', 12), text_color='#f5f6fa')
        self.already_have_account_label.place(relx=0.1, rely=0.85)

        self.login_button: CTkButton = CTkButton(self.registration_frame, text='Login', font=('Century Gothic', 12),
                                                 fg_color='#e1b12c', hover_color='#fbc531', text_color='#2f3640',
                                                 command=lambda: navigation_service.navigate_and_withdraw(
                                                     'login', self))
        self.login_button.place(relx=0.6, rely=0.85)
