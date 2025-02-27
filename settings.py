class Settings:
    """Class for game settings"""
    
    
    def __init__(self):
        """initialize game settings"""
        #screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 139)
        self.caption = "Bubble Bluster"
        
        self.bubble_min_r = 10
        self.bubble_max_r = 50
        