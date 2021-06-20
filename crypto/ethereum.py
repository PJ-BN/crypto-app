import requests




class Ethereum:
    
    def __init__(self):
        
        super().__init__()
        self.response = requests.get("https://api.lunarcrush.com/v2?data=assets&key=uxkfgytdeqkm4m2o4nhu&symbol=ETH&data_points=365&interval=day")
        datas = self.response.json()
        self.data = datas["data"]
        self.current_price = 0  
        self.y_diff = 0
        self.w_diff = 0  
        self.m_diff = 0 
        self.y_per = 0
        self.w_per = 0
        self.m_per = 0         
        
        
    def current(self):
        
        
        for value in self.data:
            
            self.current_price = value["price"]
             
             
             
        return self.current_price
    
    
    def yesterday(self):
        
        for value in self.data:
            
            self.current_price = value["price"]
            self.y_per = value["percent_change_24h"]
            
        y_val = self.current_price - (self.y_per/100)*self.current_price
        self.y_diff = y_val - self.current_price
        self.y_diff = -self.y_diff
        return y_val
    
    
    def last_week(self):
        
        for value in self.data:
            
            self.current_price = value["price"]
            self.w_per = value["percent_change_7d"]
            
        w_val = self.current_price - (self.w_per/100)*self.current_price
        self.w_diff = w_val - self.current_price
        self.w_diff = -self.w_diff
        return w_val
    
    
    def last_month(self):
        
        for value in self.data:
            
            self.current_price = value["price"]
            self.m_per = value["percent_change_30d"]
            
        m_val = self.current_price - (self.m_per/100)*self.current_price
        self.m_diff = m_val - self.current_price
        self.m_diff = -self.m_diff
        return m_val
    
    