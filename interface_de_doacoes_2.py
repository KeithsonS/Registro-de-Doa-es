import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Funções para adicionar e remover entradas
def add_donation():
    donor_name = entry_donor_name.get()
    donation_amount = entry_donation_amount.get()
    if donor_name and donation_amount:
        listbox_donations.insert(tk.END, f"{donor_name} - R${donation_amount}")
        entry_donor_name.delete(0, tk.END)
        entry_donation_amount.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both donor name and donation amount.")

def add_beneficiary():
    beneficiary_name = entry_beneficiary_name.get()
    beneficiary_info = entry_beneficiary_info.get()
    if beneficiary_name and beneficiary_info:
        listbox_beneficiaries.insert(tk.END, f"{beneficiary_name} - {beneficiary_info}")
        entry_beneficiary_name.delete(0, tk.END)
        entry_beneficiary_info.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both beneficiary name and information.")

def add_project():
    project_name = entry_project_name.get()
    project_status = entry_project_status.get()
    if project_name and project_status:
        listbox_projects.insert(tk.END, f"{project_name} - {project_status}")
        entry_project_name.delete(0, tk.END)
        entry_project_status.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both project name and status.")

def remove_selection(listbox):
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
    else:
        messagebox.showwarning("Selection Error", "Please select an item to remove.")

# Criação da janela principal
root = tk.Tk()
root.title("Gerenciador de Doações, Beneficiários e Projetos")

# Configuração do estilo
style = ttk.Style()
style.configure('TNotebook', background='#ADD8E6')
style.configure('TFrame', background='#ADD8E6')
style.configure('TButton', background='#87CEFA', padding=5)
style.configure('TLabel', background='#ADD8E6')
style.configure('TEntry', padding=5)

# Criação do notebook para abas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Aba de Doações
tab_donations = ttk.Frame(notebook)
notebook.add(tab_donations, text='Doações')

frame_donations_form = ttk.Frame(tab_donations)
frame_donations_form.pack(padx=10, pady=10, fill='x')

label_donor_name = ttk.Label(frame_donations_form, text="Nome do Doador:")
label_donor_name.grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_donor_name = ttk.Entry(frame_donations_form)
entry_donor_name.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

label_donation_amount = ttk.Label(frame_donations_form, text="Valor da Doação:")
label_donation_amount.grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_donation_amount = ttk.Entry(frame_donations_form)
entry_donation_amount.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

button_add_donation = ttk.Button(frame_donations_form, text="Adicionar Doação", command=add_donation)
button_add_donation.grid(row=2, column=0, columnspan=2, pady=10)

listbox_donations = tk.Listbox(tab_donations, width=60, height=10, bg='#f0f8ff')
scrollbar_donations = tk.Scrollbar(tab_donations, orient=tk.VERTICAL, command=listbox_donations.yview)
listbox_donations.config(yscrollcommand=scrollbar_donations.set)
listbox_donations.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)
scrollbar_donations.pack(side=tk.RIGHT, fill=tk.Y)

button_remove_donation = ttk.Button(tab_donations, text="Remover Seleção", command=lambda: remove_selection(listbox_donations))
button_remove_donation.pack(pady=5)

# Aba de Beneficiários
tab_beneficiaries = ttk.Frame(notebook)
notebook.add(tab_beneficiaries, text='Beneficiários')

frame_beneficiaries_form = ttk.Frame(tab_beneficiaries)
frame_beneficiaries_form.pack(padx=10, pady=10, fill='x')

label_beneficiary_name = ttk.Label(frame_beneficiaries_form, text="Nome do Beneficiário:")
label_beneficiary_name.grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_beneficiary_name = ttk.Entry(frame_beneficiaries_form)
entry_beneficiary_name.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

label_beneficiary_info = ttk.Label(frame_beneficiaries_form, text="Informações do Beneficiário:")
label_beneficiary_info.grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_beneficiary_info = ttk.Entry(frame_beneficiaries_form)
entry_beneficiary_info.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

button_add_beneficiary = ttk.Button(frame_beneficiaries_form, text="Adicionar Beneficiário", command=add_beneficiary)
button_add_beneficiary.grid(row=2, column=0, columnspan=2, pady=10)

listbox_beneficiaries = tk.Listbox(tab_beneficiaries, width=60, height=10, bg='#f0f8ff')
scrollbar_beneficiaries = tk.Scrollbar(tab_beneficiaries, orient=tk.VERTICAL, command=listbox_beneficiaries.yview)
listbox_beneficiaries.config(yscrollcommand=scrollbar_beneficiaries.set)
listbox_beneficiaries.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)
scrollbar_beneficiaries.pack(side=tk.RIGHT, fill=tk.Y)

button_remove_beneficiary = ttk.Button(tab_beneficiaries, text="Remover Seleção", command=lambda: remove_selection(listbox_beneficiaries))
button_remove_beneficiary.pack(pady=5)

# Aba de Projetos
tab_projects = ttk.Frame(notebook)
notebook.add(tab_projects, text='Projetos')

frame_projects_form = ttk.Frame(tab_projects)
frame_projects_form.pack(padx=10, pady=10, fill='x')

label_project_name = ttk.Label(frame_projects_form, text="Nome do Projeto:")
label_project_name.grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_project_name = ttk.Entry(frame_projects_form)
entry_project_name.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

label_project_status = ttk.Label(frame_projects_form, text="Status do Projeto:")
label_project_status.grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_project_status = ttk.Entry(frame_projects_form)
entry_project_status.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

button_add_project = ttk.Button(frame_projects_form, text="Adicionar Projeto", command=add_project)
button_add_project.grid(row=2, column=0, columnspan=2, pady=10)

listbox_projects = tk.Listbox(tab_projects, width=60, height=10, bg='#f0f8ff')
scrollbar_projects = tk.Scrollbar(tab_projects, orient=tk.VERTICAL, command=listbox_projects.yview)
listbox_projects.config(yscrollcommand=scrollbar_projects.set)
listbox_projects.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)
scrollbar_projects.pack(side=tk.RIGHT, fill=tk.Y)

button_remove_project = ttk.Button(tab_projects, text="Remover Seleção", command=lambda: remove_selection(listbox_projects))
button_remove_project.pack(pady=5)

# Inicia o loop principal da interface gráfica
root.mainloop()
