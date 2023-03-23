import os
import boto3
from fpdf import FPDF
from io import BytesIO

s3 = boto3.resource('s3')

def convert_to_pdf(file_content):
    # Create a PDF file using FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=15)
    for line in file_content.split('\n'):
        pdf.cell(200, 10, txt=line, ln=1, align='C')
    return pdf

def upload_to_s3(pdf_bytes, bucket_name, key):
    # Upload the PDF file to S3
    s3.Object(bucket_name, key).put(Body=pdf_bytes)

def lambda_handler(event, context):
    # Replace this with the name of your S3 bucket
    bucket_name = 'healthcard.com'
    object_name = event['Records'][0]['s3']['object']['key']
    # Retrieve the file content from S3
    obj = s3.Object(bucket_name, object_name)
    file_content = obj.get()['Body'].read().decode('utf-8')

    # Convert the text file to a PDF
    pdf = convert_to_pdf(file_content)

    # Upload the PDF file back to S3
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    pdf_key = 'my.pdf'
    upload_to_s3(pdf_bytes, "employee-website", pdf_key)
    
    return {
        'statusCode': 200,
        'body': 'PDF conversion complete!'
    }
