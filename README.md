# Image Converter Tool

## Overview
A desktop application built with Python that provides a user-friendly interface for basic image processing tasks. The tool focuses on two main features:
- Converting images between different formats (PNG, JPG, BMP, TIFF)
- Removing image backgrounds

## Key Features

### 1. User Interface
- Clean and intuitive GUI built with tkinter
- Three main sections:
  - Image file selection
  - Output folder selection
  - Format conversion options
- Simple checkbox for background removal
- Clear success/error messages for user feedback

### 2. Format Conversion
- Supports conversion between common image formats:
  - PNG
  - JPG
  - BMP
  - TIFF
- Preserves original image quality
- Maintains original file names with new extensions

### 3. Background Removal
- Optional background removal using rembg library
- Processes images before format conversion
- Maintains transparency in supported formats

## Technical Implementation
- Built using Python's standard libraries and popular packages:
  - tkinter for GUI
  - PIL (Python Imaging Library) for image processing
  - rembg for background removal
- Simple and efficient file handling
- Error handling for common issues:
  - File selection errors
  - Invalid formats
  - Processing failures

## Practical Uses
This tool is particularly useful for:
- Basic image format conversion needs
- Quick background removal tasks
- Simple image processing workflow

## Current Limitations
- Processes one image at a time
- Limited to basic format conversion
- Basic GUI styling
- No image preview functionality

This tool demonstrates a practical implementation of common image processing tasks with a focus on simplicity and ease of use.
