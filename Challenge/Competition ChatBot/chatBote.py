from tkinter import *
root=Tk()
root.geometry('750x400')
root.title("ChatBot d'orientation")
Message = Label(root,text='''Bienvenue sur notre chatbot d orientation ! Pour commencer,
veuillez répondre aux questions suivantes pour nous aider à mieux comprendre vos intérêts, 
vos compétences et vos motivations. 
Nous utiliserons ces informations pour vous suggérer des options de carrière qui correspondent à votre personnalité.
Nous vous remercions d avance pour votre participation !''')
Message.pack()

resulta = {
    "Développement digital" : 0,
    "Infrastructure digital" : 0,
    "Marketing digital" : 0,
    "Design" : 0
}

def question_1():

    for ele in root.winfo_children():
        ele.destroy()
    Noml =Label(root,text="Question 1 : Quel est votre nom complet ?")
    Nom_Entry=Entry(root)
    Noml.pack()
    Nom_Entry.pack()
    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_2(Nom_Entry))
    Next.pack()
Next=Button(root,text="Next",bg='blue',fg='white',command=question_1)
Next.pack()


def question_2(prev_answer):
    
    for ele in root.winfo_children():
        ele.destroy()
    question2=Label(root,text="Question 2 : Quels sont les sujets qui vous passionnent?")
    q2v=StringVar()

    q2_art=Radiobutton(root,text="Art",variable=q2v,value="Art")
    q2_tachnologie=Radiobutton(root,text="Technologie",variable=q2v,value="technologie")
    q2_buisness=Radiobutton(root,text="Buisness",variable=q2v,value="Buisness")
    q2_ingenierie=Radiobutton(root,text="Ingenierie",variable=q2v,value="Ingenierie")
    q2_science=Radiobutton(root,text="Science",variable=q2v,value="Science")
    question2.pack()
    q2v=StringVar()
    q2_art=Radiobutton(root,text="Art",variable=q2v,value="Art")
    q2_tachnologie=Radiobutton(root,text="Technologie",variable=q2v,value="technologie")
    q2_buisness=Radiobutton(root,text="Buisness",variable=q2v,value="Buisness")
    q2_ingenierie=Radiobutton(root,text="Ingenierie",variable=q2v,value="Ingenierie")
    q2_science=Radiobutton(root,text="Science",variable=q2v,value="Science")
    q2_art.pack()
    q2_tachnologie.pack()
    q2_buisness.pack()
    q2_ingenierie.pack()
    q2_science.pack()
    q2v.set("none")
    
    list_answers ={ "Art":"Design",
                    "technologie":"Développement digital",
                    "Buisness":"Marketing digital",
                    "Ingenierie":"Infrastructure digital",
                    "Science":''
                }
    
    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_3(list_answers[q2v.get()]))
    Next.pack()


def question_3(prev_answer):
    
    for ele in root.winfo_children():
        ele.destroy()

    global resulta    
    if prev_answer != '':
        resulta[prev_answer] += 1

    print(resulta)    

    question = Label(root, text="Quetion 3 : Quels sont les types d'activités que vous préférez? (plusieurs réponses possibles)")
    question.pack()

    list_v = []
    for i in range(9):
        list_v.append(IntVar())

    repnse1 = Checkbutton(root, text="Travailler en équipe", variable=list_v[0]).pack()
    repnse2 = Checkbutton(root, text="Travailler seul", variable=list_v[1]).pack()
    repnse3 = Checkbutton(root, text="Résoudre des problèmes", variable=list_v[2]).pack()
    repnse4 = Checkbutton(root, text="Apprendre des nouvelles choses", variable=list_v[3]).pack()
    repnse5 = Checkbutton(root, text="Analyse", variable=list_v[4]).pack()
    repnse6 = Checkbutton(root, text="Création", variable=list_v[5]).pack()
    repnse7 = Checkbutton(root, text="Prise de décision", variable=list_v[6]).pack()
    repnse8 = Checkbutton(root, text="Voyage", variable=list_v[7]).pack()
    repnse9 = Checkbutton(root, text="Lecture", variable=list_v[8]).pack()
    
    list_answers ={ "Travailler en équipe":["Développement digital", "Infrastructure digital", "Marketing digital", "Design"],
                    "Travailler seul":["Développement digital", "Design"],
                    "Résoudre des problèmes":["Développement digital"],
                    "Apprendre des nouvelles choses":["Développement digital", "Marketing digital", "Design"],
                    "Analyse":["Développement digital", "Infrastructure digital"],
                    "Création":["Design"],
                    "Prise de décision":["Marketing digital"],
                    "Voyage":["Infrastructure digital"],
                    "Lecture]":["Développement digital", "Infrastructure digital", "Marketing digital", "Design"]
                }

    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_4(list_answers, list_v))
    Next.pack()


