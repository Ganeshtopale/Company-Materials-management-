from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
import csv
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(request):
    products = Product.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(product_name__icontains=search_query)
    return render(request, 'DataAdd/home.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'DataAdd/add_product.html', {'form': form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'DataAdd/update_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')


def export_to_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    writer = csv.writer(response)

    products = Product.objects.all()
    writer.writerow(
        ['Sr. #', 'Customer Name', 'Product Name', 'Specification', 'Target Price', 'UOM', 'Qty', 'Vendor 1',
         'Vendor 2', 'Vendor 3', 'Vendor 4', 'L1 Price', 'Total Price', 'GST %', 'GST Value', 'Remarks'])
    for product in products:
        writer.writerow(
            [product.id, product.customer_name, product.product_name, product.specification, product.target_price,
             product.uom, product.qty, product.vendor_1, product.vendor_2, product.vendor_3, product.vendor_4,
             product.l1_price, product.total_price, product.gst_percent, product.gst_value, product.remarks])
    return response


def generate_pdf(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template_path = 'DataAdd/pdf_template.html'
    context = {'product': product}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="product_{product.id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
