#!/bin/bash

echo "Running security scan with Trivy..."
trivy image mydockerhub/myapp:latest
    