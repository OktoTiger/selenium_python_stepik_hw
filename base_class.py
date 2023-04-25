
class Base():
    def __init__(self, browser):
        self.browser = browser
    

    """Method asset word""" 
    
    def assert_word(self, word, result):
        value_word = word.text
        result_word = result.text
        print("Значение в корзине: " + value_word, "Значение на главной странице: " + result_word) 
        assert value_word == result_word
        print("Проверка Продукта успешна.Ты красавчик!"), print(value_word, result_word)
    
    
        

