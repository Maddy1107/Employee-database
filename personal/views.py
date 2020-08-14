from django.shortcuts import render,get_object_or_404,render_to_response
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import xlwt
from .utils import render_to_pdf
from .models import Employee,family,med,emergency,education,employment,references

#-----------------------------------------------------------

def index(request):
    return render(request,'personal/home3.html')

def index2(request):
    return render(request,'personal/home1.html')


#----------------------------------------------EXCEL EXPORT

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('med')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Employee_id','Blood_group','Ailments','Allergies']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = med.objects.all().values_list('Employee_id', 'Blood_group', 'Ailments', 'Allergies')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)


    wb.save(response)
    return response


#--------------------------------------------------------GENERATE PDFS

def generator(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    context = {'emp': emp}
    return render(request, 'personal/generators.html', context)


def generate_JL(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/Joining Letter.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_NOC(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/Noc.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_CL(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/Confrimation.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_COD(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/COD.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_OL(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/offer.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_EI(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/exit.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_IL(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/increment.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_transfer(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/transfer.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_PL(request,emp_id):
    emp1=Employee.objects.get(pk=emp_id)
    data={
        'emp1' : emp1,
        }
    pdf = render_to_pdf('personal/generators/promotion.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

#----------------------------------------------------------------

def emps(request):
    all_emp= Employee.objects.all()
    context = {'all_emp' : all_emp}
    return render(request,'personal/emp_add1.html', context)

def emps2(request):
    all_emp= Employee.objects.all()
    context = {'all_emp' : all_emp}
    return render(request,'personal/emp_add.html', context)

#------------------------------------------------------------------

def details(request,emp_id):
    emp = get_object_or_404(Employee, pk=emp_id)
    context = {'emp':emp }
    return render(request,'personal/full_detail1.html', context)

def details1(request,emp_id):
    emp = get_object_or_404(Employee, pk=emp_id)
    context = {'emp':emp }
    return render(request,'personal/full_detail.html', context)

#---------------------------------------------------------------------


def custom_404(request):
    return render_to_response('personal/error_employee.html')

def success(request):
    return render(request,'personal/success.html')

#------------------------------------------------NEW ADDITIONS TO DATABASE

class EmpCreate(CreateView):
    model=Employee
    fields=['Employee_id','Employee_name','Fathers_name','Date_Of_Birth','Gender','Present_Address','Permanent_Address',
            'Residential_Contact_No','Permanent_Contact_No','Email_id','Marital_Status','Marriage_Date']
    success_url = reverse_lazy('personal:fam-add')
    slug_field = 'Employee_id'

class EmpCreate1(CreateView):
    model=family

    fields=['Employee_id','Name','Date_of_Birth','Gender','Relationship','Occupation']
    success_url = reverse_lazy('personal:fam-add')
    slug_field = 'Employee_id'

class EmpCreate2(CreateView):
    model=med
    fields=['Employee_id','Blood_group','Ailments','Allergies',]
    success_url = reverse_lazy('personal:emer-add')
    slug_field = 'Employee_id'

class EmpCreate3(CreateView):
    model = emergency
    fields = ['Employee_id','Contact_person_name', 'Relation', 'Landline_No', 'Mobile_No', ]
    success_url = reverse_lazy('personal:edu-add')
    slug_field = 'Employee_id'

class EmpCreate4(CreateView):
    model = education
    fields = ['Employee_id', 'Degree', 'Institute', 'From', 'To', 'Percentage']
    success_url = reverse_lazy('personal:edu-add')
    slug_field = 'Employee_id'

class EmpCreate5(CreateView):
    model = employment
    fields = ['Employee_id', 'Date_of_Joining', 'Department', 'Designation','Pan_no','Epic_no','Aadhar_card_no','Bank_acc_no', 'PF_acc_no','ESIC_no','Reporting_person','Joining_Salary','Present_Salary','Last_date_of_increment','Employee_Status']
    success_url = reverse_lazy('personal:ref-add')
    slug_field = 'Employee_id'

class EmpCreate6(CreateView):
    model = references
    fields = ['Employee_id', 'Name', 'Contact_No']
    success_url = reverse_lazy('personal:ref-add')

#--------------------------------------------------------------EXISTING ADD
def addxlist(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    context = {'emp': emp}
    return render(request, 'personal/Add_existing.html', context)

class EmpCreatex(CreateView):
    model=Employee
    fields=['Employee_id','Employee_name','Fathers_name','Date_Of_Birth','Gender','Present_Address','Permanent_Address',
            'Residential_Contact_No','Permanent_Contact_No','Email_id','Marital_Status','Marriage_Date']
    success_url = reverse_lazy('personal:success')
    slug_field = 'Employee_id'

class EmpCreatex1(CreateView):
    model=family
    fields=['Employee_id','Name','Date_of_Birth','Gender','Relationship','Occupation']
    success_url = reverse_lazy('personal:success')
    slug_field = 'Employee_id'

class EmpCreatex2(CreateView):
    model=med
    fields=['Employee_id','Blood_group','Ailments','Allergies',]
    success_url = reverse_lazy('personal:success')
    slug_field = 'Employee_id'

class EmpCreatex3(CreateView):
    model = emergency
    fields = ['Employee_id','Contact_person_name', 'Relation', 'Landline_No', 'Mobile_No', ]
    success_url = reverse_lazy('personal:success')
    slug_field = 'Employee_id'

class EmpCreatex4(CreateView):
    model = education
    fields = ['Employee_id', 'Degree', 'Institute', 'From', 'To', 'Percentage']
    success_url = reverse_lazy('personal:success')
    slug_field = 'Employee_id'

class EmpCreatex5(CreateView):
    model = employment
    fields = ['Employee_id', 'Date_of_Joining', 'Department', 'Designation','Pan_no','Epic_no','Aadhar_card_no','Bank_acc_no', 'PF_acc_no','ESIC_no','Reporting_person','Joining_Salary','Present_Salary','Last_date_of_increment','Employee_Status']
    success_url = reverse_lazy('personal:success')
    slug_field = 'Employee_id'

class EmpCreatex6(CreateView):
    model = references
    fields = ['Employee_id', 'Name', 'Contact_No']
    success_url = reverse_lazy('personal:success')

#----------------------------------------------------UPDATES TO THE DATABASE

def UpdateList(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    context = {'emp': emp}
    return render(request, 'personal/UpdateList.html', context)

class EmpUpdate(UpdateView):
    model = Employee
    slug_field = 'Employee_id'
    slug_url_kwarg = 'emp_id'
    success_url = reverse_lazy('personal:employees')
    fields = ['Employee_id', 'Employee_name','Fathers_name', 'Date_Of_Birth', 'Gender', 'Present_Address', 'Permanent_Address',
              'Residential_Contact_No', 'Permanent_Contact_No', 'Email_id', 'Marital_Status', 'Marriage_Date']

class EmpUpdate1(UpdateView):
    model = family
    slug_field = 'Employee_id'
    slug_url_kwarg = 'emp_id'
    success_url = reverse_lazy('personal:employees')
    fields = ['Employee_id', 'Name', 'Date_of_Birth', 'Gender', 'Relationship', 'Occupation']

class EmpUpdate2(UpdateView):
    model = med
    slug_field = 'Employee_id'
    slug_url_kwarg = 'emp_id'
    success_url = reverse_lazy('personal:employees')
    fields = ['Employee_id', 'Blood_group', 'Ailments', 'Allergies', ]

class EmpUpdate3(UpdateView):
    model = emergency
    fields = ['Employee_id', 'Contact_person_name', 'Relation', 'Landline_No', 'Mobile_No', ]
    slug_field = 'Employee_id'
    success_url = reverse_lazy('personal:employees')
    slug_url_kwarg = 'emp_id'

class EmpUpdate4(UpdateView):
    model = education
    fields = ['Employee_id', 'Degree', 'Institute', 'From', 'To', 'Percentage']
    slug_field = 'Employee_id'
    success_url = reverse_lazy('personal:employees')
    slug_url_kwarg = 'emp_id'

class EmpUpdate5(UpdateView):
    model = employment
    fields = ['Employee_id', 'Date_of_Joining', 'Department','Designation','Pan_no','Epic_no','Aadhar_card_no','Bank_acc_no', 'PF_acc_no','ESIC_no','Reporting_person','Joining_Salary','Present_Salary','Last_date_of_increment','Employee_Status']
    slug_field = 'Employee_id'
    slug_url_kwarg = 'emp_id'
    success_url = reverse_lazy('personal:employees')


class EmpUpdate6(UpdateView):
    model = references
    fields = ['Employee_id', 'Name', 'Contact_No']
    slug_field = 'Employee_id'
    slug_url_kwarg = 'emp_id'
    success_url = reverse_lazy('personal:employees')

#-----------------------------------------------------DLETING FROM THE DATABASE

class EmpDelete(DeleteView):
    model=Employee
    slug_field = 'Employee_id'
    slug_url_kwarg = 'emp_id'
    success_url = reverse_lazy('personal:employees1')




















