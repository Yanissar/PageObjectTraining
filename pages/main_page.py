from .base_page import BasePage

class MainPage(BasePage):

    # Заглушка, предложенная в ходе оптимизации
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    
    # Есть другой вариант реализации такой заглушки
    #def __init__(self):
        #pass