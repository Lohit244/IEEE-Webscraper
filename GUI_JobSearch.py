from tkinter import *
from PIL import ImageTk, Image
import indeed as indeed
import webbrowser
from tkinter import ttk
import naukri as naukri
import linkedin as linkedin

root = Tk()
root.title("Job Search")
root.configure(background='#101E3F')

# This dict will store all the urls for specific notbook elements

global urlDict
urlDict = {}
def open_url():
    k = notebook.tab(notebook.select(), "text")
    link = urlDict[k]
    webbrowser.open(link,new=1)

# Self Explanatory

def deletetab():
    for tab in notebook.winfo_children():
        if str(tab) == (notebook.select()):
            tab.destroy()
            return 

def handle_search():

    # Get Data from Entries
    
    website = (comboBox.get())
    job_title = jobtitle.get()
    location_to_search = location.get()
    
    # Get Data from Webscrape Modules
    
    if website == "Naukri.com":
        try:
            a = naukri.load_naukri_jobs(job_title,location_to_search)
            titles = list(naukri.getTitle(a))
            companies = list(naukri.getCompany(a))
            rating = list(naukri.getCompanyRating(a))
            loc = list(naukri.getLocation(a))
            full_url = list(naukri.getUrl(a))
            exp = list(naukri.getExp(a)) 
            salary= list(naukri.getSalary(a)) 
        except:
            titles = []
    if website == "LinkedIn":
        try:
            soupData = linkedin.load_linkedin_jobs(job_title,location_to_search)
            titles = list(linkedin.getTitle(soupData))
            companies = list(linkedin.getCompany(soupData))
            full_url = list(linkedin.getData_Id(soupData))
            loc = list(linkedin.getLocation(soupData))
            dates = list(linkedin.getDate(soupData))
        except:
            titles=[]
    if website == "Indeed":
        try:
            soupObj = indeed.load_indeed_jobs(job_title,location_to_search)
            titles = list(indeed.getTitle(soupObj))
            loc = list(indeed.getLocation(soupObj))
            
            # full_summary = (str(list(indeed.getFullSummary(soupObj)))) # Not Using becuz its ugly to have so much text
            
            summary = list(indeed.getSummary(soupObj))
            salary = list(indeed.getSalary(soupObj))
            companies = list(indeed.getCompany(soupObj))
            full_url = list(indeed.getFullUrl(soupObj))
        except:
            titles = []
    if(titles==[]):
        # This is only for indeed when jibberish is passed but its good to handle theese cuz errors are bad
        result_frame = LabelFrame(notebook,padx=10,pady=10,borderwidth=0)
        result_frame.configure(background='#101E3F')
        result_frame.pack()
        notebook.add(result_frame, text = "Error")
        error_label = Label(result_frame ,text='Check Your Input',fg='white')
        error_label.configure(background='#101E3F')
        error_label.pack()
        close_button = Button(result_frame,text='Close',command=deletetab,width=25)
        close_button.pack()
    else:
        i = 0
        # Decided to limit to 5 results or it just looked way too cluttered
        while(titles[i] and i<5):
            
            # Universal(For All Sources) - >
            
            urlDict[website[0] + ' ' + str(i+1)+ ' ' + job_title+ ' ' +location_to_search] = full_url[i]
            result_frame = LabelFrame(notebook,padx=10,pady=10,borderwidth=0)
            result_frame.configure(background='#101E3F')
            result_frame.pack()
            notebook.add(result_frame, text = website[0] + ' ' + str(i+1)+ ' ' + job_title+ ' ' +location_to_search)
            title_label = Label(result_frame ,text=titles[i],fg='white',font=('Segoe UI', 15, 'bold'))
            title_label.configure(background='#101E3F')
            company_label = Label(result_frame ,text=companies[i],fg='white',font=('Segoe UI', 10, 'normal'))
            company_label.configure(background='#101E3F')
            loc_label = Label(result_frame ,text=loc[i],fg='white',font=('Segoe UI', 10, 'normal'))
            loc_label.configure(background='#101E3F')
            visit_button = Button(result_frame,text='Visit',command=open_url,width=25)
            title_label.pack()
            company_label.pack()
            loc_label.pack()
            close_button = Button(result_frame,text='Close',command=deletetab,width=25)
            
            # Site Specific ->
            
            # LinkedIn -> Date of posting 
            
            if website == "LinkedIn":
                dates_label = Label(result_frame ,text=('Posted ' + dates[i]),fg='white',font=('Segoe UI', 10, 'normal'))
                dates_label.configure(background='#101E3F')
                dates_label.pack()
            
            # Naukri.com -> Rating,Salary,Exp
            
            if website == "Naukri.com":
                rating_label = Label(result_frame ,text=('Company Rating - ' + rating[i]),fg='white',font=('Segoe UI', 10, 'normal'))
                rating_label.configure(background='#101E3F')
                rating_label.pack()
                salary_label = Label(result_frame ,text=('Salary - ' + salary[i]),fg='white',font=('Segoe UI', 10, 'bold'))
                salary_label.configure(background='#101E3F')
                salary_label.pack()
                exp_label = Label(result_frame ,text=('Experience Expected - '+ exp[i]),fg='white',font=('Segoe UI', 10, 'normal'))
                exp_label.configure(background='#101E3F')
                exp_label.pack()
            
            # Indeed -> Salary and Summary
            
            if website == "Indeed":
                salary_label = Label(result_frame ,text=salary[i],fg='white',font=('Segoe UI', 10, 'bold'))
                salary_label.configure(background='#101E3F')
                salary_label.pack()
                summary_label = Label(result_frame ,text=summary[i],fg='white',font=('Segoe UI', 10, 'normal'))
                summary_label.configure(background='#101E3F')
                summary_label.pack()
            
            # Not Site Specific but need to be at the bottom ->
            
            visit_button.pack()
            close_button.pack()
            i+=1

