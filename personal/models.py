from __future__ import unicode_literals
from django.db import models



class Employee(models.Model):
    SELECT = ''
    MALE = 'Male'
    FEMALE = 'Female'
    gend = (
        (SELECT, ''),
        (MALE,'Male'),
        (FEMALE,'Female'),
    )
    SELECT = ''
    MARRIED = 'Married'
    SINGLE = 'Single'
    DIVORCEE = 'Divorcee'
    marr = (
        (SELECT, ''),
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
        (DIVORCEE, 'Divorcee')
    )
    #Employee_id = models.AutoField(primary_key=True, help_text='Enter Employees ID')
    Employee_id=models.IntegerField(primary_key=True,help_text='Enter Employees ID')
    Employee_name=models.CharField(max_length=50,help_text='Enter Employees Name')
    Fathers_name=models.CharField(max_length=50,help_text='Enter Fathers Name')
    Date_Of_Birth=models.DateField(auto_now=False,auto_now_add=False,help_text='Enter Employees Date of Birth')
    Gender=models.CharField(max_length=50,choices=gend,help_text='Choose Employees Gender')
    Present_Address=models.TextField(help_text='Enter Employees Present Address')
    Permanent_Address=models.TextField(help_text='Enter Employees Permanent Address')
    Residential_Contact_No=models.IntegerField(help_text='Enter Employees Residential Contact No.')
    Permanent_Contact_No=models.IntegerField(help_text='Enter Employees Permanent Contact No.')
    Email_id=models.EmailField(max_length=50,null=True,help_text='Enter Employees Email Id')
    Marital_Status=models.CharField(max_length=50,choices=marr,help_text='Choose Employees Marital Status')
    Marriage_Date=models.CharField(max_length=50,help_text='Enter Employees Marriage Date')

    def __unicode__(self):
        return self.Employee_name

class family(models.Model):
    SELECT = ''
    MALE = 'Male'
    FEMALE = 'Female'
    gend = (
        (SELECT, ''),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    Employee_id=models.ForeignKey(Employee, on_delete=models.CASCADE,help_text='Choose for which employee you want to enter details')
    Name=models.CharField(max_length=50,help_text='Enter name.')
    Date_of_Birth=models.DateField(auto_now=False,auto_now_add=False,help_text='Enter Date Of Birth')
    Gender=models.CharField(max_length=50,choices=gend,help_text='Enter the gender.')
    Relationship=models.CharField(max_length=50,help_text='Enter the relationship.')
    Occupation=models.CharField(max_length=50,help_text='Enter occupation.')

    def __unicode__(self):
        return self.Name


class med(models.Model):
    SELECT = ''
    A_positive = 'A+'
    A_negative = 'A-'
    B_positive='B+'
    B_negative ='B-'
    AB_positive ='AB+'
    AB_negative='AB-'
    O_positive='O+'
    O_negative='O-'
    group = (
        (A_positive , 'A+'),
        (A_negative , 'A-'),
        (B_positive , 'B+'),
        (B_negative , 'B-'),
        (AB_positive , 'AB+'),
        (AB_negative , 'AB-'),
        (O_positive , 'O+'),
        (O_negative , 'O-'),
    )
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE,help_text='Choose for which employee you want to enter details')
    Blood_group=models.CharField(max_length=50,choices=group,help_text='Enter the Blood Group')
    Ailments=models.CharField(max_length=50,help_text='Enter Ailments(Heart condition,BP etc.) if any')
    Allergies=models.CharField(max_length=50,help_text='Enter the allergies(Drug, etc.) if any')

    def __unicode__(self):
        return self.Blood_group

class emergency(models.Model):
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE,help_text='Choose for which employee you want to enter details')
    Contact_person_name=models.CharField(max_length=50,help_text='Enter name')
    Relation=models.CharField(max_length=50,help_text='Enter the relation')
    Landline_No=models.IntegerField(help_text='Enter Landline number')
    Mobile_No=models.IntegerField(help_text='Enter Mobile number')

    def __unicode__(self):
        return self.Contact_person_name

class education(models.Model):
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE,help_text='Choose for which employee you want to enter details')
    Degree=models.CharField(max_length=50,help_text='Enter the Degree/Doploma/Certificate')
    Institute=models.CharField(max_length=50,help_text='Enter the Institute/University')
    From=models.DateField(auto_now=False,auto_now_add=False,help_text='Enter the starting date of your degree')
    To = models.DateField(auto_now=False, auto_now_add=False, help_text='Enter the ending date of your degree')
    Percentage = models.IntegerField(help_text='Enter the final Percentage(%)')

    def __unicode__(self):
        return self.Degree

class employment(models.Model):
    SELECT = ''
    ACTIVE = 'Active'
    LEFT = 'Left'
    status = (
        (SELECT, ''),
        (ACTIVE, 'Active'),
        (LEFT, 'Left'),
    )
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE,help_text='Choose for which employee you want to enter details')
    Date_of_Joining = models.DateField(auto_now=False,auto_now_add=False,help_text='Enter date of joining')
    Date_of_Resigning = models.DateField(auto_now=False,auto_now_add=False,help_text='Enter the resigning date')
    Location = models.CharField(max_length=50,help_text='Enter the location working on')
    Last_working_day = models.DateField(auto_now=False,auto_now_add=False,help_text='Enter the last day of working')
    Department = models.CharField(max_length=50,help_text='Enter the belonging department')
    Designation=models.CharField(max_length=50,help_text='Enter the belomging designation')
    Pan_no=models.CharField(max_length=50,help_text='Enter your Pan No.')
    Epic_no=models.CharField(max_length=50,help_text='Enter your Epic No.')
    Aadhar_card_no=models.CharField(max_length=50,help_text='Enter Aadhar Card No.')
    Bank_acc_no=models.IntegerField(help_text='Enter the Bank Account Number')
    PF_acc_no=models.IntegerField(help_text='Enter the Provident Fund Acccount Number')
    UAN_No=models.IntegerField(help_text='Enter the UAN No.')
    ESIC_no = models.IntegerField(help_text='Enter the ESIC number')
    Reporting_person=models.CharField(max_length=50,help_text='Enter the name of reporting person')
    Joining_Salary=models.IntegerField(help_text='Enter the joining Salary')
    Present_Salary=models.IntegerField(help_text='Enter the present Salary')
    Transfer_date=models.DateField(auto_now=False,auto_now_add=False,help_text='Enter the date of transfer')
    Transfer_to=models.CharField(max_length=50,help_text='Enter the place transferred to.')
    Last_date_of_increment= models.DateField(auto_now=False,auto_now_add=False,help_text='Enter last date of increment')
    Employee_Status=models.CharField(max_length=50,choices=status,help_text='Enter the employment status of employee.')

    def __unicode__(self):
        return self.Department


class references(models.Model):
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE,help_text='Choose for which employee you want to enter details')
    Name = models.CharField(max_length=50,help_text='Enter the references name')
    Contact_No = models.IntegerField(help_text='Enter the references contact number')

    def __unicode__(self):
        return self.Name