def question_4(lst_answer, prev_answer):
    for ele in root.winfo_children():
        ele.destroy()
    global resulta
    for i, v in enumerate(prev_answer):
        if v.get() == 1:
            for filier in lst_answer[list(lst_answer.keys())[i]]:
                resulta[filier] += 1
    print(resulta)            

    Q4_var = StringVar()
    question = Label(root, text="Question 4 : Quel est votre rêve de carrière?").pack()
    reponse1 = Radiobutton(root, value="Entrepreneur", text="Entrepreneur", variable=Q4_var).pack()
    reponse2 = Radiobutton(root, value="Ingénieur",  text="Ingénieur", variable=Q4_var).pack()
    reponse3 = Radiobutton(root, value="Infographiste",  text="Infographiste", variable=Q4_var).pack()
    reponse4 = Radiobutton(root, value="Enseignant",  text="Enseignant", variable=Q4_var).pack()
    reponse5 = Radiobutton(root, value="Marqueteur",  text="Marqueteur", variable=Q4_var).pack()
    reponse6 = Radiobutton(root, value="Freelancer",  text="Freelancer", variable=Q4_var).pack()
    Q4_var.set("none")

    list_answers = {"Entrepreneur": ["Développement digital"],
                    "Ingénieur": ["Développement digital", "Infrastructure digital", "Marketing digital"],
                    "Infographiste": ["Design"], 
                    "Enseignant": ["Infrastructure digital"],
                    "Marqueteur": ["Marketing digital"],
                    "Freelancer": ["Développement digital", "Marketing digital", "Design"]
                }
    
    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_5(list_answers, Q4_var.get()))
    Next.pack()

def question_5(lst_answers, prev_answer):
    for ele in root.winfo_children():
        ele.destroy()
    global resulta
    for filier in lst_answers[prev_answer]:
        resulta[filier] += 1

    question5=Label(root, text="Quetion 5 : Qu'est-ce qui vous motiverait dans un emploi? (plusieurs réponses possibles")
    question5.pack()

    list_v = []
    for i in range(6):
        list_v.append(IntVar())

    repnse1=Checkbutton(root, text="Des opportunités de développement personnel et professionnel",variable=list_v[0]).pack()
    repnse2=Checkbutton(root, text="La possibilité de prendre des décisions et d'avoir de l'autonomie",variable=list_v[1]).pack()
    repnse3=Checkbutton(root, text="La possibilité de travailler sur des projets innovants",variable=list_v[2]).pack()
    repnse4=Checkbutton(root, text="La possibilité de travailler avec des technologies de pointe",variable=list_v[3]).pack()
    repnse5=Checkbutton(root, text="La possibilité de travailler dans un environnement international",variable=list_v[4]).pack()
    repnse6=Checkbutton(root, text="La possibilité de voyager",variable=list_v[5]).pack()


    list_answers ={ "Des opportunités de développement personnel et professionnel":["Marketing digital", "Design"],
                    "La possibilité de prendre des décisions et d'avoir de l'autonomie":["Design"],
                    "La possibilité de travailler sur des projets innovants":["Développement digital"],
                    "La possibilité de travailler avec des technologies de pointe":["Développement digital"],
                    "La possibilité de travailler dans un environnement international":["Développement digital", "Design"],
                    "La possibilité de voyager":["Infrastructure digital"]
                }
    

    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_6(list_answers, list_v))
    Next.pack()