#  Image

image = Image.open('./logo.png')
image = image.resize((350, 350), Image.ANTIALIAS)
app_logo = ImageTk.PhotoImage(image)
app_logo_label = Label(root, image=app_logo)
app_logo_label.configure(background='#101E3F')
app_logo_label.pack(pady=50,padx=200)

# Frame to hold entry and comboBox elements

frame = LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame.configure(background='#101E3F')
frame.pack()

# Entries for query and Labels

jobtitle = Entry(frame,width=50,font=('Segoe UI', 10, 'normal'))
jobtitle_label = Label(frame,text="Job Title",fg='white',font=('Segoe UI', 10, 'normal'))
location = Entry(frame,width=50,font=('Segoe UI', 10, 'normal'))
location_label = Label(frame,text="Location",fg='white',font=('Segoe UI', 10, 'normal'))
jobtitle_label.configure(background='#101E3F')
location_label.configure(background='#101E3F')
jobtitle.grid(row=0,column=0)
jobtitle_label.grid(row=1,column=0)
location.grid(row=0,column=1)
location_label.grid(row=1,column=1)

# ComboBox & Label

comboBox = ttk.Combobox(frame,values=['LinkedIn','Naukri.com','Indeed'],state="readonly",font=('Segoe UI', 10, 'normal'),width=50)
comboBox.set('LinkedIn')
comboBox_label = Label(frame,text='Website',fg='white',font=('Segoe UI', 10, 'normal'))
comboBox_label.configure(background='#101E3F')
comboBox_label.grid(row=1,column=3)
comboBox.grid(row =0, column=3)

# Button

searchbtn = Button(frame,command=handle_search,text="Search",width=40)
searchbtn.grid(row=2,column=1)


# ResultFrame

notebook = ttk.Notebook(root)
notebook.pack(pady=30,padx=30, expand=True)


# Start mainloop

root.mainloop()