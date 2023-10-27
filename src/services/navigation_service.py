from customtkinter import CTkToplevel, CTk


class NavigationService:
    def __init__(self):
        self.routes: dict[str, CTk | CTkToplevel] = {}

    def register(self, route: str, view: CTkToplevel) -> None:
        self.routes[route] = view

    def destroy_route(self, route: str) -> None:
        self.routes[route].destroy()

    def register_and_mainloop(self, route: str, view: CTk) -> None:
        self.routes[route] = view
        self.routes[route].mainloop()

    def navigate(self, route: str) -> None:
        self.routes[route].deiconify()

    def navigate_and_withdraw(self, route: str, current: CTk | CTkToplevel) -> None:
        current.withdraw()
        self.routes[route].deiconify()
