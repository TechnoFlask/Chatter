from services.navigation_service import NavigationService
from pages.views.registration_view import RegistrationView
from pages.views.chat_view import ChatView
from pages.views.login_view import LoginView


if __name__ == '__main__':
    navigation_service = NavigationService()
    login_view = LoginView(navigation_service)
    registration_view = RegistrationView(navigation_service)
    chat_view = ChatView(navigation_service)

    registration_view.withdraw()
    chat_view.withdraw()

    navigation_service.register('registration', registration_view)
    navigation_service.register('chat', chat_view)
    navigation_service.register_and_mainloop('login', login_view)
