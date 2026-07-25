#!/bin/bash
# Build script for Render

echo "Building X-HViT Medical Application..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput

echo "Build complete!"