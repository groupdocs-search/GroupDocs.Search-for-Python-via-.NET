FROM python:3.13-slim

# System packages the examples need on Linux, as measured for this release
# (config `linux_packages`). libicu-dev is what the .NET runtime itself needs.
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends libicu-dev libgdiplus \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