def question_6(lst_answer, prev_answer):
    for ele in root.winfo_children():
        ele.destroy()

    global resulta
    for i, v in enumerate(prev_answer):
        if v.get() == 1:
            for filier in lst_answer[list(lst_answer.keys())[i]]:
                resulta[filier] += 1


    question6=Label(root,text="Question 6 : Quel type d'environnement de travail préférez-vous?")
    question6.pack()
    q6v=StringVar()
    Bureau=Radiobutton(root,text="Bureau",variable=q6v,value="Bureau")
    Open_space=Radiobutton(root,text="Open-Space",variable=q6v,value="Open-Space")
    Travalad=Radiobutton(root,text="Travail a distance",variable=q6v,value="Travail a distance")
    Travailst=Radiobutton(root,text="Travail sur terrain",variable=q6v,value="Travail sur terrain")
    Bureau.pack()
    Open_space.pack()
    Travalad.pack()
    Travailst.pack()
    q6v.set("none")

    list_answers ={ "Bureau":["Développement digital", "Marketing digital"],
                    "Open-Space":["Design"],
                    "Travail a distance":["Développement digital", "Marketing digital", "Design"],
                    "Travail sur terrain":["Infrastructure digital"],
                }
    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_7(list_answers, q6v.get()))
    Next.pack()

def question_7(lst_answer, prev_answer):
    for ele in root.winfo_children():
        ele.destroy()

    global resulta
    for filier in lst_answer[prev_answer]:
        resulta[filier] += 1

    question = Label(root, text="Quetion 7 : Quelles sont vos principales aptitudes? (plusieurs réponses possibles)")
    question.pack()

    list_v = []
    for i in range(8):
        list_v.append(IntVar())

    repnse1 = Checkbutton(root, text="Esprit de logique", variable=list_v[0]).pack()
    repnse2 = Checkbutton(root, text="Esprit d'équipe", variable=list_v[1]).pack()
    repnse3 = Checkbutton(root, text="Esprit de management", variable=list_v[2]).pack()
    repnse4 = Checkbutton(root, text="Communication", variable=list_v[3]).pack()
    repnse5 = Checkbutton(root, text="Curiosité, l'envie de s'auto-former", variable=list_v[4]).pack()
    repnse6 = Checkbutton(root, text="Esprit d'analyse", variable=list_v[5]).pack()
    repnse7 = Checkbutton(root, text="Esprit de marketing", variable=list_v[6]).pack()
    repnse8 = Checkbutton(root, text="Esprit de création", variable=list_v[7]).pack()

    list_answers ={ "Esprit de logique":["Développement digital", "Design"],
                    "Esprit d'équipe":["Développement digital", "Infrastructure digital"],
                    "Esprit de management":["Infrastructure digital"],
                    "Communication":["Développement digital", "Marketing digital", "Design"],
                    "Curiosité, l'envie de s'auto-former":["Développement digital", "Design"],
                    "Esprit d'analyse":["Infrastructure digital"],
                    "Esprit de marketing":["Marketing digital"],
                    "Esprit de création":["Design"],
                }
    
    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_8(list_answers, list_v))
    Next.pack()

def question_8(lst_answer, prev_answer):
    for ele in root.winfo_children():
        ele.destroy()

    global resulta
    for i, v in enumerate(prev_answer):
        if v.get() == 1:
            for filier in lst_answer[list(lst_answer.keys())[i]]:
                resulta[filier] += 1
    
    question = Label(root, text="Quetion 8 : Quels sont les types de problèmes que vous aimez résoudre? (plusieurs réponses possibles)")
    question.pack()

    list_v = []
    for i in range(5):
        list_v.append(IntVar())

    repnse1 = Checkbutton(root, text="Problèmes techniques", variable=list_v[0]).pack()
    repnse2 = Checkbutton(root, text="Problèmes de recherche", variable=list_v[1]).pack()
    repnse3 = Checkbutton(root, text="Problèmes commerciaux", variable=list_v[2]).pack()
    repnse4 = Checkbutton(root, text="Problèmes de gestion", variable=list_v[3]).pack()
    repnse5 = Checkbutton(root, text="Problèmes créatifs", variable=list_v[4]).pack()

    list_answers ={ "Problèmes techniques":["Développement digital", "Infrastructure digital"],
                    "Problèmes de recherche":["Développement digital"],
                    "Problèmes commerciaux":["Marketing digital"],
                    "Problèmes de gestion":["Infrastructure digital", "Marketing digital"],
                    "Problèmes créatifs":["Design"],
                }

    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_9(list_answers, list_v))
    Next.pack()


