import PySimpleGUI as sg
import json
import os
import sys

#---------------------------------------------

LARGURA , ALTURA = 1024 , 600






#---------------------------------------------
class App():
    def __init__(self , icon_base ):
        super().__init__()
        #sg.theme('DarkAmber')

        

        self.read_theme_colors      = self.appTheme()
        self.size_inputs            = ( 33 , 40 )
        self.size_buttons           = ( 36 , 1 )

        self.font_texts_inputs      = "arial"
        self.font_texts             = "impact"

        #------------------------------------------------------------------
        #---------------- Layouts elements App ----------------------------



        self.layout_imagem = [ 
                                [ sg.Image( source = "images\Banner.png", size = (497 , 610 ) ) ]  
                             ]


        self.layoutInputs = [ 
                            
                            [ self.textWidget( text = "Nome" , text_color = self.read_theme_colors["texts"] , text_background_color = self.read_theme_colors["background"] ) ],

                            [ sg.InputText( size = self.size_inputs , font = self.font_texts_inputs , border_width = 0 , background_color = self.read_theme_colors["texts"]  , key = "_INPUT_NAME_" ,  ) ],


                            [ self.textWidget( text = "Email" , text_color = self.read_theme_colors["texts"] , text_background_color = self.read_theme_colors["background"] ) ],

                            [ sg.InputText( size = self.size_inputs , font = self.font_texts_inputs , border_width = 0 , background_color = self.read_theme_colors["texts"]  , key = "_INPUT_EMAIL_" ) ],


                            [ self.textWidget( text = "Senha" , text_color = self.read_theme_colors["texts"] , text_background_color = self.read_theme_colors["background"] ) ],

                            [ sg.InputText( size = self.size_inputs , font = self.font_texts_inputs , border_width = 0 , background_color = self.read_theme_colors["texts"]  ,  key = "_INPUT_SENHA_" ) ],

                         ]
        

        self.layout_button = [
                                [ sg.Button(button_text      = 'SALVA.TXT' , 
                                            size             = self.size_buttons ,
                                            font             = "impact",
                                            border_width     = 0 ,
                                            key              = "_BUTTON_SAVE_" ,
                                            button_color     = ( self.read_theme_colors["button"][1] , self.read_theme_colors["button"][2] ) ,
                                            mouseover_colors = self.read_theme_colors["texts"] )
                                ]

                            ]
        
                            
        self.col_inputs = [ 
                            [ sg.VPush( background_color = self.read_theme_colors["background"]  ) ],
                            
                            [ sg.Image( source = "images\Lock.png", background_color = self.read_theme_colors["background"]  ) ],

                            [ sg.VPush( background_color = self.read_theme_colors["background"]  ) ],

                            [ sg.Column( self.layoutInputs  , background_color = self.read_theme_colors["background"] ) ],
                            
                            [ sg.VPush( background_color = self.read_theme_colors["background"]  ) ] ,

                            [ sg.Column( self.layout_button  , background_color = self.read_theme_colors["background"] ) ],

                            [ sg.VPush( background_color = self.read_theme_colors["background"] ) ] ,

                            ]
        



        self.full_layout = [ 
                                # colunn image ------------------------------------------------------------------------
                                [ 
                                    sg.Column(  self.layout_imagem  , 
                                                    background_color        = self.read_theme_colors["background"] , 
                                                    #justification           = 'left', 
                                                    element_justification   = "Left",
                                                    pad                     = 0 , 
                                                    expand_y                = False ,
                                                    ),


                                    sg.Push( background_color = self.read_theme_colors["background"] ),


                                    # colunn INPUTs -------------------------------------------------------------------------
                                    sg.Column( self.col_inputs  , 
                                                background_color        = self.read_theme_colors["background"] ,
                                                #justification           = 'c',
                                                element_justification   = "center",
                                                pad                     = 0  , 
                                                expand_y                = True ),
                                    

                                    sg.Push( background_color = self.read_theme_colors["background"] ),

                                ],
                        
                        ]
        
        

        self.windon_app = sg.Window(  "Space Save Login", 
                                    background_color        = self.read_theme_colors["background"] ,
                                    size                    = ( LARGURA , ALTURA ) ,
                                    icon                    = "images\Lock.ico",
                                    finalize                = True,
                                    #transparent_color       = self.read_theme_colors["background"]  ,
                                    element_justification   = "center" ).layout( self.full_layout )
        pass
    
    

    #-------------------------------------------------------------------------------
    def textWidget( self , text = "" , text_color = "" , text_background_color = "" ):
        return sg.Text( text                = text , #size = (None, None),
                        auto_size_text      = True, 
                        font                = self.font_texts,
                        text_color          = text_color, 
                        background_color    = text_background_color,
                        border_width        = 0, 
                        justification       = "left"
                        )



    #-------------------------------------------------------------------------------
    def json_read(self , name_file ):
        with open( name_file + '.json', "r" , encoding="utf8") as js_file:
            return json.load(js_file)
        


    #-------------------------------------------------------------------------------
    def appTheme( self ):
        colors  = self.json_read( name_file = "database/app_colors" )
        theme   = colors["theme"]

        return {
                "background"    : theme["background"] , 
                "input_text"    : theme["input_text"] , 
                "button"        : theme["buttons_colors"] , 
                "texts"         : theme["texts"] 
                }
    
        pass

 

    #-------------------------------------------------------------------------------
    def salveLoginTxtFile(self , events , values ):

        
        if events == "_BUTTON_SAVE_":
            input_name  = values[ "_INPUT_NAME_"  ]
            input_email = values[ "_INPUT_EMAIL_" ]
            input_senha = values[ "_INPUT_SENHA_" ]
            #----------------------------------------
            out_path     = input_name + ".txt"
            text_txt_out = [ "NOME = "+ str( input_name ) + "\n" , "EMAIL = "+ str( input_email ) + "\n" , "SENHA = "+ str( input_senha ) + "\n"  ]


            with open(  out_path , 'w' ) as save_file:
                for ind , text_ in enumerate( text_txt_out ):
                    save_file.write( text_ )


        pass




#-------------------------------------------------------------------------------

    def main(self):
        #--------------------------------------------

        while True:
            events, values = self.windon_app.Read(  timeout = 10 )

            if events == sg.WIN_CLOSED or events == 'Cancel':
                break

            self.salveLoginTxtFile( events , values )








#-------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    icon_app_base64 = b"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"
    
    
    app_c = App( icon_base = icon_app_base64 )
    app_c.main()


