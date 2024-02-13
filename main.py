import os
from tkinter import Tk,ttk,filedialog,Canvas,PhotoImage,Frame
from tkinter import *
from PIL import Image,ImageTk, ImageDraw,ImageFont











def main():

    img_list=[]
    img_data={}

    def upload():
        filename = filedialog.askopenfilename()
        print (f"Uploading {filename}")
        image=ImageTk.PhotoImage(Image.open(filename))
        img_list.append(image)
        img_data["path"]=filename

        print (img_data)
        img_height=img_list[0].height()
        img_width=img_list[0].width()
        
        canvas.create_image(200,200,image=img_list[0])
        
        print (f"size of picture is {img_height}x{img_width}")
        lbl_size.config(text=f"{img_width}x{img_height}")
        canvas.place(x=100,y=100,anchor="center")
        canvas.pack()

    def watermark():

        img=img_data["path"]

        with Image.open(img) as im:
            
            watermark=ImageDraw.Draw(im)
            font = ImageFont.truetype("Arial.ttf", 30)
            fill_color = (203,201,201)
            watermark_text = "J@Wi"
            width,height =im.size
            x=width - width + 50
            y=height -50

            position=(x,y)
            print (position)
            watermark.text(xy = position, text = watermark_text, font = font, fill = fill_color)
            im.show()
        


    def resize():
        pass

  


    root = Tk("Waterworks")
    root.title("WaterWorks")
    root.geometry("800x800")
    frm = Frame(master=root,highlightbackground="green",bg="grey",height=20,width=20)
    frm.pack(padx=5,pady=5,fill="both",expand=True,side="left")
    frm2 = Frame(master=root,highlightbackground="blue",bg="white",height=20,width=500,pady=20)
    frm2.pack(padx=5,pady=5,fill="both",expand=True,side="right")
    btn_rsz=Button(frm,text="Resize",command=resize,highlightbackground="grey",width=8)
    btn=Button(frm,text="Upload",command=upload,highlightbackground="grey",width=8)
    btn_water=Button(frm,text="WaterMark",command=watermark,highlightbackground="grey",width=8)
    lbl_size=Label(frm,text="Size: ",highlightbackground="grey",bg="Grey",fg="black",font=("Arial",20))
    lbl_size.place(relx=0.0 ,rely=0.99,anchor="sw",)
    btn.place(x=25,y=40)
    btn_rsz.place(x=25,y=80)
    btn_water.place(x=25,y=120)
    canvas=Canvas(frm2,width=500,height=500)
  
    

   





    root.mainloop()
if __name__ == "__main__":
    main()