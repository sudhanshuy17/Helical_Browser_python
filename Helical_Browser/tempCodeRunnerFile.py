       home_btn = QAction('home', self)
        home_btn.triggered.connect(self.nevigate_home)
        navbar.addAction(home_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))       
       