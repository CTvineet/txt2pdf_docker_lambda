FROM public.ecr.aws/lambda/python:3.8
# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Install awslambdaric
RUN pip install awslambdaric
# Copy function code
COPY app.py ./
# Set the CMD to your handler
CMD ["app.lambda_handler"]
# Set the entrypoint
ENTRYPOINT ["/var/lang/bin/python3.8", "-m", "awslambdaric"]
