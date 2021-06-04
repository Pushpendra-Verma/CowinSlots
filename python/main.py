from tkinter.font import BOLD
from requests import *
from tkinter import *


def session():
    pincode = pinValue.get()
    date = dateValue.get()

    data = get(
        f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}")
    
    dataJson = data.json()
    counter = 4
    for value in range(len(dataJson['sessions'])):
        with open('data.txt', 'a') as f:
            f.write('Name' + "--" +
                    str(dataJson['sessions'][value]['name'])+'\n')
            f.write(
                'Dose1' + "--"+str(dataJson['sessions'][value]['available_capacity_dose1'])+'\n')
            f.write(
                'Dose2' + "--" + str(dataJson['sessions'][value]['available_capacity_dose2'])+'\n')
            f.write('Min Age' + "--" +
                    str(dataJson['sessions'][value]['min_age_limit'])+'\n')
            f.write('Vaccine' + "--" +
                    str(dataJson['sessions'][value]['vaccine'])+'\n')
            f.write('Slots' + "--" +
                    str(dataJson['sessions'][value]['slots'])+'\n')
            f.write('\n\n')

        col = value//4
        if counter % 28 == 0:
            counter = 4
        if (dataJson['sessions'][value]['available_capacity_dose1'] > 0 and dataJson['sessions'][value]['min_age_limit'] >= 45):
            Label(root, text=f"Location: {dataJson['sessions'][value]['name']}", fg='blue').grid(
                row=counter+1, column=col, sticky='w')
            Label(root, text=f"Dose 1: {dataJson['sessions'][value]['available_capacity_dose1']}", fg='white', bg='green').grid(
                row=counter+2, column=col, sticky='w')
            Label(root, text=f"Dose 2: {dataJson['sessions'][value]['available_capacity_dose2']}", fg='green').grid(
                row=counter+3, column=col, sticky='w')
            Label(root, text=f"Min. Age: {dataJson['sessions'][value]['min_age_limit']}", fg='red').grid(
                row=counter+4, column=col, sticky='w')
            Label(root, text=f"Vaccine: {dataJson['sessions'][value]['vaccine']}").grid(
                row=counter+5, column=col, sticky='w')
            Label(root, text='--------------------------------').grid(row=counter +
                                                                      6, column=col, sticky='w')
            counter = counter + 6
        elif (dataJson['sessions'][value]['available_capacity_dose1'] > 0 and dataJson['sessions'][value]['min_age_limit'] < 45):
            Label(root, text=f"Location: {dataJson['sessions'][value]['name']}", fg='blue').grid(
                row=counter+1, column=col, sticky='w')
            Label(root, text=f"Dose 1: {dataJson['sessions'][value]['available_capacity_dose1']}", fg='white', bg='yellow').grid(
                row=counter+2, column=col, sticky='w')
            Label(root, text=f"Dose 2: {dataJson['sessions'][value]['available_capacity_dose2']}", fg='green').grid(
                row=counter+3, column=col, sticky='w')
            Label(root, text=f"Min. Age: {dataJson['sessions'][value]['min_age_limit']}", fg='red').grid(
                row=counter+4, column=col, sticky='w')
            Label(root, text=f"Vaccine: {dataJson['sessions'][value]['vaccine']}").grid(
                row=counter+5, column=col, sticky='w')
            Label(root, text='--------------------------------').grid(row=counter +
                                                                      6, column=col, sticky='w')
            counter = counter + 6
        else:
            Label(root, text=f"Location: {dataJson['sessions'][value]['name']}", fg='blue').grid(
                row=counter+1, column=col, sticky='w')
            Label(root, text=f"Dose 1: {dataJson['sessions'][value]['available_capacity_dose1']}", fg='green').grid(
                row=counter+2, column=col, sticky='w')
            Label(root, text=f"Dose 2: {dataJson['sessions'][value]['available_capacity_dose2']}", fg='green').grid(
                row=counter+3, column=col, sticky='w')
            Label(root, text=f"Min. Age: {dataJson['sessions'][value]['min_age_limit']}", fg='red').grid(
                row=counter+4, column=col, sticky='w')
            Label(root, text=f"Vaccine: {dataJson['sessions'][value]['vaccine']}").grid(
                row=counter+5, column=col, sticky='w')
            Label(root, text='--------------------------------').grid(row=counter +
                                                                      6, column=col, sticky='w')
            counter = counter + 6


root = Tk()
root.geometry('1366x768')
root.title('Covid Slots')
Label(root, text='Covid Vaccine Slots Availability', font=[
      'Georgia', 24, BOLD], fg='blue').grid(row=0, columnspan=3)
pic = PhotoImage(file='assets/image.png')
Label(root, image=pic).grid(row=0, column=4)
Label(root, text='Enter Pincode', font=['Georgia', 12, BOLD]).grid(
    row=2, column=0, sticky='w')
Label(root, text='Enter Date(dd-mm-yyyy)',
      font=['Georgia', 12, BOLD]).grid(row=3, column=0, sticky='w')

pinValue = StringVar()
dateValue = StringVar()

Entry(root, textvariable=pinValue).grid(row=2, column=1)
Entry(root, textvariable=dateValue).grid(row=3, column=1)

Button(root, text='Check', command=session, fg='green',
       font=['Georgia', 12, BOLD]).grid(row=4, column=1)

root.mainloop()
