import customtkinter
from tkinter import messagebox
import google.generativeai as genai

genai.configure(api_key="AIzaSyCJ2jhk3vCvFwIZL8GTb3yFnNxOcfiAHDs")

model = genai.GenerativeModel('gemini-2.5-flash')

customtkinter.set_default_color_theme("themes/breeze.json")
font="SF Pro Display"

data={"Interested Subjects": None, "Marks":None}
markList = []

welcome = customtkinter.CTk()
welcome.geometry("480x270")
welcome.title("Career Compass")
welcome.resizable(False, False)

presents = customtkinter.CTkLabel(welcome, text="Project Castor Presents", fg_color="transparent", font=(font, 20))
presents.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

title = customtkinter.CTkLabel(welcome, text="Career Compass", fg_color="transparent", font=(font, 40))
title.place(relx=0.5, rely=0.425, anchor=customtkinter.CENTER)

def pageTwoCanon():
    welcome.destroy()
    subjSelect = customtkinter.CTk()
    subjSelect.geometry("400x410")
    subjSelect.resizable(False, False)
    subjSelect.title("Career Compass: Interest Selector")

    subjs = ['Accounting', 'Acting', 'Agribusiness', 'Algebra', 'Anatomy & Physiology', 'Animation', 'Anthropology', 'Archaeology', 'Art History', 'Artificial Intelligence', 'Astronomy & Astrophysics', 'Automotive Technology', 'Aviation Mechanics', 'Biochemistry', 'Biology', 'Biomedical Science', 'Blockchain Technology', 'Botany', 'Business Ethics', 'Business Law', 'Business Management', 'Calculus', 'Carpentry', 'Ceramics', 'Chemistry', 'Civics', 'Classical Languages (e.g., Latin, Greek)', 'Climate Science', 'Cloud Computing', 'Combinatorics', 'Comparative Literature', 'Computational Thinking', 'Computer Graphics', 'Computer Networks', 'Construction Technology', 'Cosmetology', 'Costume Design', 'Creative Writing', 'Criminology', 'Culinary Arts', 'Cultural Studies', 'Cybersecurity', 'Data Science', 'Data Structures & Algorithms', 'Databases', 'Demography', 'Differential Equations', 'Digital Forensics', 'Digital Media Arts', 'Discrete Mathematics', 'Drama & Playwriting', 'Drawing & Illustration', 'Drone Operation & Maintenance', 'E-Commerce', 'Earth Science', 'Ecology & Environmental Science', 'Economics', 'Economics for Business', 'Editing & Publishing', 'Electrical & Electronics Technology', 'Embedded Systems', 'English Literature', 'Entrepreneurship', 'Essay Writing & Composition', 'Fashion Design', 'Fiction Writing', 'Film Studies', 'Finance', 'Financial Mathematics', 'Forensic Science', 'Forestry', 'Game Theory', 'Gender Studies', 'Genetics', 'Geology', 'Geometry', 'Graphic Design', 'HVAC (Heating, Ventilation, Air Conditioning)', 'History (General)', 'Hospitality & Tourism Management', 'Human Geography', 'Human Resource Management', 'Human-Computer Interaction', 'Interior Design', 'International Business', 'International Relations', 'Investment & Portfolio Management', 'Journalism', 'Linguistics', 'Literary Theory', 'Machine Learning', 'Marine Technology', 'Marketing', 'Materials Science', 'Mathematics', 'Mechatronics', 'Meteorology', 'Microbiology', 'Mobile App Development', 'Molecular Biology', 'Music Composition', 'Music Theory', 'Neuroscience', 'Number Theory', 'Nutrition Science', 'Oceanography', 'Operating Systems', 'Operations Research', 'Organic Chemistry', 'Painting', 'Peace & Conflict Studies', 'Pharmacology', 'Phonetics & Phonology', 'Photography', 'Physics', 'Plumbing', 'Poetry & Poetics', 'Political Science', 'Probability & Statistics', 'Programming', 'Project Management', 'Psychology', 'Public Policy', 'Rhetoric', 'Robotics', 'Science', 'Screenwriting', 'Sculpture', 'Second Language Acquisition', 'Semantics & Pragmatics', 'Social Work', 'Sociology', 'Software Engineering', 'Sound Design', 'Stage Design', 'Supply Chain Management', 'Technical Writing', 'Theater Arts', 'Thermodynamics', 'Topology', 'Translation & Interpretation', 'Trigonometry', 'Urban Studies', 'Voice & Diction', 'Web Development', 'Welding', 'World History', 'World Literature', 'Zoology']

    title = customtkinter.CTkLabel(subjSelect, text="Career Compass", fg_color="transparent", font=(font, 30))
    title.place(relx=0.5, rely=0.11775, anchor=customtkinter.CENTER)

    subjAnnounce = customtkinter.CTkLabel(subjSelect, text="Please select the subjects you like:", fg_color="transparent", font=(font, 20))
    subjAnnounce.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    subjSelection = customtkinter.CTkComboBox(subjSelect, values=subjs, width=235, state="readonly", font=(font, 14))
    subjSelection.set("Select a subject to add")
    subjSelection.place(relx=0.7, rely=0.2875, anchor=customtkinter.E)

    chosenSubjs = customtkinter.CTkTextbox(subjSelect, height=192.5, width=310, font=(font, 14))
    chosenSubjs.delete("0.0", "end")
    chosenSubjs.configure(state="disabled")
    chosenSubjs.place(relx=0.5, rely=0.575, anchor=customtkinter.CENTER)

    def addSubj():
        chosenSubjs.configure(state="normal")
        if subjSelection.get() != "Select a subject to add":
            chosenSubjs.insert("0.0", subjSelection.get()+"\n")
        chosenSubjs.configure(state="disabled")

    add = customtkinter.CTkButton(subjSelect, text="+", font=(font, 16), width=30, command=addSubj)
    add.place(relx=0.71, rely=0.2875, anchor=customtkinter.W)

    def rmvSubj():
        chosenSubjs.configure(state="normal")
        chosenSubjs.delete("1.0", "2.0")
        chosenSubjs.configure(state="disabled")

    rmv = customtkinter.CTkButton(subjSelect, text="-", font=(font, 16), width=30, command=rmvSubj)
    rmv.place(relx=0.8, rely=0.2875, anchor=customtkinter.W)

    def pageThreeCanon():
        chosenSubjects = chosenSubjs.get(0.0, "end").split("\n")
        del chosenSubjects[-2:]
        data["Interested Subjects"] = chosenSubjects
        subjSelect.destroy()

        markSheet = customtkinter.CTk()
        markSheet.geometry("400x410")
        markSheet.resizable(False, False)
        markSheet.title("Career Compass: Marks Entry")

        title = customtkinter.CTkLabel(markSheet, text="Career Compass", fg_color="transparent", font=(font, 30))
        title.place(relx=0.51, rely=0.11775, anchor=customtkinter.CENTER)

        markAnnounce0 = customtkinter.CTkLabel(markSheet, text="""Please enter your marks for""", fg_color="transparent", font=(font, 20))
        markAnnounce0.place(relx=0.51, rely=0.2, anchor=customtkinter.CENTER)

        markAnnounce1 = customtkinter.CTkLabel(markSheet, text="the following subjects:", fg_color="transparent", font=(font, 20))
        markAnnounce1.place(relx=0.51, rely=0.26, anchor=customtkinter.CENTER)


        mathematics = customtkinter.CTkLabel(markSheet, text="Mathematics", fg_color="transparent", font=(font, 17.5))
        mathematics.place(relx=0.075, rely=0.35, anchor=customtkinter.W)

        mathPercentage = customtkinter.CTkEntry(markSheet, width=40, justify=customtkinter.RIGHT)
        mathPercentage.place(relx=0.9, rely=0.35, anchor=customtkinter.E)


        phys = customtkinter.CTkLabel(markSheet, text="Physics", fg_color="transparent", font=(font, 17.5))
        phys.place(relx=0.075, rely=0.43, anchor=customtkinter.W)

        physPercentage = customtkinter.CTkEntry(markSheet, width=40, justify=customtkinter.RIGHT)
        physPercentage.place(relx=0.9, rely=0.43, anchor=customtkinter.E)


        chem = customtkinter.CTkLabel(markSheet, text="Chemistry", fg_color="transparent", font=(font, 17.5))
        chem.place(relx=0.075, rely=0.51, anchor=customtkinter.W)

        chemPercentage = customtkinter.CTkEntry(markSheet, width=40, justify=customtkinter.RIGHT)
        chemPercentage.place(relx=0.9, rely=0.51, anchor=customtkinter.E)


        bio = customtkinter.CTkLabel(markSheet, text="Biology", fg_color="transparent", font=(font, 17.5))
        bio.place(relx=0.075, rely=0.59, anchor=customtkinter.W)

        bioPercentage = customtkinter.CTkEntry(markSheet, width=40, justify=customtkinter.RIGHT)
        bioPercentage.place(relx=0.9, rely=0.59, anchor=customtkinter.E)


        sst = customtkinter.CTkLabel(markSheet, text="Social Science / Social Studies", fg_color="transparent", font=(font, 17.5))
        sst.place(relx=0.075, rely=0.67, anchor=customtkinter.W)

        sstPercentage = customtkinter.CTkEntry(markSheet, width=40, justify=customtkinter.RIGHT)
        sstPercentage.place(relx=0.9, rely=0.67, anchor=customtkinter.E)


        comp = customtkinter.CTkLabel(markSheet, text="Computers", fg_color="transparent", font=(font, 17.5))
        comp.place(relx=0.075, rely=0.75, anchor=customtkinter.W)

        compPercentage = customtkinter.CTkEntry(markSheet, width=40, justify=customtkinter.RIGHT)
        compPercentage.place(relx=0.9, rely=0.75, anchor=customtkinter.E)

        for i in range(35, 83, 8):
            rely = i/100
            customtkinter.CTkLabel(markSheet, text="%", fg_color="transparent", font=(font, 17.5)).place(relx=0.93, rely=rely, anchor=customtkinter.CENTER)

        def finalPage():
            try:
                if mathPercentage.get() != "":
                    mathMarks = float(mathPercentage.get())
                    markList.append(mathMarks)
                elif mathPercentage.get() == "":
                    mathMarks = -1000
                    markList.append("N")
                
                if physPercentage.get() != "":
                    physMarks = float(physPercentage.get())
                    markList.append(physMarks)
                elif physPercentage.get() == "":
                    physMarks = -1000
                    markList.append("N")
                        
                if chemPercentage.get() != "":
                    chemMarks = float(chemPercentage.get())
                    markList.append(chemMarks)
                elif chemPercentage.get() == "":
                    chemMarks = -1000
                    markList.append("N")
                        
                if bioPercentage.get() != "":
                    bioMarks = float(bioPercentage.get())
                    markList.append(bioMarks)
                elif bioPercentage.get() == "":
                    bioMarks = -1000
                    markList.append("N")
                        
                if sstPercentage.get() != "":
                    sstMarks = float(sstPercentage.get())
                    markList.append(sstMarks)
                elif sstPercentage.get() == "":
                    sstMarks = -1000
                    markList.append("N")
                        
                if compPercentage.get() != "":
                    compMarks = float(compPercentage.get())
                    markList.append(compMarks)
                elif compPercentage.get() == "":
                    compMarks = -1000
                    markList.append("N")
                

                if mathMarks > 100 or physMarks >100 or chemMarks >100 or bioMarks >100 or sstMarks >100 or compMarks >100:
                    messagebox.showerror("Error", "Please make sure all marks that have been entered in the percentage slot are equal or below 100%")
                    markList.clear()
                elif mathMarks <= 100 or physMarks <= 100 or chemMarks <= 100 or bioMarks <= 100 or sstMarks <= 100 or compMarks <= 100:
                    markSheet.destroy()
                    data["Marks"] = markList
                    
                    if len(data["Interested Subjects"]) == 0:
                        prompt = "I am not interested in any subject in particular.\n" 
                    elif len(data["Interested Subjects"]) > 0:
                        prompt = "I am interested in these subjects:\n" 
                        for i in range(len(data["Interested Subjects"])):
                            prompt = prompt+data["Interested Subjects"][i]+"\n"
                    
                    if data["Marks"][0] != "N" or data["Marks"][1] != "N" or data["Marks"][2] != "N" or data["Marks"][3] != "N" or data["Marks"][4] != "N" or data["Marks"][5] != "N":
                        prompt = prompt+"\nMy marks percentage are:\n"

                        subjList = ["Mathematics: ", "Physics: ", "Chemistry: ", "Biology: ", "Social Studies/Social Science: ", "Computers: "]
                        for i in range(6):
                            if data["Marks"][i] != "N":
                                prompt = prompt+subjList[i]+str(markList[i])+"%\n"
                    prompt = prompt+"\nPlease suggest 10 suitable jobs for me. I require no other information, just a plain list of jobs, nothing else. The list must not be numbered, nor bullet pointed. It must be simple text, in a simple list, only 10 jobs."
                    messagebox.showinfo("Processing...", "Processing information. Please wait.")                    
                    response = model.generate_content(prompt)

                    jobsTxt = response.text
                    jobsList = jobsTxt.split("\n") 

                    job = customtkinter.CTk()
                    job.geometry("390x760")
                    job.title("Career Compass")
                    job.resizable(False, False)

                    title = customtkinter.CTkLabel(job, text="Career Compass", fg_color="transparent", font=(font, 40))
                    title.place(relx=0.5, rely=0.075, anchor=customtkinter.CENTER)

                    caption = customtkinter.CTkLabel(job, text="Here are 10 jobs we think are best for you:", fg_color="transparent", font=(font, 18))
                    caption.place(relx=0.5, rely=0.12, anchor=customtkinter.CENTER)

                    job1 = customtkinter.CTkButton(job, text=jobsList[0], font=(font, 14), height=50, width=225)
                    job1.place(relx=0.5, rely=0.035+0.15, anchor=customtkinter.CENTER)

                    job2 = customtkinter.CTkButton(job, text=jobsList[1], font=(font, 14), height=50, width=225)
                    job2.place(relx=0.5, rely=0.035+0.23, anchor=customtkinter.CENTER)

                    job3 = customtkinter.CTkButton(job, text=jobsList[2], font=(font, 14), height=50, width=225)
                    job3.place(relx=0.5, rely=0.035+0.31, anchor=customtkinter.CENTER)

                    job4 = customtkinter.CTkButton(job, text=jobsList[3], font=(font, 14), height=50, width=225)
                    job4.place(relx=0.5, rely=0.035+0.39, anchor=customtkinter.CENTER)

                    job5 = customtkinter.CTkButton(job, text=jobsList[4], font=(font, 14), height=50, width=225)
                    job5.place(relx=0.5, rely=0.035+0.47, anchor=customtkinter.CENTER)

                    job6 = customtkinter.CTkButton(job, text=jobsList[5], font=(font, 14), height=50, width=225)
                    job6.place(relx=0.5, rely=0.035+0.55, anchor=customtkinter.CENTER)

                    job7 = customtkinter.CTkButton(job, text=jobsList[6], font=(font, 14), height=50, width=225)
                    job7.place(relx=0.5, rely=0.035+0.63, anchor=customtkinter.CENTER)

                    job8 = customtkinter.CTkButton(job, text=jobsList[7], font=(font, 14), height=50, width=225)
                    job8.place(relx=0.5, rely=0.035+0.71, anchor=customtkinter.CENTER)

                    job9 = customtkinter.CTkButton(job, text=jobsList[8], font=(font, 14), height=50, width=225)
                    job9.place(relx=0.5, rely=0.035+0.79, anchor=customtkinter.CENTER)

                    job10 = customtkinter.CTkButton(job, text=jobsList[9], font=(font, 14), height=50, width=225)
                    job10.place(relx=0.5, rely=0.035+0.87, anchor=customtkinter.CENTER)



                    job.mainloop()
                    

            except ValueError:
                messagebox.showerror("Error", 'Please make sure only numbers have been entered in the percentage slot. If you have typed "%", please remove it.')
                markList.clear()

        pageThree = customtkinter.CTkButton(markSheet, text="Continue ⏭️", font=(font, 18), width=350, command=finalPage)
        pageThree.place(relx=0.51, rely=0.85, anchor=customtkinter.CENTER)

        subjAnnounce = customtkinter.CTkLabel(markSheet, text="Leave the entryblank if inapplicable", fg_color="transparent", font=(font, 15))
        subjAnnounce.place(relx=0.96, rely=0.95, anchor=customtkinter.E)

        markSheet.mainloop()    

    pageThree = customtkinter.CTkButton(subjSelect, text="Continue ⏭️", font=(font, 18), width=310, command=pageThreeCanon)
    pageThree.place(relx=0.5, rely=0.87, anchor=customtkinter.CENTER)

    subjSelect.mainloop()
    
pageTwo = customtkinter.CTkButton(welcome, text="Find your dream job!", command=pageTwoCanon, font=(font, 14))
pageTwo.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

welcome.mainloop()