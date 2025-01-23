#DataAdd/views.py
'''
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch
from io import BytesIO
from .models import ProductData


def home(request):
    products = ProductData.objects.all()
    return render(request, 'home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductDataForm()
    return render(request, 'add_product.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(ProductData, pk=pk)
    if request.method == 'POST':
        form = ProductDataForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductDataForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(ProductData, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'delete_product.html', {'product': product})


def generate_pdf(request, pk):
    # Retrieve the product
    product = get_object_or_404(ProductData, pk=pk)

    # Prepare HTTP response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{product.product_name}.pdf"'

    # Create a buffer for the PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    # Define the table data
    data = [
        ["Field", "Value"],
        ["Sr. No", product.sr_no],
        ["Date", product.date],
        ["Product Name", product.product_name],
        ["Specification", product.specification],
        ["Customer Name", product.customer_name],
        ["L1 Price", product.l1_price],
        ["GST %", product.gst_percent],
        ["Gross Cost Value", product.gross_cost_value],
        ["USD", product.usd],
        ["Vendor 1 (Name)", product.vendor1_name],
        ["Vendor 1 (Price)", product.vendor1_price],
        ["Vendor 2 (Name)", product.vendor2_name],
        ["Vendor 2 (Price)", product.vendor2_price],
        ["Vendor 3 (Name)", product.vendor3_name],
        ["Vendor 3 (Price)", product.vendor3_price],
        ["Remarks", product.remarks],
    ]

    # Create the table and set its width to fit the A4 page
    table = Table(data, colWidths=[2.5 * inch, 4 * inch])  # Adjust widths as needed
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Build the PDF
    doc.build([table])

    # Write the PDF to the response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductData
from .forms import ProductDataForm  # Import your form here

def edit_product(request, pk):
    product = get_object_or_404(ProductData, pk=pk)  # Get the product or return 404
    if request.method == 'POST':
        form = ProductDataForm(request.POST, instance=product)  # Bind the form to the product instance
        if form.is_valid():
            form.save()  # Save the updated product data
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = ProductDataForm(instance=product)  # Populate the form with the product data
    return render(request, 'edit_product.html', {'form': form})  # Render the template with the form
'''
#-----------------------------------------------------------------------------------------------------------
#---------- New Edit code ----------------------------------------------------------


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch
from io import BytesIO
from .models import ProductData
from .forms import ProductDataForm
#---------------------------------------------------------------------------------

from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductData


def home(request):
    query = request.GET.get('search', '')

    # If there's a query, filter products based on all relevant fields
    if query:
        products = ProductData.objects.filter(
            sr_no__icontains=query) | ProductData.objects.filter(
            date__icontains=query) | ProductData.objects.filter(
            product_name__icontains=query) | ProductData.objects.filter(
            specification__icontains=query) | ProductData.objects.filter(
            customer_name__icontains=query) | ProductData.objects.filter(
            l1_price__icontains=query) | ProductData.objects.filter(
            gst_percent__icontains=query) | ProductData.objects.filter(
            gross_cost_value__icontains=query) | ProductData.objects.filter(
            usd__icontains=query) | ProductData.objects.filter(
            vendor1_name__icontains=query) | ProductData.objects.filter(
            vendor1_price__icontains=query) | ProductData.objects.filter(
            vendor2_name__icontains=query) | ProductData.objects.filter(
            vendor2_price__icontains=query) | ProductData.objects.filter(
            vendor3_name__icontains=query) | ProductData.objects.filter(
            vendor3_price__icontains=query) | ProductData.objects.filter(
            remarks__icontains=query)
    else:
        products = ProductData.objects.all()

    return render(request, 'home.html', {'products': products, 'query': query})


#-------------------------------------------------------------------------------------------------------


def all_products(request):
    products = ProductData.objects.all()
    return render(request, 'all_products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = ProductDataForm()
    return render(request, 'add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(ProductData, pk=pk)
    if request.method == 'POST':
        form = ProductDataForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = ProductDataForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(ProductData, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('all_products')
    return render(request, 'delete_product.html', {'product': product})

def generate_pdf(request, pk):
    product = get_object_or_404(ProductData, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{product.product_name}.pdf"'
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    data = [
        ["Field", "Value"],
        ["Sr. No", product.sr_no],
        ["Date", product.date],
        ["Product Name", product.product_name],
        ["Specification", product.specification],
        ["Customer Name", product.customer_name],
        ["L1 Price", product.l1_price],
        ["GST %", product.gst_percent],
        ["Gross Cost Value", product.gross_cost_value],
        ["USD", product.usd],
        ["Vendor 1 (Name)", product.vendor1_name],
        ["Vendor 1 (Price)", product.vendor1_price],
        ["Vendor 2 (Name)", product.vendor2_name],
        ["Vendor 2 (Price)", product.vendor2_price],
        ["Vendor 3 (Name)", product.vendor3_name],
        ["Vendor 3 (Price)", product.vendor3_price],
        ["Remarks", product.remarks],
    ]
    table = Table(data, colWidths=[2.5 * inch, 4 * inch])
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)
    doc.build([table])
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
