from dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        # Creating local page variable by using self
        # page object that is coming from test we are attaching to local class object.
        # Local variables can be call from any place within the class by using self. + variable name
        self.page = page


    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, userName, password):
        self.page.get_by_placeholder("email@example.com").fill(userName)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage









# Here we will write methods that belongs to login page