def question_9(lst_answer, prev_answer):
    for ele in root.winfo_children():
        ele.destroy()

    global resulta
    for i, v in enumerate(prev_answer):
        if v.get() == 1:
            for filier in lst_answer[list(lst_answer.keys())[i]]:
                resulta[filier] += 1


    Q9_var = StringVar()
    question = Label(root, text="Question 9 : Est-ce que vous utilisez déjà des logiciels pour la manipulation d'images ou de vidéos ?").pack()
    reponse1 = Radiobutton(root, value="oui", text="oui", variable=Q9_var).pack()
    reponse2 = Radiobutton(root, value="non", text="non", variable=Q9_var).pack()
    Q9_var.set("none")

    list_answers = {"oui": "Design",
                    "non" : ''
                    }
    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_10(list_answers,Q9_var.get()))
    Next.pack()

def question_10(lst_answer, prev_answer):
    for ele in root.winfo_children():
        ele.destroy()
    global resulta
    if prev_answer != 'non':
        resulta[lst_answer[prev_answer]] += 1

    Q10_var = StringVar()
    question = Label(root, text="Question 10 : Avez-vous déjà des notions sur la programmation ?").pack()
    reponse1 = Radiobutton(root, value="oui", text="oui", variable=Q10_var).pack()
    reponse2 = Radiobutton(root, value="non", text="non", variable=Q10_var).pack()
    Q10_var.set("none")

    list_answers = {"oui": "Développement digital",
                    "non" : ''
                    }
    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_11(list_answers,Q10_var.get()))
    Next.pack()


def question_11(lst_answer,prev_answer):
    for ele in root.winfo_children():
        ele.destroy()

    global resulta
    if prev_answer != 'non':
        resulta[lst_answer[prev_answer]] += 1    

    question11=Label(root,text="Quetion 11 : Est-ce que vous connaissez tous les réseaux sociaux et les utilisez-vous ?")
    question11.pack()
    q11v=StringVar()
    oui=Radiobutton(root,text="oui",variable=q11v,value="Oui")
    oui.pack()
    non=Radiobutton(root,text="Non",variable=q11v,value="Non")
    non.pack()
    q11v.set('none')
    
    list_answers ={ "Oui":"Marketing digital",
                    "Non":''
                }
    Next=Button(root,text="Next",bg='blue',fg='white',command=lambda : question_12(list_answers, q11v.get()))
    Next.pack()

def question_12(lst_answer ,prev_answer):
    for ele in root.winfo_children():
        ele.destroy()

    global resulta
    if prev_answer != 'Non':
        resulta[lst_answer[prev_answer]] += 1

    question12=Label(root,text="Quetion 12 : Est-ce que vous avez une idée sur l'infrastructure numérique ?")
    question12.pack()
    q12v=StringVar()
    Oui=Radiobutton(root,text="oui",variable=q12v,value="Oui")
    Oui.pack()
    Non=Radiobutton(root,text="Non",variable=q12v,value="Non")
    Non.pack()
    q12v.set('none')

    list_answers ={ "Oui":"Infrastructure digital",
                    "Non":''
                }
    Next=Button(root,text="Submit",bg='blue',fg='white',command=lambda : Submit(list_answers, q12v.get()))
    Next.pack()

def Submit(lst_answer, prev_answer):
    for ele in root.winfo_children():
        ele.destroy()

    global resulta
    if prev_answer != 'Non':
        resulta[lst_answer[prev_answer]] += 1

    resulta_final = 'Développement digital'
    maximum = resulta["Développement digital"]
    for filier in resulta:
        if resulta[filier] > maximum:
            resulta_final = filier    
        
    message = f'''Merci d'avoir utilisé notre chatbot d'orientation ! 
En fonction de vos réponses, nous avons identifié l'option de carrière suivante qui correspond à vos intérêts,
vos compétences et vos motivations : {resulta_final}. Nous vous encourageons à explorer cette option pour en savoir plus sur elle,
et à consulter des professionnels pour obtenir des conseils sur la façon de poursuivre cette carrière.
Nous espérons que cette expérience vous a été utile et vous a aidé à explorer de nouvelles idées pour votre avenir professionnel.   
'''
    l = Label(root, text=message).pack()

root.mainloop()
